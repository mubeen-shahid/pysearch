from setuptools import setup
#from distutils.core import setup
import py2exe, sys, os
sys.argv.append('py2exe')
setup(windows = [{'script': "pysearch_gui.py"}])