# -*- coding: utf-8 -*-
from odoo import fields, models


class SupplierData(models.Model):
    _name = "materials.supplier"
    _description = "Material Supplier Data Related Model"

    id = fields.Char("Supplier ID",
                     required=True)

    name = fields.Char("Supplier Name",
                       required=True)

    address = fields.Char("Supplier Address",
                          required=True)
