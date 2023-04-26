# python-grecaptcha
google recaptcha library for recaptcha v2 invisible, probably works with v2/v3 normal as well aslong as you know how to do the frontend

# Installation

just clone the repo or save grecaptcha.py and put it in a folder with ur project :)


# Web.py example

    import web
    import time
    import requests
    from grecaptcha import Grecaptcha

    urls = (
        '/', 'home'
    )

    web.config.debug = True

    templates = web.template.render('templates/')
    app = web.application(urls, globals())
    recaptcha = Grecaptcha(secretkey="6LfihLklAAAAAI1X3swQMRNJLAt0BAvk-sMhTp9c",
                           sitekey="6LfihLklAAAAAPpK7MGkiYI4iIhA-2WuUlfWWNrV")


    class home:
        def GET(self):
            return templates.index()

    def POST(self):
        data = web.input()
        print(data)
        ip = web.ctx['ip']
        if recaptcha.verify(data['g-recaptcha-response'], remoteip='38.240.226.60'):
            return "Success"
        else:
            return "Failure"


    if __name__ == "__main__":
        app = web.application(urls, globals())
        app.run()

