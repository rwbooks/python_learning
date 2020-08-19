#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:ls

from tornado.web import RequestHandler

class IndexHandler(RequestHandler):
    def get(self,*args,**kwargs):
        self.write("it's test!")