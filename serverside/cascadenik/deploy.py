#!/usr/bin/env python

"""
Release Steps
-------------

 * do once:
    * svn mkdir ../../../tags/cascadenik
    * create ~./pypirc file with pypi user:pass
    * python setup.py register

 * do each release:
    * Edit CHANGELOG.txt
    * rebuild MANIFEST 'python setup.py sdist --manifest-only'
    * Increment 'version' below, in __init__.py, and in setup.py
    * Commit changes to SVN - confirm correct r# in CHANGELOG
    * Run `deploy.py` to create sdist, upload, and create tag
    * Commit tag
    * Update Google Code wiki

"""

import sys
import time
from subprocess import call as subcall

DEBUG = False

app = 'cascadenik'
version = '0.2.0'
tag_dir= '../../../tags/%s' % app

def call(cmd):
  if DEBUG:
      print 'DEBUG: will execute -> %s' % cmd  
  else:
      try:
        response = subcall(cmd,shell=True)
        print
        time.sleep(1)
        if response < 0:
          sys.exit(response)
      except OSError, E:
        sys.exit(E)

def cleanup():
    call('sudo rm -rf *.egg* *.pyc dist/ build/')

def tag():
    call('svn copy https://mapnik-utils.googlecode.com/svn/trunk/serverside/%s/ https://mapnik-utils.googlecode.com/svn/tags/%s/%s -m "tagging %s %s release"' % (app,app,version,app,version))

def package():
    call('python setup.py sdist upload')
    call('cp dist/%s-%s.tar.gz %s' % (app,version,tag_dir))
    call('svn add %s/%s-%s.tar.gz' % (tag_dir,app,version))

def commit():
    call('svn ci %s -m "tagging %s %s release"' % (tag_dir,app,version))
    
def main():
    cleanup()
    tag()
    package()
    cleanup()
    #commit()
    
if __name__ == '__main__':
    main()