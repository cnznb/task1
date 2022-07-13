"""
Step 1.2：负责调整/删除数据集的脏数据
"""
import re
import os
import shutil
from tqdm import tqdm

# 规范输出路径
to = "E:/sets"
files = os.listdir(to)
for file in tqdm(files):
    path = to + '/' + file
    in_files = os.listdir(path)
    if len(in_files) < 4:
        print(len(in_files), in_files)
        shutil.rmtree(path)
    elif len(in_files) == 4:
        for f in in_files:
            fs = f.split('.')
            fss = fs[0].split('_')
            if fss[-2] == 'del':
                if os.path.getsize(path + '/' + f) == 0:
                    shutil.rmtree(path)
                    continue
                fs = open(path + '/' + f, 'r', encoding='UTF-8')
                s = fs.read()
                fs.close()
                if re.search("import|package|public|private|protected|void", s):
                    shutil.rmtree(path)
    else:
        print(len(in_files), in_files)
        shutil.rmtree(path)
