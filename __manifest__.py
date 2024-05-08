# -*- coding: utf-8 -*-
{
    'name' : 'Owl Tutorial',
    'version' : '17.0',
    'summary': 'Owl Tutorial',
    'sequence': -1,
    'description': """Owl Tutorial""",
    'category': 'Website',
    'depends' : ['web', 'website'],
    'data': [
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_frontend': [
            'qweb_tutorial/static/src/components/**/*',
        ],
    },
}
