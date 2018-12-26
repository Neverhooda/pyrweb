#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cherrypy
from os.path import abspath

import subprocess
from os import listdir
from os.path import isfile, join
from random import randint


class Yorick(object):
    """ Service for control Yorick"""
    @cherrypy.expose
    def index(self):
        with open('static/index.html', 'r') as file:
            return file.readlines()

    @cherrypy.expose
    def greet(self, name):
        return 'Hello {}!'.format(name)

    @cherrypy.expose
    def play_random(self):
        print("hello")
        dir_t = "/home/gress/work/terminator"
        # dir_t = "C:/Users/ank/Downloads/Telegram Desktop"
        only_files = [f for f in listdir(dir_t) if isfile(join(dir_t, f))]
        mp3_files = []
        for mp in only_files:
            if mp.endswith('.mp3'):
                mp3_files.append(mp)
        subprocess.check_call(["mpg123", "%s/%s" % (dir_t, mp3_files[randint(0, len(mp3_files))])])
        return mp3_files
        # return '{"status":200}'


configuration = {
            '/': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': abspath('./static')
                },
}

cherrypy.config.update({'server.socket_host': '64.72.221.48',
                        'server.socket_port': 80,
                       })

cherrypy.quickstart(Yorick(), '/', configuration)
