#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:ls


import tornado.ioloop
import tornado.web
from config1 import options
from core import index


def main():
    application = tornado.web.Application([
        (r"/", index.IndexHandler),
    ], debug=True)
    application.listen(options["port"])
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
