# -*- coding: utf-8 -*-
{
    'name': "Prueba de Odoo",

    'summary': """Version estable""",

    'description': """
		Esto es  lo aprendido en el curso
    """,

    'author': "Soluciones 4G",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Inventario',
    'version': '0.1r',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo.xml',
    ],
    'installable':True,
    'auto_install':False,
}
