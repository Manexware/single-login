{
    'name': 'Restrict Multiple Sign in for Same User',
	'version': '1.0',
	'category': 'Tools',
	'sequence': 1,
	'summary': 'Restrict Multiple Sign in for Same User in Odoo.',
	'description': """
        Restrict Multiple Sign in for Same User
        =======================================

        Module to Restrict Multiple Sign in for Same User in Odoo.""",
	'author': 'Nevpro Business Solutions Pvt Ltd.',
	'website': 'http://www.nevpro.co.in',
	'depends': ['web', 'base'],
	'data': [
	    'views/single_login.xml',
		'views/custom_template.xml',
		'scheduler.xml',
	],
	'demo_xml': [],
	'installable': True,
	'application': True,
	'auto_install': False,
}