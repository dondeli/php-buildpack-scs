#!/usr/bin/python

import os, sys, json

BPDIR = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))
NDIR = os.path.join(BPDIR, 'defaults', 'options.json')
LOLO = '/home/taademi6/Desktop/cf/php-buildpack/defaults/options.json'

fh = open(LOLO, 'rt')


print(json.load(fh))
