{
    'name': 'Panama Electronic Invoicing (FEL)',
    'version': '1.0',
    'category': 'Accounting/Localizations',
    'summary': 'Integration with Panama FEL electronic invoicing system',
    'description': 'This module integrates Odoo with the Panama Facturación Electrónica (FEL) system.',
    'author': 'Your Name',
    'website': 'https://www.yourwebsite.com',
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'views/fel_config_views.xml',
        'views/account_move_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}