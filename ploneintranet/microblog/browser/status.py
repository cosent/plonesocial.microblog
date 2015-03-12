from datetime import datetime
from zope.interface import Interface
from zope.interface import alsoProvides
from zope.interface import implements
from zope.component import adapts
from zope.component import queryUtility
from zope.component import getMultiAdapter

from AccessControl import getSecurityManager
from Products.CMFPlone.interfaces import IPloneSiteRoot
from Acquisition import aq_inner
from Acquisition import aq_chain
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase

from z3c.form import form, field, button
from z3c.form.interfaces import IFormLayer
from plone.z3cform import z2
from plone.z3cform.fieldsets import extensible
from plone.z3cform.interfaces import IWrappedForm
from plone import api

from ..interfaces import IMicroblogTool
from ..interfaces import IStatusUpdate
from ..interfaces import IMicroblogContext

from ploneintranet.microblog.statusupdate import StatusUpdate
from ploneintranet.microblog.utils import get_microblog_context

from .interfaces import IPlonesocialMicroblogLayer
from .interfaces import IStatusProvider

from zope.i18nmessageid import MessageFactory
_ = MessageFactory('ploneintranet.microblog')

try:
    from ploneintranet.attachments.attachments import IAttachmentStoragable
    from ploneintranet.attachments.utils import extract_and_add_attachments
except ImportError:
    IAttachmentStoragable = None


class StatusForm(extensible.ExtensibleForm, form.Form):

    ignoreContext = True  # don't use context to get widget data
    id = None
    label = _(u"Add a comment")
    fields = field.Fields(IStatusUpdate).omit('portal_type',
                                              '__parent__',
                                              '__name__',
                                              'id',
                                              'mime_type',
                                              'creator',
                                              'userid',
                                              'creation_date',
                                              'thread_id')

    def updateFields(self):
        super(StatusForm, self).updateFields()

    def updateWidgets(self):
        super(StatusForm, self).updateWidgets()

    def updateActions(self):
        super(StatusForm, self).updateActions()
        self.actions['cancel'].addClass("hide")
        self.actions['statusupdate'].addClass("standalone")

    @button.buttonAndHandler(_(u"label_statusupdate",
                               default=u"Status Update"),
                             name='statusupdate')
    def handleComment(self, action):

        # Validation form
        data, errors = self.extractData()
        if errors:
            return

        container = queryUtility(IMicroblogTool)
        microblog_context = get_microblog_context(self.context)
        if hasattr(self.context, 'thread_id') and self.context.thread_id:
            thread_id = self.context.thread_id  # threaded
        elif self.context.__class__.__name__ == 'StatusUpdate':
            thread_id = self.context.id  # first reply
        else:
            thread_id = None  # new
        status = StatusUpdate(data['text'],
                              context=microblog_context,
                              thread_id=thread_id)

        file_upload = self.request.get('form.widgets.attachments')
        attachments_supported = (
            IAttachmentStoragable is not None and
            IAttachmentStoragable.providedBy(status))
        if attachments_supported and file_upload:
            token = self.request.get('attachment-form-token')
            extract_and_add_attachments(
                file_upload, status, workspace=self.context, token=token)

        # debugging only
#        container.clear()

        # save the status update
        container.add(status)

        # Redirect to portal home
        self.request.response.redirect(self.action)

    def attachment_form_token(self):
        member = api.user.get_current()
        username = member.getUserName()
        return "{0}-{1}".format(
            username,
            datetime.utcnow().strftime('%Y%m%d%H%M%S%f'))

    @button.buttonAndHandler(_(u"Cancel"))
    def handleCancel(self, action):
        # This method should never be called, it's only there to show
        # a cancel button that is handled by a jQuery method.
        pass  # pragma: no cover


class StatusProvider(object):
    """Re-usable microblog status form provider"""
    implements(IStatusProvider)
    adapts(Interface, IPlonesocialMicroblogLayer, Interface)

    form = StatusForm
    index = ViewPageTemplateFile('status.pt')

    comment_transform_message = "What's on your mind?"

    def __init__(self, context, request, view):
        self.context = context
        self.request = request
        self.view = view
        # optional give thread to provider
        self.thread_id = None
        self.portlet_data = None  # used by microblog portlet
        # force microblog context to IMicroblogContext or SiteRoot
        for obj in aq_chain(self.context):
            if IMicroblogContext.providedBy(obj) \
                    or IPloneSiteRoot.providedBy(obj):
                self.context = obj
                return

    def update(self):
        self._update()

    def _update(self):
        if self.available:
            z2.switch_on(self, request_layer=IFormLayer)
            self.form = self.form(aq_inner(self.context), self.request)
            alsoProvides(self.form, IWrappedForm)
            self.form.update()

    def render(self):
        return self.index()

    __call__ = render

    @property
    def available(self):
        permission = "Plone Social: Add Microblog Status Update"
        have_permission = getSecurityManager().checkPermission(
            permission, self.context)
        is_installed = queryUtility(IMicroblogTool)
        return have_permission and is_installed

    def is_attachment_supported(self):
        return IAttachmentStoragable is not None

    @property
    def compact(self):
        if not self.portlet_data:
            return True
        else:
            return self.portlet_data.compact

    def portal_url(self):
        portal_state = getMultiAdapter((self.context, self.request),
                                       name=u'plone_portal_state')
        return portal_state.portal_url()

    def get_users(self):
        """Get user names"""
        user_ids = self.request.get('users')
        if user_ids:
            return [
                {
                    'id': user.id,
                    'fullname': user.getProperty('fullname'),
                }
                for user in api.user.get_users()
                if user.id in user_ids
            ]
        return []


class StatusReplyProvider(StatusProvider):
    """status form provider to be used on a statusupdate"""
    implements(IStatusProvider)
    adapts(IStatusUpdate, IPlonesocialMicroblogLayer, Interface)

    form = StatusForm
    label = _(u"Add a reply")

    index = ViewPageTemplateFile('status.pt')
    available = True  # fixme security check

    comment_transform_message = "Reply..."

    def __init__(self, context, request, view):
        self.context = context
        self.request = request
        self.view = view
        self.thread_id = context.thread_id or context.id  # catch first
        self.portlet_data = None  # used by microblog portlet

        self.form.fields['text'].field.title = self.label


class StatusViewlet(StatusProvider, ViewletBase):

    def __init__(self, context, request, view, manager):
        StatusProvider.__init__(self, context, request, view)
        ViewletBase.__init__(self, context, request, view, manager)

    def update(self):
        self._update()
        ViewletBase.update(self)
