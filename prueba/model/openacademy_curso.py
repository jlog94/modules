from manifest import models, fields
'''
Este es la creacion del curso
'''
clas Course(models, Model):
'''
Esta es la creacion de la clase
'''
    _name = 'openacademy.course'
    # Creacion del campo field
    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
