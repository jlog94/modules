# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Curso (models.Model):
    _name = 'openacademy.curso'  # Model odoo name

    # Field reserved to identified name re
    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    responsible_id = fields.Many2one('res.users', ondelete='set null', string="Responsible", index=True)
    session_ids = fields.One2many('openacademy.session', 'course_id', string="Sessions")

    @api.multi
    def copy(self, default=None):
        default = dict(default or {})

        copied_count = self.search_count(
            [('name', '=like', u"Copy of {}%".format(self.name))])
        if not copied_count:
            new_name = u"Copy of {}".format(self.name)
        else:
            new_name = u"Copy of {} ({})".format(self.name, copied_count)

        default['name'] = new_name
        return super(Curso, self).copy(default)
    
    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         "El titulo del curso no debe ser igual a la descripcion"),

        ('name_unique',
         'UNIQUE(name)',
         "El nombre del curso debe ser unico"),
    ]
