# Blender Transfer Com Render

import bpy
import os
import subprocess

# 文件目录开头
file_path_header = r"C:\Users\lnlao\Desktop"

# 文件名
file_path_list = [
    r"\01.blend",
    r"\02.blend",
    r"\03.blend",
    r"\04.blend",
    r"\05.blend",
    r"\06.blend",
    r"\07.blend",
    r"\08.blend"
    ]

for i in file_path_list:
    os.chdir("C:/Program Files\Blender Foundation\Blender 3.1")
    subprocess.run(["blender", "-b", file_path_header + file_path_list[i], "-a"], shell = True)