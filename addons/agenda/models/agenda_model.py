from odoo import fields, models

class AgendaModel(models.Model):
    _name = "agenda_model"

    _description = "Test Model"

    name = fields.Char()