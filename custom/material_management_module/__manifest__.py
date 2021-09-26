# -*- coding: utf-8 -*-
{
    'name' : 'Material Management Module',
    'version' : '1.0',
    'summary' : 'Material Management Module',
    'sequence' : 10,
    'description' : """Material Management Module""",
    'category' : 'Productivity',
    'website' : '',
    'depends' : ['website'],
    'data' : [
        'security/ir.model.access.csv',
        'views/material/form.xml',
        'views/material/list.xml',
        'views/header.xml',
        'views/footer.xml',
        'views/material.xml',
        'views/supplier.xml'
    ],
    'demo' : [],
    'qweb' : [],
    'installable' : True,
    'application' : True,
    'auto_install' : False
}
