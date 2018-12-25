#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cherrypy
from os.path import abspath


class Yorick(object):
    """ Service for control Yorick"""
    @cherrypy.expose
    def index(self):
        with open('static/index.html', 'r') as file:
            return file.readlines()

    @cherrypy.expose
    def greet(self, name):
        return 'Hello {}!'.format(name)


configuration = {
            '/': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': abspath('./static')
                },
}


cherrypy.quickstart(Yorick(), '/', configuration)
