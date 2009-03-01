from cx_Freeze import setup, Executable

#from setuptools import setup
from distutils.command.install import INSTALL_SCHEMES
import sys
import qczechtile

required_python_version = '2.5'

###############################################################################
# arguments for the setup command
###############################################################################
name = "QCzechtile"
version = qczechtile.__versionstr__
desc = ""
long_desc = """"""
classifiers=[
    "Development Status :: 3 - Alpha",
    "License :: OSI Approved :: BSD"
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Topic :: Text Processing",
    "Topic :: Text Processing :: Markup :: HTML",
    "Topic :: Text Processing :: Markup :: XML"
]
author="Lukas Almad Linhart"
author_email="bugs@almad.net"
url="http://projects.almad.net/python-czechtile"
cp_license="BSD"
packages=[
    "qczechtile"
]

data_files=[]
scripts = ['bin/qczechtile']
executables = [Executable(script='bin/qczechtile', packages=['sip'])]


def main():
    if sys.version < required_python_version:
        s = "I'm sorry, but %s %s requires Python %s or later."
        print s % (name, version, required_python_version)
        sys.exit(1)

    # set default location for "data_files" to platform specific "site-packages"
    # location
    for scheme in INSTALL_SCHEMES.values():
        scheme['data'] = scheme['purelib']

    setup(
        name=name,
        scripts=scripts,
        version=version,
        description=desc,
        long_description=long_desc,
        classifiers=classifiers,
        author=author,
        author_email=author_email,
        url=url,
        license=cp_license,
        packages=packages,
#        download_url=download_url,
        data_files=data_files,
        executables=executables,
    )

if __name__ == "__main__":
    main()
