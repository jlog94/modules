from manifest import models, fields

'''
Este es la creacion del curso
'''
clas Course(models,Model):
    '''
    Esta es la creacion de la clase
    '''
    _name = 'openacademy.course'
    name = fields.Char(string="Title", required=True) #Creacion del campo field
    description = fields.Text(string="Description")
