#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:ls


import tornado.ioloop
import tornado.web
import tornado.options

tornado.options.define("port",default=8888,type=int)

class MainHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        self.write("Hello, world")

def main():
    application = tornado.web.Application([
        (r"/", MainHandler),
    ],debug=True)
    application.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()