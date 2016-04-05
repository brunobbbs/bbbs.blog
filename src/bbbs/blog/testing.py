# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import bbbs.blog


class BbbsBlogLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=bbbs.blog)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'bbbs.blog:default')


BBBS_BLOG_FIXTURE = BbbsBlogLayer()


BBBS_BLOG_INTEGRATION_TESTING = IntegrationTesting(
    bases=(BBBS_BLOG_FIXTURE,),
    name='BbbsBlogLayer:IntegrationTesting'
)


BBBS_BLOG_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(BBBS_BLOG_FIXTURE,),
    name='BbbsBlogLayer:FunctionalTesting'
)


BBBS_BLOG_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        BBBS_BLOG_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='BbbsBlogLayer:AcceptanceTesting'
)
