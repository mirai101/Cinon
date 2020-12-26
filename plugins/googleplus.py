#config = None
app_cinon = None


def search(domain, limit):
    #search google+ only with google search engine
    #who is gonna have google+ indexed better than google itself?
    url = 'https://www.google.com/search?num=100&start={counter}&hl=en&q=site%3Aplus.google.com+intext:"Works at"+-inurl:photos+-inurl:about+-inurl:posts+-inurl:plusones+%40{word}'
    app_cinon.init_search(url, domain, limit, 0, 100, 'Google+')
    app_cinon.process()
    return app_cinon.get_emails()


class Plugin:
    def __init__(self, app, conf):#
        global app_cinon, config
        #config = conf
        app.register_plugin('googleplus', {'search': search})
        app_cinon = app
