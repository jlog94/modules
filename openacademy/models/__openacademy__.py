from manifest import models, fields, api

class Course (model.Model):
    _name = 'openacademy.course'

    name = fields.Char(string="Title", required=True)
    description = field.Text(string="Description")
