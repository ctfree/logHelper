#!/usr/bin/python
import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

try:
    import web
except ImportError:
    sys.path.append("/home/edrop/opt/python/lib/python2.4/site-packages")
    import web

from web import form

log_form = form.Form(
    form.Textbox('userid', description='userid'),
    form.Textbox('task', description='task'),
    form.Checkbox('src', value='web', description='web'),
    form.Checkbox('src', value='windows', description='windows'),
    form.Radio('src', ['web', 'windows']),
    form.Button("submit", type="submit", description="search"),
)
form.AttributeList
log_form1 = form.Form(
    form.Textbox('userid', description='userid'),
    form.Textbox('task', description='task'),
    form.Checkbox('src', value='web', description='web'),
    form.Checkbox('src', value='windows', description='windows'),
    form.Button("submit", type="submit", description="search"),
)

print log_form.render()
