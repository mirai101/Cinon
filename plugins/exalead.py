#config = None
app_cinon = None


def search(domain, limit):
    url = "http://www.exalead.com/search/web/results/?q=%40{word}&elements_per_page=10&start_index={counter}"
    app_cinon.init_search(url, domain, limit, 0, 50, 'Exalead')
    app_cinon.process()
    return app_cinon.get_emails()


class Plugin:
    def __init__(self, app, conf):#
        global app_cinon, config
        #config = conf
        app.register_plugin('exalead', {'search': search})
        app_cinon = app
