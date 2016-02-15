#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from livereload import Server, shell

server = Server()
server.watch('./*.py', shell('ark build'))
server.watch('./src/**/*.md', shell('ark build'))
server.serve(port=8889, root='./out')
