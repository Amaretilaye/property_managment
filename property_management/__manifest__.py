{
    'name': "Property Management",
    'version': '1.0',
    'summary': 'This module provides a complete property rental management system for real estate businesses and property managers. It enables users to manage properties, register tenants, create and track lease agreements, and automate rent calculations and payments. ',
    'depends': ['base', 'mail'],
    'author': 'Amare Tilaye',
    'sequence': 0,
    'category': 'Real Estate',
    'website': 'https://example.com/learn-more-about-my-module',

    'data': [
        'security/ir.model.access.csv',
        'views/property_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}
