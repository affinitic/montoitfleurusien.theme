# -*- coding: utf-8 -*-

from Acquisition import aq_inner
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from plone.memoize.instance import memoize


class MonToitNews(BrowserView):

    @memoize
    def getNews(self, nombre):
        """
        récupère les actualités (news)
        """
        catalog = getToolByName(aq_inner(self.context), 'portal_catalog')
        listMonToitNews = catalog(portal_type='News Item',
                                  review_state=('external', 'internal'),
                                  sort_on='Date',
                                  sort_order='reverse',
                                  sort_limit=nombre)
        return listMonToitNews

    def getNewsIconURL(self, newsBrain):
        """
        récupère l'icône d'une news (ou celle par défaut)
        """
        news = newsBrain.getObject()
        if news.getImage():
            return 'image_tile'
        else:
            # image par défaut
            return 'news.png'


class MonToitEvents(BrowserView):

    @memoize
    def getEvents(self, nombre):
        """
        reécupère les événements-calendriers (events)
        """
        catalog = getToolByName(aq_inner(self.context), 'portal_catalog')
        listMonToitevents = catalog(portal_type='Event',
                                    review_state=('external', 'internal'),
                                    sort_on='Date',
                                    sort_order='reverse',
                                    sort_limit=nombre)

        return [listMonToitevents.getObject() for event in listMonToitevents]
