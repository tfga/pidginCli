# coding=utf-8

#@PydevCodeAnalysisIgnore
from setuptools import setup, find_packages

setup(
    name = "PidginCli",
    version = "1.0",
    packages = find_packages('src'),
    package_dir = {'':'src'},
    
    #
    # dependencies: apt-get install python-setuptools
    # 
    # TODO? O próprio setuptools pode ser incluído no egg:
    #    
    #     http://packages.python.org/distribute/setuptools.html#using-setuptools-without-bundling-it
    #

    # 
    # Test dependencies
    # 
    # Para instalar (e rodar os testes -- mas isso não está funcionando):
    #     
    #     python setup.py test
    #     
    tests_require = [
        'mock'
    ],
    
    entry_points = {
        'console_scripts': [
#           'scriptName = my_package.some_module:main_func',
            'pidginMsg            = PidginCli.Main:entryPoint'
           ,'_pidginCompleteBuddy = PidginCli.CompleteBuddyMain:entryPoint'

           ,'pidginQuickLaunch    = PidginQuickLaunch.QuickLaunchMain:entryPoint'
        ],
    }
)
