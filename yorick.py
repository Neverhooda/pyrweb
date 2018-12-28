"""@package Yorick web ui
web service for ...
"""

# !/usr/bin/env python
# -*- coding: UTF-8 -*-

import cherrypy
import os
from os.path import abspath

import json
import subprocess
import wget

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
    def features(self):
        with open('static/features.html', 'r') as file:
            return file.readlines()

    @cherrypy.expose
    def left_hand(self, action, parameters):
        print("Left", action, parameters)
        return '{"status":200}'

    @cherrypy.expose
    def right_hand(self, action, parameters):
        print("Right", action, parameters)
        return '{"status":200}'

    @cherrypy.expose
    def greet(self, name):
        return 'Hello {}!'.format(name)

    @cherrypy.expose
    def play_custom(self, sound):
        print(sound)
        subprocess.check_call(["mpg123", "sound/%s" % sound])
        return '{"status":200}'

    @cherrypy.expose
    def play_random(self):
        print("hello")
        dir_t = "/home/gress/work/pyrweb/sound"
        # dir_t = "C:/Users/ank/Downloads/Telegram Desktop"
        only_files = [f for f in listdir(dir_t) if isfile(join(dir_t, f))]
        mp3_files = []
        for mp in only_files:
            if mp.endswith('.mp3'):
                mp3_files.append(mp)
        subprocess.check_call(["mpg123", "%s/%s" % (dir_t, mp3_files[randint(0, len(mp3_files))])])
        return mp3_files
        # return '{"status":200}'

    @cherrypy.expose
    def upload(self, ufile):
        upload_path = "/home/gress/work/pyrweb/sound"
        upload_filename = ufile.filename
        upload_file = os.path.normpath(
            os.path.join(upload_path, upload_filename))

        size = 0
        with open(upload_file, 'wb') as out:
            while True:
                data = ufile.file.read(8192)
                if not data:
                    break
                out.write(data)
                size += len(data)

        if upload_filename.endswith('.mp3'):
            print(upload_file)
            subprocess.check_call(["mpg123", "sound/%s" % upload_filename])
        raise cherrypy.HTTPRedirect("/")

    @cherrypy.expose
    def list(self):
        print("hello")
        dir_t = "/home/gress/work/pyrweb/sound"
        # dir_t = "C:/Users/ank/Downloads/Telegram Desktop"
        # dir_t = "C:/work"
        only_files = [f for f in listdir(dir_t) if isfile(join(dir_t, f))]
        list_mp3 = []
        for mp in only_files:
            if mp.endswith('.mp3'):
                list_mp3.append(mp)
        return json.dumps(list_mp3)

    @cherrypy.expose
    def play_song(self, select_song):
        print(select_song)
        subprocess.check_call(["mpg123", "sound/%s" % select_song])
        raise cherrypy.HTTPRedirect("/")

    @cherrypy.expose
    def upload_by_url(self):
        data_raw = cherrypy.request.body.read().decode('utf8').replace("'", '"')
        data = json.loads(data_raw)
        print(data)
        # run()
        filename = wget.download(data["url"], out="sound")
        print(filename)
        subprocess.check_call(["mpg123", filename])
        return '{"status":200}'


configuration = {
            '/': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': abspath('./static')
                },
}

cherrypy.config.update({'server.socket_host': '127.0.0.1',
                        'server.socket_port': 80,
                       })

cherrypy.quickstart(Yorick(), '/', configuration)
