import sys
import webbrowser

from distutils.core import setup


if sys.argv[1] in ('install', 'build', 'sdist', 'bdist_wheel'):
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')


setup(name='rickroll',
      version='1.2',
      description="The Python module that's never gonna give you up.",
      long_description="The Python module that's never gonna let you down.",
      author='James Bennett',
      author_email='james@b-list.org',
      url='https://github.com/ubernostrum/rickroll',
      py_modules=['rickroll'],
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',
                   'Topic :: Internet',
                   'Topic :: Sociology'],
      )
