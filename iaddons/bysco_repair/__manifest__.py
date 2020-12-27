# -*- coding: utf-8 -*-
{
    'name': "维修单",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'repair'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'report/paperformat.xml',
        'report/bysco_gds_repair_reports.xml',
        'report/bysco_gds_repair_templates_repair_order.xml',
        # 'report/bysco_repair_report.xml',
        # 'report/bysco_repair_report.xml',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
