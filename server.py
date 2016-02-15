#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
from livereload import Server, shell

subprocess.run(['ark', 'build'])

server = Server()
server.watch('./*.py', shell('ark build'))
server.watch('./src/**/*.md', shell('ark build'))
server.serve(port=8889, root='./out')
