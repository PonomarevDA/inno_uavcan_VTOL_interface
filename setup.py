#!/usr/bin/env python3
#
# Copyright (C) 2016  UAVCAN Development Team  <uavcan.org>
#
# This software is distributed under the terms of the MIT License.
#
# Author: Pavel Kirienko <pavel.kirienko@zubax.com>
#

import glob
import os
import shutil
import sys

import pkg_resources
from setuptools import setup, find_packages
from setuptools.archive_util import unpack_archive

PACKAGE_NAME = 'uavcan_gui_tool'
HUMAN_FRIENDLY_NAME = 'UAVCAN GUI Tool'

SOURCE_DIR = os.path.abspath(os.path.dirname(__file__))

sys.path.append(os.path.join(SOURCE_DIR, PACKAGE_NAME))
from version import __version__

assert sys.version_info[0] == 3, 'Python 3 is required'

ICON_HIRES = os.path.join(PACKAGE_NAME, 'icons', 'logo_256x256.png')
ICON_ICO = os.path.join(PACKAGE_NAME, 'icons', 'logo.ico')

#
# Checking if git submodules are initialized
#
if not glob.glob(os.path.join(SOURCE_DIR, PACKAGE_NAME, 'thirdparty', '*', '*')):
    print('Initializing git submodules...')
    res = os.system('git submodule update --init --recursive')
    if res != 0:
        raise RuntimeError('Could not initialize git submodules [%d]' % res)

#
# Setup args common for all targets
#
args = dict(
    name=PACKAGE_NAME,
    version='.'.join(map(str, __version__)),
    packages=find_packages(),
    setup_requires=[
        'setuptools',
        'setuptools_git>=1.0',
    ],
    install_requires=[
        'setuptools>=18.5',
        'pyuavcan_v0>=1.0.0.dev34',
        'pyserial~=3.0',
        'qtawesome~=0.3.1',
        'qtconsole~=4.2.0',
        'pyyaml~=5.1',
        'easywebdav~=1.2',
        'numpy',
        'pyqt5',
        'traitlets',
        'jupyter-client',
        'ipykernel',
        'pygments',
        'qtpy'
    ],
    # We can't use "scripts" here, because generated shims don't work with multiprocessing pickler.
    entry_points={
        'gui_scripts': [
            '{0}={0}.main:main'.format(PACKAGE_NAME),
        ]
    },
    include_package_data=True,

    # Meta fields, they have no technical meaning
    description='UAVCAN Bus Management and Diagnostics App',
    author='UAVCAN Development Team',
    author_email='uavcan@googlegroups.com',
    url='http://uavcan.org',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',
        'Topic :: Scientific/Engineering :: Visualization',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Environment :: X11 Applications',
        'Environment :: Win32 (MS Windows)',
        'Environment :: MacOS X',
    ]
)

if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
    # Delegating the desktop integration work to 'install_freedesktop'
    args.setdefault('setup_requires', []).append('install_freedesktop')

    icon_path = os.path.join(sys.prefix, 'share/icons/hicolor/256x256/apps', PACKAGE_NAME + '.png')

    args['desktop_entries'] = {
        PACKAGE_NAME: {
            'Name': HUMAN_FRIENDLY_NAME,
            'GenericName': args['description'],
            'Comment': args['description'],
            'Categories': 'Development;Utility;',
            'Icon': icon_path,
        }
    }

    # Manually installing the icon (we can't use data_files because... oh, it just doesn't work here)
    icon_installation_path = args['desktop_entries'][PACKAGE_NAME]['Icon']
    print('Permanently installing icon to:', icon_installation_path)
    try:
        shutil.rmtree(icon_installation_path)
    except Exception:
        pass
    try:
        os.makedirs(os.path.dirname(icon_installation_path))
    except Exception:
        pass
    shutil.copy(ICON_HIRES, icon_installation_path)

    # Manually invoking the freedesktop extension - this should work even if we're getting installed via PIP
    sys.argv.append('install_desktop')


#
# Windows-specific options and hacks
#
if os.name == 'nt':
    args.setdefault('install_requires', []).append('cx_Freeze ~= 6.1')

if ('bdist_msi' in sys.argv) or ('build_exe' in sys.argv):
    import cx_Freeze

    # cx_Freeze can't handle 3rd-party packages packed in .egg files, so we have to extract them for it
    dependency_eggs_to_unpack = [
        'uavcan',
        'qtpy',
        'qtconsole',
    ]
    unpacked_eggs_dir = os.path.join('build', 'hatched_eggs')
    sys.path.insert(0, unpacked_eggs_dir)
    try:
        shutil.rmtree(unpacked_eggs_dir)
    except Exception:
        pass
    for dep in dependency_eggs_to_unpack:
        for egg in pkg_resources.require(dep):
            if not os.path.isdir(egg.location):
                unpack_archive(egg.location, unpacked_eggs_dir)

    import qtawesome
    import qtconsole
    import PyQt5
    import zmq
    import pygments
    import IPython
    import ipykernel
    import jupyter_client
    import traitlets
    import numpy

    # Oh, Windows, never change.
    missing_dlls = glob.glob(os.path.join(os.path.dirname(numpy.core.__file__), '*.dll'))
    print('Missing DLL:', missing_dlls)

    # My reverence for you, I hope, will help control my inborn instability; we are accustomed to a zigzag way of life.
    args['options'] = {
        'build_exe': {
            'packages': [
                'pkg_resources',
                'zmq',
                'pygments',
                'jupyter_client',
            ],
            'include_msvcr': True,
            'include_files': [
                                 PACKAGE_NAME,
                                 # These packages don't work properly when packed in .zip, so here we have another bunch of ugly hacks
                                 os.path.join(unpacked_eggs_dir, os.path.dirname(PyQt5.__file__)),
                                 os.path.join(unpacked_eggs_dir, os.path.dirname(qtawesome.__file__)),
                                 os.path.join(unpacked_eggs_dir, os.path.dirname(qtconsole.__file__)),
                                 os.path.join(unpacked_eggs_dir, os.path.dirname(zmq.__file__)),
                                 os.path.join(unpacked_eggs_dir, os.path.dirname(pygments.__file__)),
                                 os.path.join(unpacked_eggs_dir, os.path.dirname(IPython.__file__)),
                                 os.path.join(unpacked_eggs_dir, os.path.dirname(ipykernel.__file__)),
                                 os.path.join(unpacked_eggs_dir, os.path.dirname(jupyter_client.__file__)),
                                 os.path.join(unpacked_eggs_dir, os.path.dirname(traitlets.__file__)),
                                 os.path.join(unpacked_eggs_dir, os.path.dirname(numpy.__file__)),
                             ] + missing_dlls,
        },
        'bdist_msi': {
            'initial_target_dir': '[ProgramFilesFolder]\\UAVCAN\\' + HUMAN_FRIENDLY_NAME,
        },
    }
    args['executables'] = [
        cx_Freeze.Executable(os.path.join('bin', PACKAGE_NAME),
                             base='Win32GUI',
                             icon=ICON_ICO,
                             shortcutName=HUMAN_FRIENDLY_NAME,
                             shortcutDir='ProgramMenuFolder'),
    ]
    # Dispatching to cx_Freeze only if MSI build was requested explicitly. Otherwise continue with regular setup.
    # This is done in order to be able to install dependencies with regular setuptools.
    def setup(*args, **kwargs):
        cx_Freeze.setup(*args, **kwargs)

setup(**args)
