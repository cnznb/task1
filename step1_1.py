"""
Step 1.1:
    生成规范化数据集
    保留xxx_old.java和xxx_del_line.txt
"""
import os
import shutil
from tqdm import tqdm
# 数据集本地路径
path = "E:/dataset"
# 规范输出路径
to = "F:/DataSet"


def work(file_path):
    files = os.listdir(file_path)
    for f in files:
        fs = f.split('.')
        fss = fs[0].split('_')
        if len(fs) != 2 or len(fss) < 2:
            continue
        if not os.path.exists(to + '/' + fss[0]):
            os.makedirs(to + '/' + fss[0])
        if fss[-1] == 'old':
            shutil.copyfile(file_path + '/' + f, to + '/' + fss[0] + '/' + fs[0] + '.java')
        elif fss[-2] == 'del':
            shutil.copyfile(file_path + '/' + f, to + '/' + fss[0] + '/' + f)
        # 行号是否需要单独提取放置一个文件中？


def normalized_dataset():
    files = os.listdir(path)
    for file in tqdm(files):
        new_files = os.listdir(path+'/'+file)
        for fs in tqdm(new_files):
            end_files = os.listdir(path+'/'+file+'/'+fs)
            for f in end_files:
                work(path+'/'+file+'/'+fs+'/'+f)


# 生成规范数据集
normalized_dataset()
