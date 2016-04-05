# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from bbbs.blog.testing import BBBS_BLOG_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that bbbs.blog is properly installed."""

    layer = BBBS_BLOG_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if bbbs.blog is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('bbbs.blog'))

    def test_browserlayer(self):
        """Test that IBbbsBlogLayer is registered."""
        from bbbs.blog.interfaces import IBbbsBlogLayer
        from plone.browserlayer import utils
        self.assertIn(IBbbsBlogLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = BBBS_BLOG_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['bbbs.blog'])

    def test_product_uninstalled(self):
        """Test if bbbs.blog is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('bbbs.blog'))

    def test_browserlayer_removed(self):
        """Test that IBbbsBlogLayer is removed."""
        from bbbs.blog.interfaces import IBbbsBlogLayer
        from plone.browserlayer import utils
        self.assertNotIn(IBbbsBlogLayer, utils.registered_layers())
