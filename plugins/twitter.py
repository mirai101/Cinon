#config = None
app_cinon = None


def search(domain, limit):
    all_emails = []
    app_cinon.show_message("[+] Searching in Twitter")

    yahooUrl = 'http://search.yahoo.com/search?p=site%3Atwitter.com+intitle:"on Twitter"+%40{word}&n=100&ei=UTF-8&va_vt=any&vo_vt=any&ve_vt=any&vp_vt=any&vd=all&vst=0&vf=all&vm=p&fl=0&fr=yfp-t-152&xargs=0&pstart=1&b={counter}'
    app_cinon.init_search(yahooUrl, domain, limit, 1, 100, 'Yahoo + Twitter')
    app_cinon.process()
    all_emails += app_cinonget_emails()

    bingUrl = 'http://www.bing.com/search?q=site%3Atwitter.com+intitle:"on Twitter"+%40{word}&count=50&first={counter}'
    app_cinon.init_search(bingUrl, domain, limit, 0, 50, 'Bing + Twitter')
    app_cinon.process()
    all_emails += app_cinon.get_emails()

    googleUrl = 'https://www.google.com/search?num=100&start={counter}&hl=en&q=site%3Atwitter.com+intitle:"on Twitter"+"%40{word}"'
    app_cinon.init_search(googleUrl, domain, limit, 0, 100, 'Google + Twitter')
    app_cinon.process()
    all_emails += app_cinon.get_emails()

    url = 'http://www.baidu.com/search/s?wd=site%3Atwitter.com+intitle:"on Twitter"+"%40{word}"&pn={counter}'
    app_cinon.init_search(url, domain, limit, 0, 10, 'Baidu + Twitter')
    app_cinon.process()
    all_emails += app_cinon.get_emails()

    url = 'http://www.exalead.com/search/web/results/?q=site%3Atwitter.com+intitle:"on Twitter"+%40{word}&elements_per_page=10&start_index={counter}'
    app_cinon.init_search(url, domain, limit, 0, 50, 'Exalead + Twitter')
    app_cinon.process()
    all_emails += app_cinon.get_emails()

    #dogpile seems to not support site:

    return all_emails


class Plugin:
    def __init__(self, app, conf):#
        global app_cinon, config
        #config = conf
        app.register_plugin('twitter', {'search': search})
        app_cinon = app
