import functools
import xmlrpclib
HOST = '172.17.0.2'
PORT = 8069
DB = 'odoo_course'
USER = 'jog@soluciones4g.com'
PASS = 'mascota2017'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST, PORT)

# 1. Login
uid = xmlrpclib.ServerProxy(ROOT + 'common').login(DB, USER, PASS)
print "Iniciaste sesion como %s (uid:%d)" % (USER, uid)

call = functools.partial(
    xmlrpclib.ServerProxy(ROOT + 'object').execute,
    DB, uid, PASS)
#SESSION
# 2. Read the sessions
model = 'openacademy.session'
method_name = 'search_read'
domain = []
sessions = call(model, method_name, domain, ['course_id','name', 'seats','taken_seats'])
#sessions = call('openacademy.session', 'search_read', [], ['course_id','name', 'seats','taken_seats'])
print "sessions",sessions
for session in sessions:
    print "ID %s Session %s (%s acientos), acientos ocupados: %s" % (session['id'],session['name'], session['seats'],session['taken_seats'])

method_name="search_read"
domain=[('name','=','Curso Odoo 1')]
course_ids=call('openacademy.course','search',domain)
course_id=course_ids[0]
print 'course_ids',course_ids

#method_name='create'
#course_id=call('openacademy.course', method_name,{'name':'Curso Odoo 1'})

method_name='create'
responsible_id=call('res.partner','search',[('name','=','TELCEL')])[0]
print "responsible_id",responsible_id
new_sesion_id= call(model, method_name,{
    'name':'Sesion de wf',
    'instructor_id':responsible_id,
    'course_id': course_id,
    #'attendee_ids':[(4,responsible_id)],
    'attendee_ids':[(4,11),(4,9)],
    })
print "new_sesion_id",new_sesion_id
#CREAR UNA SESION //////////////////////////////////////////////////////////////////////////////////////////////

#new_sesion_id=call('openacademy.session','create',{'name':'Curso 2','course_id':34,'seats':2,'duration':1.0}) ##hace un registros

#responsible_id=call('res.partner','search',[('name','=','TELCEL')])[0]
#new_sesion_id=call('openacademy.session','create',{
#    'name':'Viernes',
#    'instructor_id':responsible_id,
#    'course_id':course_id,
#    'attendee_ids':[(4,responsible_id)]})

#COURSE
# 3. Read the course
#models = 'openacademy.course'
#courses = call(models, method_name, domain, ['name'])
#courses = call('openacademy.course', 'search_read', [], ['name'])
#for course in courses:
#    print "ID %s" % (course['name'])

#CREAR UN CURSO ///////////////////////////////////////////////////////////////////////////////////////////////
#new_curso_id=call('openacademy.course','create',{'name':'Curso de Verano 1','description':'Curso de Verano 1'}) #ERROR constraint
#new_curso_id=call('openacademy.course','create',{'name':'Curso de Verano 50','description':'Curso de Verano 1'}) #Solo si el nombre es diferente lo inserta