#!/usr/bin/python
try:
    import web
except ImportError:
    sys.path.append("/home/edrop/opt/python/lib/python2.4/site-packages")
    import web

from web import form

class deploy:
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
