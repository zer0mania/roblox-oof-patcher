import glob
import os
import sys

print('''
                                               ____               __       __             
                                  ____  ____  / __/  ____  ____ _/ /______/ /_  ___  _____
                                 / __ \/ __ \/ /_   / __ \/ __ `/ __/ ___/ __ \/ _ \/ ___/
                                / /_/ / /_/ / __/  / /_/ / /_/ / /_/ /__/ / / /  __/ /    
                                \____/\____/_/    / .___/\__,_/\__/\___/_/ /_/\___/_/     
                                                 /_/                                
                                                    
                                                    zer0mania#6278
''')

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

list_of_files = glob.glob(os.path.expanduser('~') + '\AppData\Local\Roblox\Versions\*')
latest_dir = max(list_of_files, key=os.path.getctime)

with open(resource_path('ouch.ogg'), 'rb') as f:
    s = f.read()
    f.close()

with open(latest_dir + '\content\sounds\ouch.ogg', 'wb') as f:
    f.truncate(0)
    f.write(s)
    f.close()

print("\n\n                               Successfully patched :) you may close this window now")
input()
