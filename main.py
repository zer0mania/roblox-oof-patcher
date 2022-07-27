import glob
import os

print('''
                                               ____               __       __             
                                  ____  ____  / __/  ____  ____ _/ /______/ /_  ___  _____
                                 / __ \/ __ \/ /_   / __ \/ __ `/ __/ ___/ __ \/ _ \/ ___/
                                / /_/ / /_/ / __/  / /_/ / /_/ / /_/ /__/ / / /  __/ /    
                                \____/\____/_/    / .___/\__,_/\__/\___/_/ /_/\___/_/     
                                                 /_/                                
                                                    
                                                    zer0mania#6278
''')

list_of_files = glob.glob(os.path.expanduser('~') + '\AppData\Local\Roblox\Versions\*')
latest_dir = max(list_of_files, key=os.path.getctime)

with open('ouch.ogg', 'rb') as f:
    s = f.read()
    f.close()

with open(latest_dir + '\content\sounds\ouch.ogg', 'wb') as f:
    f.truncate(0)
    f.write(s)
    f.close()

print("\n\n                               Successfully patched :) you may close this window now")
input()