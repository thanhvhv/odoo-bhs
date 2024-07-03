# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Hide Won Lead/Opportunities',
    'version': '15.0',
    'category': 'Sales/CRM',
    'sequence': -115,
    'summary': 'Module allows hide won lead/opportunities by optional.',
    'description': "",
    'website': 'https://bachasoftware.com/',
    'depends': ['crm'],
    'data': [
        'views/crm_lead_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/banner.gif'],
    # Author
    'author': 'Bac Ha Software',
    'maintainer': 'Bac Ha Software',
    'license': 'LGPL-3',
}
