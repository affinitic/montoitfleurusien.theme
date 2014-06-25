# -*- coding: utf-8 -*-

from Acquisition import aq_inner
from zope.component import getMultiAdapter
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName


class DiazoParametersView(BrowserView):
    """
    Diazo Parameters methods
    """

    def isPortalFrontPage(self):
        """
        Returns True if we are on portal root or default page
        """
        # Avoid error in plone.app.layout.navigation.defaultpage when getting
        # unexisting objectIds() or getId()
        if getattr(self.context, "getId", None) is None or \
           getattr(self.context, "objectIds", None) is None:
            return False

        context_state = getMultiAdapter((aq_inner(self.context), self.request),
                                        name=u'plone_context_state')
        isRoot = context_state.is_portal_root()
        if not isRoot:
            return False

        portalUrl = getToolByName(self.context, 'portal_url')
        portal = portalUrl.getPortalObject()
        frontPageName = portal.getDefaultPage()
        frontPage = self.context.restrictedTraverse(frontPageName, default=None)
        if self.context == frontPage:
            return True

        return False
