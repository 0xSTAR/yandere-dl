#!/usr/bin/env python3
import os
import sys
import subprocess
import platform

PLATFORM = platform.system()
if not PLATFORM == 'Windows' or not PLATFORM=='Linux' or not PLATFORM=='Darwin':
    print(f'{PLATFORM} is not supported by bootstrapper')

is_64bit = True if sys.maxsize > 2**32 else False # 2**32 same as pow(2,32)
# ^^^^ for those mac arm64 and mac x86_64 people

is_cpython = True if platform.python_implementation() == 'CPython' else False
PYTHON_VERSION_TUPLE = platform.python_version_tuple() if is_cpython else sys.exit('Must be using CPython ( 3.6 <= version < 3.11 )')
LEGAL_PYTHON_VERSION = True if PYTHON_VERSION_TUPLE[0]=='3' and PYTHON_VERSION_TUPLE[1] >= 6 and PYTHON_VERSION_TUPLE[1] < 11 else False
if not LEGAL_PYTHON_VERSION:print('Must be a version of CPython >= 3.6 and < 3.11'); sys.exit()

CREATED_DISTRIBUTABLE:str = ''

TARGET = './src/__main__.py'
DIST_PATH = os.getcwd()+'/dist_bin'
WORK_PATH = os.getcwd()+'/build_tmp'

def ins():
    current_dir = os.getcwd()

    venv_dir = '.venv' if PLATFORM=='Linux' or PLATFORM=='Darwin' else 'venv'
    if PLATFORM=='Linux' or PLATFORM=='DARWIN' and os.path.isdir('.venv'):
        subprocess.call(['rm','-R',current_dir+'/.venv'])
    elif os.path.isdir('venv'):
        subprocess.call(['rmdir',current_dir+'/venv'])

    script_dir = 'Scripts' if PLATFORM == 'Windows' else 'bin'
    activate = 'activate.bat' if PLATFORM=='Windows' else 'activate'

    subprocess.call([sys.executable,'-m','venv',venv_dir])
    subprocess.call(['{}/{}/{}/{}'.format(current_dir,venv_dir,script_dir,activate)])

    subprocess.call([sys.executable,'-m','pip','install','-r','requirements.txt'])

    # subprocess.call(['deactivate'])
    return

def darwin32(mac_info):
    target_arch = 'universal2' if mac_info.machine=='x86' else sys.exit(f"""Architecture: {mac_info.machine} not recognized . . .
    Please report to Issues on the GitHub page what architecture this message states.
    A screenshot would be helpful.""")
    dist_type = '_macOS_universal2'
    try:
        PyInstaller.__main__.run([
            TARGET,
            '-y','--clean',
            '-F','-c',
            '--icon yandere.ico',
            '--target-arch {}'.format(target_arch),
            '-n yandere-dl{}'.format(dist_type),
            '--noupx',
            '--distpath {}'.format(DIST_PATH),
            '--workpath {}'.format(WORK_PATH)
        ])
    except:
        PyInstaller.__main__.run([
            TARGET,
            '-y','--clean',
            '-F','-c',
            '--icon yandere.ico',
            '-n yandere-dl{}'.format('_macOS_generic'),
            '--noupx',
            '--distpath {}'.format(DIST_PATH),
            '--workpath {}'.format(WORK_PATH)
        ])
    global CREATED_DISTRIBUTABLE
    CREATED_DISTRIBUTABLE = 'yandere-dl{}'.format(dist_type)
    return

def darwin64(mac_info):
    target_arch = 'arm64' if mac_info.machine=='arm64' else 'x86_64'
    dist_type = '_macOS_arm64' if arch=='arm64' else '_macOS_x86_64'# if arch=='x86_64'
    PyInstaller.__main__.run([
        TARGET,
        '-y','--clean',
        '-F','-c',
        '--icon yandere.ico',
        '--target-arch {}'.format(target_arch),
        '-n yandere-dl{}'.format(dist_type),
        '--noupx',
        '--distpath {}'.format(DIST_PATH),
        '--workpath {}'.format(WORK_PATH)
    ])
    global CREATED_DISTRIBUTABLE
    CREATED_DISTRIBUTABLE = 'yandere-dl{}'.format(dist_type)
    return

def win32_64():
    arch = '_win64' if is_64bit else '_win32'
    PyInstaller.__main__.run([
        TARGET,
        '-y','--clean',
        '-F','-c',
        '--icon yandere.ico',
        '-n yandere-dl{}'.format(arch),
        '--noupx',
        '--distpath {}'.format(DIST_PATH),
        '--workpath {}'.format(BUILD_PATH)
    ])
    global CREATED_DISTRIBUTABLE
    CREATED_DISTRIBUTABLE = 'yandere-dl{}'.format('yandere-dl{}'.format(arch+'.exe'))
    return

def linux32_64():
    arch = '_linux64' if is_64bit else '_linux32'
    PyInstaller.__main__.run([
        TARGET,
        '-y','--clean',
        '-F',
        '--icon yandere.ico',
        '-n yandere-dl{}'.format(arch),
        '--noupx',
        '--distpath {}'.format(DIST_PATH),
        '--workpath {}'.format(BUILD_PATH)
    ])
    global CREATED_DISTRIBUTABLE
    CREATED_DISTRIBUTABLE = 'yandere-dl{}'.format('yandere-dl{}'.format(arch))
    return

def build():
    import PyInstaller.__main__

    if PLATFORM=='Windows':win32_64()
    elif PLATFORM=='Linux':linux32_64()
    elif PLATFORM=='Darwin' and is_64bit:darwin64(platform.mac_ver())
    elif PLATFORM=='Darwin' and not is_64bit:darwin32(platform.mac_ver())
    return

def aftermath():
    subprocess.call(['deactivate'])
    if os.path.isfile(DIST_PATH+'/'+CREATED_DISTRIBUTABLE) and PLATFORM=='Darwin' or PLATFORM=='Linux':
        subprocess.call(['sudo','chmod','a+rwx',DIST_PATH+'/'+CREATED_DISTRIBUTABLE])
    return

def main():
    ins()
    build()
    aftermath()
    return

if __name__ == '__main__':
    main()
    sys.exit()
