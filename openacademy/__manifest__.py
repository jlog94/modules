# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """Prueba del Curso""",

    'description': """
        Practicando con Odoo
    """,

    'author': "soluciones4g",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1r',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/view_curso.xml',
        'views/view_session.xml',
        'views/view_partner.xml',
        'views/view_wizard.xml',
        'workflow/session_workflow.xml',
        'report/openacademy_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo_curso.xml',
    ],
    'intallable': True,
    'auto_install': False,
}
