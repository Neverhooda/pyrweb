#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cherrypy
import os
from os.path import abspath

import json
import uuid
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
        dir_t = "/home/gress/pyrweb/sound"
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
        upload_path = os.path.dirname(__file__)
        upload_filename = ufile.filename
        upload_file = os.path.normpath(
            os.path.join("%s/%s" % (upload_path, "sound"), upload_filename))
        size = 0
        with open(upload_file, 'wb') as out:
            while True:
                data = ufile.file.read(8192)
                if not data:
                    break
                out.write(data)
                size += len(data)
        out = '''
            File received.
            Filename: {}
            Length: {}
            Mime-type: {}
            '''.format(ufile.filename, size, ufile.content_type, data)
        # return out
        if upload_filename.endswith('.mp3'):
            print(upload_file)
            subprocess.check_call(["mpg123", "sound/%s" % upload_filename])
        raise cherrypy.HTTPRedirect("/")

    @cherrypy.expose
    def list(self):
        print("hello")
        # dir_t = "/home/gress/pyrweb/sound"
        dir_t = "C:/Users/ank/Downloads/Telegram Desktop"
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
        data = cherrypy.request.body.read().decode('utf8').replace("'", '"')
        print(data)
        # run()
        name = str(uuid.uuid4())
        subprocess.check_call(["wget", data["url"], "-O", "%s.mp3" % name])
        subprocess.check_call(["mpg123", "sound/%s.mp3" % name])
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
