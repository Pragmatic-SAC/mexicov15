# -*- coding: utf-8 -*-
import logging
from odoo import api, fields, models
from lxml.objectify import fromstring

_logger = logging.getLogger(__name__)
MX_PACKAGING_CATALOG = [
    ('1A1', 'Bidones (Tambores) de Acero 1 de tapa no desmontable'),
    ('1A2', 'Bidones (Tambores) de Acero 1 de tapa desmontable'),
    ('1B1', 'Bidones (Tambores) de Aluminio de tapa no desmontable'),
    ('1B2', 'Bidones (Tambores) de Aluminio de tapa desmontable'),
    ('1D', 'Bidones (Tambores) de Madera contrachapada'),
    ('1G', 'Bidones (Tambores) de Cartón'),
    ('1H1', 'Bidones (Tambores) de Plástico de tapa no desmontable'),
    ('1H2', 'Bidones (Tambores) de Plástico de tapa desmontable'),
    ('1N1', 'Bidones (Tambores) de Metal que no sea acero ni aluminio de tapa no desmontable'),
    ('1N2', 'Bidones (Tambores) de Metal que no sea acero ni aluminio de tapa desmontable'),
    ('3A1', 'Jerricanes (Porrones) de Acero de tapa no desmontable'),
    ('3A2', 'Jerricanes (Porrones) de Acero de tapa desmontable'),
    ('3B1', 'Jerricanes (Porrones) de Aluminio de tapa no desmontable'),
    ('3B2', 'Jerricanes (Porrones) de Aluminio de tapa desmontable'),
    ('3H1', 'Jerricanes (Porrones) de Plástico de tapa no desmontable'),
    ('3H2', 'Jerricanes (Porrones) de Plástico de tapa desmontable'),
    ('4A', 'Cajas de Acero'),
    ('4B', 'Cajas de Aluminio'),
    ('4C1', 'Cajas de Madera natural ordinaria'),
    ('4C2', 'Cajas de Madera natural de paredes a prueba de polvos (estancas a los pulverulentos)'),
    ('4D', 'Cajas de Madera contrachapada'),
    ('4F', 'Cajas de Madera reconstituida'),
    ('4G', 'Cajas de Cartón'),
    ('4H1', 'Cajas de Plástico Expandido'),
    ('4H2', 'Cajas de Plástico Rígido'),
    ('5H1', 'Sacos (Bolsas) de Tejido de plástico sin forro ni revestimientos interiores'),
    ('5H2', 'Sacos (Bolsas) de Tejido de plástico a prueba de polvos (estancos a los pulverulentos)'),
    ('5H3', 'Sacos (Bolsas) de Tejido de plástico resistente al agua'),
    ('5H4', 'Sacos (Bolsas) de Película de plástico'),
    ('5L1', 'Sacos (Bolsas) de Tela sin forro ni revestimientos interiores'),
    ('5L2', 'Sacos (Bolsas) de Tela a prueba de polvos (estancos a los pulverulentos)'),
    ('5L3', 'Sacos (Bolsas) de Tela resistentes al agua'),
    ('5M1', 'Sacos (Bolsas) de Papel de varias hojas'),
    ('5M2', 'Sacos (Bolsas) de Papel de varias hojas, resistentes al agua'),
    ('6HA1', 'Envases y embalajes compuestos de Recipiente de plástico, con bidón (tambor) de acero'),
    ('6HA2', 'Envases y embalajes compuestos de Recipiente de plástico, con una jaula o caja de acero'),
    ('6HB1', 'Envases y embalajes compuestos de Recipiente de plástico, con un bidón (tambor) exterior de aluminio'),
    ('6HB2', 'Envases y embalajes compuestos de Recipiente de plástico, con una jaula o caja de aluminio'),
    ('6HC', 'Envases y embalajes compuestos de Recipiente de plástico, con una caja de madera'),
    ('6HD1', 'Envases y embalajes compuestos de Recipiente de plástico, con un bidón (tambor) de madera contrachapada'),
    ('6HD2', 'Envases y embalajes compuestos de Recipiente de plástico, con una caja de madera contrachapada'),
    ('6HG1', 'Envases y embalajes compuestos de Recipiente de plástico, con un bidón (tambor) de cartón'),
    ('6HG2', 'Envases y embalajes compuestos de Recipiente de plástico, con una caja de cartón'),
    ('6HH1', 'Envases y embalajes compuestos de Recipiente de plástico, con un bidón (tambor) de plástico'),
    ('6HH2', 'Envases y embalajes compuestos de Recipiente de plástico, con caja de plástico rígido'),
    ('6PA1', 'Envases y embalajes compuestos de Recipiente de vidrio, porcelana o de gres, con un bidón (tambor) de acero'),
    ('6PA2', 'Envases y embalajes compuestos de Recipiente de vidrio, porcelana o de gres, con una jaula o una caja de acero'),
    ('6PB1', 'Envases y embalajes compuestos de Recipiente de vidrio, porcelana o de gres, con un bidón (tambor) exterior de aluminio'),
    ('6PB2', 'Envases y embalajes compuestos de Recipiente de vidrio, porcelana o de gres, con una jaula o una caja de aluminio'),
    ('6PC', 'Envases y embalajes compuestos de Recipiente de vidrio, porcelana o de gres, con una caja de madera'),
    ('6PD1', 'Envases y embalajes compuestos de Recipiente de vidrio, porcelana o de gres, con bidón (tambor) de madera contrachapada'),
    ('6PD2', 'Envases y embalajes compuestos de Recipiente de vidrio, porcelana o de gres, con canasta de mimbre'),
    ('6PG1', 'Envases y embalajes compuestos de Recipiente de vidrio, porcelana o de gres, con un bidón (tambor) de cartón'),
    ('6PG2', 'Envases y embalajes compuestos de Recipiente de vidrio, porcelana o de gres, con una caja de cartón'),
    ('6PH1', 'Envases y embalajes compuestos de Recipiente de vidrio, porcelana o de gres, con un envase y embalaje de plástico expandido'),
    ('6PH2', 'Envases y embalajes compuestos de Recipiente de vidrio, porcelana o de gres, con un envase y embalaje de plástico rígido'),
    ('7H1', 'Bultos de Plástico'),
    ('7L1', 'Bultos de Tela'),
    ('Z01', 'No aplica')
]

class ResPartner(models.Model):
    _inherit = 'res.partner'

    l10n_mx_edi_operator_licence = fields.Char('Operator Licence')


class AccountMove(models.Model):
    _inherit = 'account.move'


    def _l10n_mx_edi_get_packaging_desc(self, code):
        return dict(MX_PACKAGING_CATALOG).get(code, None)

    def _l10n_mx_edi_decode_cfdi(self, cfdi_data=None):
        if cfdi_data is not None:
            cfdi_data = cfdi_data.replace('xmlns__cartaporte20', 'xmlns:cartaporte20')
        result = super(AccountMove, self)._l10n_mx_edi_decode_cfdi(cfdi_data=cfdi_data)
        if cfdi_data is not None:
            cfdi = fromstring(cfdi_data)
            if 'cartaporte20' not in cfdi.nsmap:
                return result
            cfdi.attrib['{http://www.w3.org/2001/XMLSchema-instance}schemaLocation'] = '%s %s %s' % (
                cfdi.get('{http://www.w3.org/2001/XMLSchema-instance}schemaLocation'),
                'http://www.sat.gob.mx/CartaPorte20',
                'http://www.sat.gob.mx/sitio_internet/cfd/CartaPorte/CartaPorte20.xsd')
            result['cfdi_node'] = cfdi
        return result

    l10n_mx_edi_is_guide_invoice = fields.Boolean('Is Delivery Guide Invoice', copy=False)
    l10n_mx_edi_vehicle_id = fields.Many2one('l10n_mx_delivery_guide_invoice.vehicle', 'Vehicle Configuration',
                                             copy=False)
    l10n_mx_edi_transport_type = fields.Selection(
        [('00', 'No use of Federal Highways'), ('01', 'Federal Motor Carrier')], string='Type of Transport', copy=False)
    l10n_mx_edi_shipping_id = fields.Many2one('res.partner', string='Address Shipping', copy=False)
    l10n_mx_edi_shipping_filter = fields.Many2many('res.partner', 'res_partner_l10n_mx_edi_shipping',
                                                   compute='_compute_l10n_mx_edi_shipping_filter')
    l10n_mx_edi_origin_id = fields.Many2one('res.partner', string='Origin Shipping', copy=False)
    l10n_mx_edi_origin_filter = fields.Many2many('res.partner', 'res_partner_l10n_mx_edi_origin_filter',
                                                 compute='_compute_l10n_mx_edi_origin_filter')
    l10n_mx_edi_is_export = fields.Char(compute='_l10n_mx_edi_compute_is_export')
    l10n_mx_edi_distance = fields.Integer('Distance to Destination (KM)', copy=False)

    @api.depends('partner_id')
    def _l10n_mx_edi_compute_is_export(self):
        for record in self:
            record.l10n_mx_edi_is_export = record.partner_id.country_id.code != 'MX'

    @api.depends('partner_id')
    def _compute_l10n_mx_edi_shipping_filter(self):
        for move in self:
            _parent = move.partner_id.parent_id if move.partner_id.parent_id.id else move.partner_id
            _address = [_parent.id] + _parent.child_ids.ids
            move.l10n_mx_edi_shipping_filter = _address

    @api.depends('company_id')
    def _compute_l10n_mx_edi_origin_filter(self):
        for move in self:
            _parent = move.company_id.partner_id.parent_id if move.company_id.partner_id.parent_id.id else move.company_id.partner_id
            _address = [_parent.id] + _parent.child_ids.ids
            move.l10n_mx_edi_origin_filter = _address

    @api.model
    def l10n_mx_get_weight_uom(self):
        _weight_uom = self.env['product.template']._get_weight_uom_id_from_ir_config_parameter()
        return _weight_uom
