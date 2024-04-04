{
    'name': 'Gestion des visites',
    'version': '15.0.1.0',
    'author': 'Yeo Ali',
    'category': 'Human Resources/employee',
    'summary': 'Module pour gérer les visites dans une entreprise',
    'description': """
        Ce module permet de gérer les visites dans une entreprise.
    """,
    "license": "AGPL-3",
    "complexity": "normal",
    "website": "https://github.com/lons/visite_management",
   
    'depends': ['base'],
    'data': [
        'view/visite_views.xml',
    ],
    'icon': "icon.png",
    'installable': True,
    'auto_install': False,
}
