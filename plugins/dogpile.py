
#config = None
app_cinon = None


def search(domain, limit):
    url = 'http://www.dogpile.com/search/web?qsi={counter}&q="%40{word}"'
    app_cinon.init_search(url, domain, limit, 1, 10, 'Dogpile')
    app_cinon.process()
    return app_cinon.get_emails()


class Plugin:
    def __init__(self, app, conf):#
        global app_cinon, config
        #config = conf
        app.register_plugin('dogpile', {'search': search})
        app_cinon = app
