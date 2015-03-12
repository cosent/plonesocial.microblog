import time
import unittest2 as unittest
from threading import RLock
from zope.component import queryUtility

from plone import api

from ploneintranet.microblog.testing import \
    PLONESOCIAL_MICROBLOG_PORTAL_SUBSCRIBER_INTEGRATION_TESTING
from ploneintranet.microblog.testing import tearDownContainer

from ploneintranet.microblog.interfaces import IMicroblogTool
from ploneintranet.microblog.statusupdate import StatusUpdate


class PortalSubscriber(object):
    """This object is used to test that we can get the portal
    within a status update subscription.
    """

    def __init__(self):
        self.lock = RLock()
        self.messages = []

    def __call__(self, obj, event):
        portal = api.portal.get()
        with self.lock:
            self.messages.append(
                (obj.text, '/'.join(portal.getPhysicalPath()))
            )


portal_subscriber = PortalSubscriber()


class TestMicroblogPortalSubscriber(unittest.TestCase):

    layer = PLONESOCIAL_MICROBLOG_PORTAL_SUBSCRIBER_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def tearDown(self):
        container = queryUtility(IMicroblogTool)
        tearDownContainer(container)

    def test_add_multi_portal(self):
        portal = api.portal.get()
        self.assertIsNotNone(portal)
        portal_path = '/'.join(portal.getPhysicalPath())
        tool = queryUtility(IMicroblogTool)
        for i in xrange(0, 10):
            su = StatusUpdate('Test {}'.format(str(i + 1)))
            if i == 5:
                time.sleep(1)
            # Next message triggers queue flush
            tool.add(su)
        # Here we need to sleep for some time to give the thread timer
        # queue committer in ploneintranet.microblog
        # time to commit the statuses.
        time.sleep(2)
        self.assertEqual(
            portal_subscriber.messages,
            [
                ('Test 1', portal_path),
                ('Test 2', portal_path),
                ('Test 3', portal_path),
                ('Test 4', portal_path),
                ('Test 5', portal_path),
                ('Test 6', portal_path),
                ('Test 7', portal_path),
                ('Test 8', portal_path),
                ('Test 9', portal_path),
                ('Test 10', portal_path)
            ]
        )
