# -*- coding: utf-8 -*-
{
    'name': "hospital_management_system",

    'summary': "hospital",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','account', 'stock', 'hr',],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/patient.xml',
        'views/doctor.xml',
        'views/doctor_appointment.xml',
        'views/department.xml',
        'views/hospital_room.xml',
        'views/hospital_medicine.xml',
        'views/medical_report.xml',
        'views/hospital_bill.xml',
    ],
    # only loaded in demonstration mode
    'demo': [ ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}

