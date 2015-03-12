# -*- encoding: utf8 -*-
from Products.CMFPlone.utils import getFSVersionTuple
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider
from ploneintranet.microblog.browser.status import StatusViewlet
from zope import schema
from zope.formlib import form
from zope.i18nmessageid import MessageFactory
from zope.interface import implements

_ = MessageFactory('ploneintranet.microblog')
PLONE4 = getFSVersionTuple()[0] <= 4


class IMicroblogPortlet(IPortletDataProvider):
    """A portlet to render the microblog.
    """

    title = schema.TextLine(title=_(u"Title"),
                            description=_(u"A title for this portlet"),
                            required=True,
                            default=u"Microblog")

    compact = schema.Bool(title=_(u"Compact rendering"),
                          description=_(u"Hide portlet header and footer"),
                          default=True)


class Assignment(base.Assignment):
    implements(IMicroblogPortlet)

    title = u""  # overrides readonly property method from base class

    def __init__(self,
                 title="Microblog",
                 compact=True):
        self.title = title
        self.compact = compact


class Renderer(base.Renderer):

    def __init__(self, context, request, view, manager, data):
        base.Renderer.__init__(self, context, request, view, manager, data)
        self._statusviewlet = StatusViewlet(context, request, view, manager)
        self._statusviewlet.portlet_data = data

    @property
    def available(self):
        return self._statusviewlet.available

    @property
    def compact(self):
        return self.data.compact

    def update(self):
        self._statusviewlet.update()

    render = ViewPageTemplateFile('microblog.pt')

    def statusform(self):
        return self._statusviewlet.render()


class AddForm(base.AddForm):
    if PLONE4:
        form_fields = form.Fields(IMicroblogPortlet)
    else:
        schema = IMicroblogPortlet

    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):
    if PLONE4:
        form_fields = form.Fields(IMicroblogPortlet)
    else:
        schema = IMicroblogPortlet
