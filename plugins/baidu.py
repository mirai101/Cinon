#config = None
app_cinon = None


def search(domain, limit):
    url = 'http://www.baidu.com/search/s?wd="%40{word}"&pn={counter}'
    app_cinon.init_search(url, domain, limit, 0, 10, 'Baidu')
    app_cinon.process()
    return app_cinon.get_emails()


class Plugin:
    def __init__(self, app, conf):#
        global app_cinon, config
        #config = conf
        app.register_plugin('baidu', {'search': search})
        app_cinon = app
