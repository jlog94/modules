from odoo import models, fields
'''
Este es la creacion del curso
'''
class Course (models, Model):
    '''
    Esta es la creacion de la clase curso
    '''
    _name = 'openacademy.course'
    # Creacion del campo field
    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
