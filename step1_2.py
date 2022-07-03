"""
Step 1.2：负责调整/删除数据集的脏数据
"""
import os
import shutil
from tqdm import tqdm
# 规范输出路径
to = "F:/DataSet"
i = 0
files = os.listdir(to)
for file in tqdm(files):
    path = to + '/' + file
    in_files = os.listdir(path)
    if len(in_files) < 2:
        print(len(in_files), in_files)
        shutil.rmtree(path)
    elif len(in_files) == 2:
        continue
    else:
        for f in in_files:
            fs = f.split('.')
            fss = fs[0].split('_')
            dir_name = ''
            for n in fss:
                if n == 'del' or n == 'old':
                    break
                dir_name = dir_name + n
            if not os.path.exists(to + '/' + dir_name):
                os.makedirs(to + '/' + dir_name)
            if len(os.listdir(to + '/' + dir_name)) < 2:
                shutil.move(path+'/'+f, to + '/' + dir_name + '/')


