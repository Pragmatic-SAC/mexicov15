# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Complemento de Factura Porte - MX',
    'version': '15.0.1',
    'author': 'Pragmatic S.A.C',
    'category': 'Hidden',
    'summary': 'Complemento para la factura porte con el CFDI 4.0',
    'license': 'LGPL-3',
    'contributors': [
        'Kelvin Meza <kmeza@pragmatic.com.pe>',
    ],
    'depends': [
        'product_unspsc',
        'l10n_mx_edi_40',
    ],
    'data': [
        'data/40/cfdi.xml',
        'security/ir.model.access.csv',
        'views/l10n_mx_edi_vehicle.xml',
        'views/res_partner.xml',
        'views/account_move.xml',
        'views/l10n_mx_delivery_guide_invoice_trailer.xml',
        'views/product_template.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
}
