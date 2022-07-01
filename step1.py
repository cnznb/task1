import os
import shutil
# 数据集本地路径
path = "C:/Users/winner/Desktop/dicc"
# 规范输出路径
to = "F:/DataSet"


def work(file_path):
    files = os.listdir(file_path)
    for f in files:
        fs = f.split('.')
        print(fs)
        fss = fs[0].split('_')
        print(fss)
        if not os.path.exists(to + '/' + fss[0]):
            os.makedirs(to + '/' + fss[0])
        if fss[-1] == 'old':
            shutil.copyfile(file_path + '/' + f, to + '/' + fss[0] + '/' + fs[0] + '.java')
        elif fss[-2] == 'del':
            shutil.copyfile(file_path + '/' + f, to + '/' + fss[0] + '/' + f)


def rename():
    files = os.listdir(path)
    for file in files:
        new_files = os.listdir(path+'/'+file)
        for f in new_files:
            work(path+'/'+file+'/'+f)


rename()
