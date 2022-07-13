import re
import os
import json
import subprocess

from tqdm import tqdm
from builtins import str


def work():
    inputStr = input("请输入：");
    print("你输入的内容是: ", inputStr)
    work_dir = os.getcwd()  # 获取当前路径
    listdir = os.listdir(work_dir)  # 返回path指定的文件夹包含的文件或文件夹的名字的列表
    while (inputStr != "quit" and inputStr != 'q'):
        for dirName in listdir:
            file_path = os.path.join(work_dir, dirName)  # 拼接完整的路径
            print(file_path)
            if os.path.isdir(file_path):  # 判断是否是目录
                try:
                    os.chdir(file_path)  # 移动到制定的目录下
                    result = os.popen(inputStr)  # 执行输入的命令
                    print(result.read())  # 打印命令执行的结果
                except:
                    print()
                finally:
                    print()
        inputStr = input("请输入：")


dir = "D:/idea workspace/Miner/tmp/"
to = "D:/dataset/"
source = "D:/pythonProject/task1/source/map.txt"
# os.chdir(dir)
fs = open(source, 'r', encoding='UTF-8')
s = fs.read()
fss = re.findall("(.*?) (.*?)\n", s)
no = dict(fss)
files = os.listdir(to)
for f in tqdm(files):
    f_list = os.listdir(to + f)
    if len(f_list) > 1 or os.path.getsize(to + f + '/' + f + '.json') == 0:
        continue
    print(f)
    fc = open(to + f + '/' + f + '.json', 'r', encoding='UTF-8')
    c = fc.read()
    cc = c.replace('}{', '}<SPLIT>{')
    split_data = cc.split('<SPLIT>')
    parsed_data = [json.loads(bit_data) for bit_data in split_data]
    for i in range(len(parsed_data)):
        file_path = parsed_data[i]["leftSideLocations"][0]["filePath"]
        splits = file_path.split('/')
        subprocess.Popen(
            "git show " + f + "^^:" + file_path + " > " + to + f + '/' + splits[-1],
            cwd=os.path.dirname(dir + no[f] + '/'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

