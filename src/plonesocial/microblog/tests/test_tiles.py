# -*- coding: utf-8 -*-
from plone import api
from plonesocial.microblog.browser.interfaces import IPlonesocialMicroblogLayer
from plonesocial.microblog.tool import MicroblogTool
from plonesocial.microblog.testing import (
    PLONESOCIAL_MICROBLOG_INTEGRATION_TESTING
)
from plonesocial.activitystream.interfaces import IStatusActivityReply
from plonesocial.microblog.statusupdate import StatusUpdate
from time import sleep
from zope.interface import alsoProvides
import unittest2 as unittest


class TestSetup(unittest.TestCase):

    layer = PLONESOCIAL_MICROBLOG_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        alsoProvides(self.request, IPlonesocialMicroblogLayer)

    def test_newpostbox_tile_on_portal(self):
        ''' This will test the existence of the newpostbox.tile
        and its functionality
        '''
        tile = api.content.get_view(
            'newpostbox.tile',
            self.portal,
            self.request
        )
        # we have a post container which is the microblog tool
        self.assertIsInstance(tile.post_container, MicroblogTool)
        # we dont' have a post context
        self.assertEqual(tile.post_context, None)
        # we have an attachment form token
        self.assertRegexpMatches(
            tile.attachment_form_token,
            'test-user-([0-9]*)'
        )
        # we are not posting
        self.assertEqual(tile.is_posting, False)
        self.assertEqual(tile.post_text, u'')
        self.assertEqual(tile.post_attachment, None)
        # calling update does not create a post
        tile.update()
        self.assertEqual(tile.post, None)
        # check if we render correctly
        self.assertIn('div id="microblog"', tile())

    def test_newpostbox_tile_submission_on_portal(self):
        ''' This will test the existence of the newpostbox.tile
        and its functionality
        '''
        request = self.request.clone()
        request.form.update({
            'form.widgets.text': u'Testing post',
            # 'form.widgets.attachments': u'No attachments',
            'form.buttons.statusupdate': '1'
        })
        request.other['ACTUAL_URL'] = 'http://nohost'

        tile = api.content.get_view(
            'newpostbox.tile',
            self.portal,
            request
        )
        # we are not posting
        self.assertEqual(tile.is_posting, True)
        self.assertEqual(tile.post_text, u'Testing post')
        # self.assertEqual(tile.post_attachment, u'No attachments')
        # calling update does not create a post
        tile.update()
        self.assertIsInstance(tile.post, StatusUpdate)

    def test_newpostbox_tile_submission_on_statusupdate(self):
        ''' This will test the existence of the newpostbox.tile
        and its functionality
        '''
        # First we post
        request = self.request.clone()
        request.form.update({
            'form.widgets.text': u'Testing post',
            # 'form.widgets.attachments': u'No attachments',
            'form.buttons.statusupdate': '1'
        })
        request.other['ACTUAL_URL'] = 'http://nohost'
        tile = api.content.get_view(
            'newpostbox.tile',
            self.portal,
            request
        )
        tile.update()

        # Now we have a post with an id
        thread_id = tile.post.id

        # Then we post a reply on it
        request = self.request.clone()
        request.other['ACTUAL_URL'] = 'http://nohost'
        request.form.update({
            'form.widgets.text': u'Testing replies',
            'thread_id': thread_id,
            'form.buttons.statusupdate': '1',
        })
        tile = api.content.get_view(
            'newpostbox.tile',
            self.portal,
            request
        )
        # the tile works in the context os the previous status update
        self.assertEqual(tile.post_context.id, thread_id)
        # that has no repies
        replies = tuple(tile.post_context.replies())
        self.assertEqual(len(replies), 0)
        # until the tile is processed
        tile.update()
        # after the async machinery has finished
        # we have one reply
        sleep(2)
        replies = tuple(tile.post_context.replies())
        self.assertEqual(len(replies), 1)
        # which is our newly created post
        self.assertEqual(replies[0], tile.post)
        # We want the reply to implement IStatusActivityReply to prevent
        # having it listed directly in the stream
        self.assertTrue(IStatusActivityReply.providedBy(tile.post))
