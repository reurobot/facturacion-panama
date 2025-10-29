# -*- coding: utf-8 -*-

from odoo import models, fields, api
import zeep

class AccountMove(models.Model):
    _inherit = 'account.move'

    fel_cufe = fields.Char(string='CUFE')
    fel_status = fields.Char(string='FEL Status')

    def action_post(self):
        res = super(AccountMove, self).action_post()
        for move in self:
            if move.move_type == 'out_invoice':
                move._send_to_fel()
        return res

    def _send_to_fel(self):
        config = self.env['fel.config'].search([('company_id', '=', self.company_id.id)], limit=1)
        if not config:
            return
        # Generate FEL data from invoice
        datos = self._prepare_fel_data()
        if datos:
            try:
                client = zeep.Client(wsdl=config.wsdl_url)
                response = client.service.Enviar(**datos)
                self.fel_cufe = response.get('cufe')
                self.fel_status = 'Sent'
            except Exception as e:
                self.fel_status = f'Error: {str(e)}'

    def _prepare_fel_data(self):
        # Implement XML data preparation based on invoice
        # This is a simplified example
        return {
            'tokenEmpresa': self.env['fel.config'].search([('company_id', '=', self.company_id.id)], limit=1).token_empresa,
            'tokenPassword': self.env['fel.config'].search([('company_id', '=', self.company_id.id)], limit=1).token_password,
            'documento': {
                'codigoSucursalEmisor': '0000',
                'tipoSucursal': '1',
                'datosTransaccion': {
                    'tipoEmision': '01',
                    'tipoDocumento': '01',
                    'numeroDocumentoFiscal': self.name,
                    'puntoFacturacionFiscal': '001',
                    'naturalezaOperacion': '01',
                    'tipoOperacion': 1,
                    'destinoOperacion': 1,
                    'formatoCAFE': 1,
                    'entregaCAFE': 1,
                    'envioContenedor': 1,
                    'procesoGeneracion': 1,
                    'tipoVenta': 1,
                    'fechaEmision': self.invoice_date.strftime('%Y-%m-%dT%H:%M:%S-05:00'),
                    'cliente': {
                        'tipoClienteFE': '02',
                        'tipoContribuyente': 1,
                        'numeroRUC': self.partner_id.vat or '',
                        'pais': 'PA',
                        'correoElectronico1': self.partner_id.email or '',
                        'razonSocial': self.partner_id.name
                    }
                },
                'listaItems': {
                    'item': [{
                        'descripcion': line.product_id.name,
                        'cantidad': str(line.quantity),
                        'precioUnitario': str(line.price_unit),
                        'precioItem': str(line.price_subtotal),
                        'valorTotal': str(line.price_total),
                        'tasaITBMS': '01',  # Simplified
                        'valorITBMS': str(line.price_total - line.price_subtotal)
                    } for line in self.invoice_line_ids]
                },
                'totalesSubTotales': {
                    'totalPrecioNeto': str(self.amount_untaxed),
                    'totalITBMS': str(self.amount_tax),
                    'totalFactura': str(self.amount_total),
                    'nroItems': str(len(self.invoice_line_ids))
                }
            }
        }