#config = None
app_cinon = None


def search(domain, limit):
    url = "http://www.bing.com/search?q=%40{word}&count=50&first={counter}"
    app_cinon.init_search(url, domain, limit, 0, 50, 'Bing')
    app_cinon.process()
    return app_cinon.get_emails()


class Plugin:
    def __init__(self, app, conf):#
        global app_cinon, config
        #config = conf
        app.register_plugin('bing', {'search': search})
        app_cinon = app
