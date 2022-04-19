import subprocess
import os

render_switch = False

# 文件目录开头
file_path_header = r"D:\niu_work\3d\180_BeU\model\V4"

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

count = 0

# 检测文件路径是否有误
def checkPath():
    for index in range(len(file_path_list)):
        global render_switch
        if os.path.exists(file_path_header + file_path_list[index]):
            render_switch = True
        else:
            render_switch = False
            global count
            count = index
            break


# 执行批量渲染
def renderList():
    for index in range(len(file_path_list)):
        subprocess.run(["blender", "-b", file_path_header + file_path_list[index], "-a"], shell = True)
        print(file_path_header + file_path_list[index])


def run():
    checkPath()
    if render_switch:
        print("共渲染 " + str(len(file_path_list)) + " 个文件")
        in_content = input("请确认是否开始渲染（y/n)")
        if in_content == 'y' or in_content == 'Y':
            os.chdir("C:/Program Files\Blender Foundation\Blender 3.1") # 进入 Blender 安装目录
            renderList()
        elif in_content == 'n' or in_content == 'N':
            print("已取消渲染")
        else:
            print("输入有误，请重新输入。")
            in_content = input("请确认是否开始渲染（y/n)")
    else:
        print("第 " + str(count + 1) + " 个文件路径有误")


run()