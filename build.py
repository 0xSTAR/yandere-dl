#!/usr/bin/env python3
import sys
import os
import platform

import PyInstaller.__main__

os = platform.system() if platform.system()=='Windows' or platform.system()=='Linux' or platform.system()=='Darwin' else sys.exit('ERROR: {} operating system not supported by the build tool.')
is_64=True if sys.maxsize > 2**32 else False
is_cpython = True if platform.python_implementation()=='CPython' else False
py_ver=platform.python_version_tuple()
is_legal_python=True if is_cpython and int(py_ver[0])==3 and int(py_ver[1])>= 6 and int(py_ver[1]) < 11 else sys.exit('Must be using CPython version >= 3.6 and < 3.11')

TARGET = 'src/__main__.py'

def main():
    if os=='Darwin':
        mac_info = platform.mac_ver()
        if not is_64:
            target_arch = 'universal2' if mac_info.machine=='x86' else sys.exit(f"""Architecture: {mac_info.machine} not recognized . . .
            Please report to Issues on the GitHub page what architecture this message states.
            A screenshot would be helpful.""")
            dist_type = '_macOS_universal2'
            try:
                PyInstaller.__main__.run([
                    TARGET,
                    '-y','--clean',
                    '-F','-c',
                    '--icon=yandere.ico',
                    '--target-arch={}'.format(target_arch),
                    '-n=yandere-dl{}'.format(dist_type),
                    '--noupx',
                    #'--distpath {}'.format(os.getcwd()),
                    #'--workpath {}'.format(os.getcwd()+'build_temp')
                ])
            except:
                dist_type='_macOS_generic'
                PyInstaller.__main__.run([
                    TARGET,
                    '-y','--clean',
                    '-F','-c',
                    '--icon=yandere.ico',
                    '-n=yandere-dl{}'.format(dist_type),
                    '--noupx',
                    #'--distpath {}'.format(os.getcwd()),
                    #'--workpath {}'.format(os.getcwd()+'build_temp')
                ])
            return str('yandere-dl{}'.format(dist_type))
        else:
            target_arch = 'arm64' if mac_info.machine=='arm64' else 'x86_64'
            dist_type = '_macOS_arm64' if arch=='arm64' else '_macOS_x86_64'# if arch=='x86_64'
            PyInstaller.__main__.run([
                TARGET,
                '-y','--clean',
                '-F','-c',
                '--icon=yandere.ico',
                '--target-arch={}'.format(target_arch),
                '-n=yandere-dl{}'.format(dist_type),
                '--noupx',
                #'--distpath {}'.format(os.getcwd()),
                #'--workpath {}'.format(os.getcwd()+'build_temp')
            ])
            return str('./dist/yandere-dl{}'.format(dist_type))

    elif os=='Linux': # Linux or Windows
        arch = '_linux64' if is_64 else '_linux32'
        PyInstaller.__main__.run([
            TARGET,
            '-y','--clean',
            '-F',
            #'--icon=yandere.ico',
            '-n=yandere-dl{}'.format(arch),
            '--noupx',
            #'--distpath {}'.format('dist'),
            #'--workpath {}'.format('build_temp')
        ])
        return str('./dist/yandere-dl{}'.format(arch))

    elif os=='Windows':
        arch = '_win64' if is_64 else '_win32'
        PyInstaller.__main__.run([
            TARGET,
            '-y','--clean',
            '-F','-c',
            '--icon=yandere.ico',
            '-n=yandere-dl{}'.format(arch),
            '--noupx',
            #'--distpath={}'.format(os.getcwd()),
            #'--workpath={}'.format(os.getcwd()+'build_temp')
        ])
        return str('./dist/yandere-dl{}.exe'.format(arch))

if __name__ == '__main__':
    happy_accident = main()
    #if os=='Linux' or os=='Darwin':
        #import subprocess
        #subprocess.call(['sudo','chmod','a+rwx',happy_accident])
    print('\n\n\n. . . Done ! \n')
    sys.exit()
