#config = None
app_cinon = None


def search(domain, limit):
    url = 'https://www.google.com/search?num=100&start={counter}&hl=en&q="%40{word}"'
    app_cinon.init_search(url, domain, limit, 0, 100, 'Google')
    app_cinon.process()
    return app_cinon.get_emails()


class Plugin:
    def __init__(self, app, conf):#
        global app_cinon, config
        #config = conf
        app.register_plugin('googles', {'search': search})
        app_cinon = app
