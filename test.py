#!/usr/bin/python
import sys
import logHelper
import component
import logFile
import module

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

urls = (
    '/', 'index',
    '/metaserver', 'log',
    '/mas', 'log',
    '/portal', 'log',
    '/web', 'log',
    '/test', 'log'
    '/deploy', 'deploy'
)

render = web.template.render('templates/')

web.config.debug = True

config = web.storage(
    email='aa.com',
    site_name='V1.0',
    site_desc='',
    static='/static',
)

web.template.Template.globals['config'] = config
web.template.Template.globals['render'] = render


class index:
    def GET(self):
        global render
        init()
        f = genForm()
        datas = []
        return render.log(f, datas, urls)


def genComponets():
    component.components=[]
    component.components.append(component.keyFilter('userid'))
    component.components.append(component.keyFilter('task'))
    component.components.append(component.srcFilter())


def genModules():
    module.modules=[]
    module.modules.append(module.metaserver())
    module.modules.append(module.mas())
    module.modules.append(module.test())
    for module1 in module.modules:
        module.moduleDict[module1.name] = module1


def genForm():
    log_form = form.Form()
    inputs = []
    for component1 in component.components:
        inputs.append(component1.layout())
    inputs.append(form.Button("submit", type="submit", description="search"))
    log_form.inputs = inputs
    return log_form


def parseInput(stor):
    for component1 in component.components:
        value = stor.get(component1.key)
        print component1.key, value
        if value != '':
            component1.data = value

def init():
    genComponets()
    genModules()

class log:
    def GET(self):
        global render
        f = genForm()
        datas = []
        return render.log(f, datas, urls)

    def POST(self):
        global render
        f = genForm()
        stor = web.input(src='all', userid='', trace='')
        print stor
        filters = []
        parseInput(stor)
        if stor.trace != '':
            logItem = logHelper.parseLogItem(stor.trace)
            modules1 = module.findRelationModules(logItem.server)
            datas = []
            before = True
            for module1 in modules1:
                print logItem.server, module1.name
                if logItem.server == module1.name:
                    datas.append(stor.trace.replace('<br>', '<br/>'))
                    before = False
                    continue
                if before:
                    time = component.beforeTime(module1)
                else:
                    time = component.afterTime(module1)
                time.starTime = logItem.startTime
                time.endTime = logItem.endTime
                logs = logFile.getLogs(module1);
                print logs[-1].name
                components = []
                components.append(time)
                components.extend(component.components)
                content = logHelper.findInLastlog(logs[-1].name, logItem.keyId, module1, components)
                datas.extend(content.datas)
            return render.log(f, datas, urls)
        uri = web.ctx.env.get("REQUEST_URI")[1:]
        module1 = None
        if uri != '':
            for oneModule in module.modules:
                if oneModule.name == uri:
                    module1 = oneModule
        if module1 != None and stor.userid != '':
            logs = logFile.getLogs(module1);
            print logs[-1].name
            content = logHelper.findInLastlog(logs[-1].name, stor.userid, module1, component.components)
            datas = content.datas
        else:
            datas = []
        return render.log(f, datas, urls)


if __name__ == "__main__":
    app = web.application(urls, globals())
    init()
    print 'http://127.0.0.1:8080/'
    app.run()
