# -*- coding: utf-8 -*-
from odoo import models, fields

class Property(models.Model):
    _name = "real_state.property"

    name = fields.Char(string="name", required=True)
    description = fields.Text(string="description")
    postcode = fields.Char(string="postcode")
    date_availability = fields.Datetime(string="date_availability")
    expected_price = fields.Float(string="expected_price")
    selling_price = fields.Float(string="selling_price")
    bedrooms = fields.Integer(string="bedrooms")
    living_area = fields.Integer(string="living_area")
    garage = fields.Boolean(string="garage")
    garden_orientation = fields.Selection(string="garden_orientation", selection=[
        ("north", "North"),
        ("south", "South"),
        ("east", "East"),
        ("west", "West"),
    ], required=True)