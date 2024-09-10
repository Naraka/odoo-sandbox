from odoo import models, fields, api

class SaleOrderForecast(models.Model):
    _inherit = 'sale.order'

    forecasted_sales = fields.Float(string="Sales forecasting")

