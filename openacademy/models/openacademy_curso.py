# -*- coding: utf-8 -*-
from odoo import models, fields


class Curso (models.Model):
    _name = 'openacademy.curso'  # Model odoo name

    # Field reserved to identified name re
    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
