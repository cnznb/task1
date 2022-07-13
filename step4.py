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
    ffs = os.listdir(path)
    sss = list()
    for x in ffs:
        if x.endswith('methods.txt'):
            fs = open(path + '/' + x, 'r', encoding='UTF-8')
            ss = fs.read()
            sss = re.findall(".* (\d+) (\d+)\n", ss)
            fs.close()
            break
    mine = list()
    for x in ffs:
        if x.endswith('_del_lines.txt'):
            fs = open(path + '/' + x, 'r', encoding='UTF-8')
            xq = fs.read()
            # del_line
            xqq = re.findall("(\d+) .*?\n", xq)
            fs.close()
            for xx in xqq:
                z = int(xx)
                for oo in sss:
                    if int(oo[0]) <= z <= int(oo[1]):
                        if len(mine) == 0:
                            mine.append(oo)
                        elif mine[-1] != oo:
                            mine.append(oo)
                        break
    files = os.listdir(path + '/edge')
    for f in files:
        fxs = open(path + '/edge/' + f, 'r', encoding='UTF-8')
        xs = fxs.read()
        xss = re.findall('(\d+) (\d+)\n', xs)
        fxs.close()
        q = 0
        for inn in xss:
            if q == 1:
                break
            x = int(inn[0])
            y = int(inn[1])
            for xqq in mine:
                if int(xqq[0]) <= x <= int(xqq[1]) or int(xqq[0]) <= y <= int(xqq[1]):
                    q = 1
                    break
        if q == 0:
            os.remove(path+'/edge/'+f)


source_dir = 'E:/sets'
file = os.listdir(source_dir)
for ff in tqdm(file):
    # 建立行边集
    scan(source_dir + '/' + ff)



