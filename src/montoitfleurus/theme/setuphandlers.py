# -*- coding: utf-8 -*-

import logging
from plone import api

logger = logging.getLogger('montoitfleurus.theme')


def install(context):
    if context.readDataFile('montoitfleurus.theme-default.txt') is None:
        return

    logger.info('Installing montoitfleurus.theme')
    portal = context.getSite()

    existingIds = portal.objectIds()

    # Create 3 Documents for top boxes
    # setTitle needed because of https://github.com/plone/plone.api/issues/99
    if not 'boite-presentation' in existingIds:
        page = api.content.create(container=portal, type='Document',
                                  id='boite-presentation',
                                  title="Présentation")
        page.setTitle("Présentation")
        page.setExcludeFromNav(True)
        api.content.transition(obj=portal['boite-presentation'],
                               transition='publish')
    if not 'boite-devenir-locataire' in existingIds:
        page = api.content.create(container=portal, type='Document',
                                  id='boite-devenir-locataire',
                                  title="Devenir locataire")
        page.setTitle("Devenir locataire")
        page.setExcludeFromNav(True)
        api.content.transition(obj=portal['boite-devenir-locataire'],
                               transition='publish')
    if not 'boite-vous-etes-locataire' in existingIds:
        page = api.content.create(container=portal, type='Document',
                                  id='boite-vous-etes-locataire',
                                  title="Vous êtes locataire")
        page.setTitle("Vous êtes locataire")
        page.setExcludeFromNav(True)
        api.content.transition(obj=portal['boite-vous-etes-locataire'],
                               transition='publish')

    portal.setLayout('homepage')
