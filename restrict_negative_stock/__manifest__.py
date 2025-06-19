# -*- coding: utf-8 -*-
{
    'name': "Restrict Negative Stock",
    'summary': "When someone Validate Delivery It Restrict",
    'description': """
        In Stock.picking if Delivery validate it check the On hand Qtantity when it more then Demand.
    """,
    'author': "Strata ERP",
    'website': "https://www.strataerp.com",
    'category': 'Inventory',
    'version': '0.1',
    'depends': ['base' ,'stock_delivery'],
    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}

