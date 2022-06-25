# -*- encoding: utf-8 -*-

{
    'name': 'Iraq COA',
    'version': '15.0',
    'author': "wincode",
    'maintainer': 'Wincode',
    'price': '150.0',
    'currency': 'USD',
    'website': "http://wincode.io",
    'category': 'Localization',
    'description': """
     Iraq COA.
    """,
    'depends': ['account', 'l10n_multilang'],
    'data': [
        'data/account_chart_template_data.xml',
        'data/account.group.csv',
        'data/account.account.template.csv',
        'data/l10n_ye_chart_data.xml',
        'data/account_chart_template_configure_data.xml',
    ],
     'images': ['static/description/banner.png'],
     'license': 'AGPL-3',
    'post_init_hook': 'load_translations',
}
