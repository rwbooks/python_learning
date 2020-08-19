#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:ls


import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        self.write("Hello, world")

def main():
    application = tornado.web.Application([
        (r"/", MainHandler),
    ],debug=True)
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()