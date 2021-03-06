"""
Step 3：利用dot文件生成行边集
"""
import re
import os
import shutil
from tqdm import tqdm


def create_Graph(s1, s2, s3, path, idx):
    dic = dict()
    mx = 2
    mi = 100000000
    for o in s1:
        dic[int(o[0])] = int(o[1])
        mi = min(mi, int(o[1]))
        mx = max(mx, int(o[1]))
    g = [list() for _ in range(0, mx + 1)]
    mp = [list() for _ in range(0, mx + 1)]
    for row in range(0, mx + 1):
        for _ in range(0, mx + 1):
            mp[row].append(0)
    for edge in s2:
        u = dic[int(edge[0])]
        v = dic[int(edge[1])]
        if u == v:
            continue
        flag = 0
        for x in s3:
            if x[1] == u or x[1] == v:
                flag = 1
                break
        if flag:
            continue
        if mp[u][v] == 0:
            g[u].append(v)
            mp[u][v] = 1
    fi = open(path + '/edge/edgelist'+str(idx)+'.txt', 'a')
    for i in range(mi, mx):
        if len(g[i]) == 0:
            continue
        for x in g[i]:
            print(i, x, file=fi)
    fi.close()


def work(st, path, idx):
    # 正则抽取对应关系：（编号，行号)
    s1 = re.findall("(\d+).*?<SUB>(\d+)", st)
    if len(s1) == 0:
        return
    # 正则抽取边集：（编号，编号）
    s2 = re.findall("\"(\d+)\" -> \"(\d+)\".*\n", st)
    if len(s2) == 0:
        return
    # 找到函数出口行号
    s3 = re.findall("(\d+).*?\(METHOD.*?<SUB>(\d+)", st)
    if len(s3) == 0 or len(s3) > 2:
        return
    # print(s3)
    # 字典存编号行号对应关系
    create_Graph(s1, s2, s3, path, idx)


def scan(path):
    # 从本地读入文件
    files = os.listdir(path+'/dot')
    i = 0
    for f in files:
        fs = open(path + '/dot/' + f, 'r', encoding='UTF-8')
        s = fs.read()
        # 抽取并修改不合法行
        ss = re.findall("\"(\d+)\".*?\)>.*?\n", s)
        for x in ss:
            s = s.replace('\"'+x+'\"', 'w')
        # print(f)
        work(s, path, i)
        i = i + 1


def delete_empty_dot(path):
    if not os.path.exists(path+'/dot'):
        shutil.rmtree(path)
        return
    if len(os.listdir(path+'/dot')) == 0:
        shutil.rmtree(path)


source_dir = 'E:/sets'
file = os.listdir(source_dir)
for ff in tqdm(file):
    # 删除dot文件为空的或者不存在dot文件的脏数据
    # delete_empty_dot(source_dir+'/'+ff)
    # print(source_dir + '/' + ff)
    # 建立行边集
    if not os.path.exists(source_dir + '/' + ff + '/edge'):
        os.mkdir(source_dir + '/' + ff + '/edge')
        scan(source_dir + '/' + ff)
        if not os.path.exists(source_dir + '/' + ff + '/edge'):
            shutil.rmtree(source_dir + '/' + ff)



