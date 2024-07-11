{
    'name': "BH Auto Create User",
    'version': '16.0.1.0.0',
    'description': """
       Automatically create a new user from a new employee 
    """,
    'author': 'Bac Ha Software',
    'company': 'Bac Ha Software',
    'maintainer': 'Bac Ha Software',
    'website': "https://bachasoftware.com",
    'category': 'Human Resources',
    'depends': ['hr', 'hr_recruitment'],
    'data': [
        'views/hr_views.xml',
    ],
    'images': ['static/description/useremployee.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'application': True
}
