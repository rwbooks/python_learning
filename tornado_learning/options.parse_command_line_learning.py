#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:ls


import tornado.ioloop
import tornado.web
import tornado.options

tornado.options.define("port",default=8888,type=int)
tornado.options.define("list",default=[],type=str,multiple=True)

class MainHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        self.write("Hello, world")

def main():
    # 获取命令行参数
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r"/", MainHandler),
    ],debug=True)
    application.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()