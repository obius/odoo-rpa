{
    'name': 'Hello World App',
    'version': '1.0.0',
    'category': 'Tools',
    'summary': 'A simple Hello World application for Odoo',
    'description': """
Hello World App
===============

This is a simple Hello World application that demonstrates basic Odoo functionality.
It includes:
- A simple model to store hello world messages
- Basic views to display and manage messages
- Menu items for easy access

Perfect for learning Odoo development or as a starting template.
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/hello_world_views.xml',
        'data/demo_data.xml',
    ],
    'demo': [
        'data/demo_data.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'images': ['static/description/icon.png'],
    'price': 0.0,
    'currency': 'EUR',
}