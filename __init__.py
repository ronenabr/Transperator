# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Transperator
                                 A QGIS plugin
 Make black background invisible in selected layers
                             -------------------
        begin                : 2015-11-16
        copyright            : (C) 2015 by ronen@visionmap
        email                : ronen@visionmap.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Transperator class from file Transperator.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .transperator import Transperator
    return Transperator(iface)
