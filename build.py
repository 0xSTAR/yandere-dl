#!/usr/bin/env python3

from __future__ import print_function
import os, sys, subprocess

ONE_FILE = True
# VENV = True

if __name__ == '__main__':
    #def ins(mod):
    #    # void = os.devnull -- doesn't have a file no.
    #    void = open(os.devnull,'w')
    #    #try:
    #    subprocess.check_call([sys.executable,'-m','pip','install','-U',mod],
    #                                    stdout=void,stderr=void)
    #    #except CalledProcessError:

    def ins(virtenv:bool = True):
    	#void = open(os.devnull,'w')
    	subprocess.check_call([sys.executable,'-m','pip','install','-r','requirements.txt'])

    TARGET = './yandere-dl.py'
    def build(onefile:bool = True):
        if onefile:
            subprocess.check_call(['pyinstaller','--icon','yandere.ico','--onefile',TARGET])
            return
        subprocess.check_call(['pyinstaller','--icon','yandere.ico',TARGET])
        return

    def main():
    	#ins(VENV)
        ins()
        build(ONE_FILE)

    main()
    sys.exit()
