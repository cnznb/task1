import re
import os


def create_Graph(s1, s2, s3):
    dic = dict()
    mx = 2
    mi = 100000000
    for o in s1:
        dic[int(o[0])] = int(o[1])
        print(o)
        mi = min(mi, int(o[1]))
        mx = max(mx, int(o[1]))
    print(mi, mx)
    g = [list() for _ in range(0, mx + 1)]
    mp = [list() for _ in range(0, mx + 1)]
    for row in range(0, mx + 1):
        for _ in range(0, mx + 1):
            mp[row].append(0)
    for edge in s2:
        u = dic[int(edge[0])]
        v = dic[int(edge[1])]
        if u == int(s3[0][1]) or v == int(s3[0][1]) or u == int(s3[1][1]) or v == int(s3[1][1]) or u == v:
            continue
        if mp[u][v] == 0:
            g[u].append(v)
            mp[u][v] = 1
    fi = open('C:/Users/winner/Desktop/edgeList.txt', 'a')
    for i in range(mi, mx):
        if len(g[i]) == 0:
            continue
        for x in g[i]:
            print(i, x, file=fi)
    fi.close()


def solve(st):
    # 正则抽取对应关系：（编号，行号)
    s1 = re.findall("(\d+).*?<SUB>(\d+)", st)
    # 正则抽取边集：（编号，编号）
    s2 = re.findall("\"(\d+)\" -> \"(\d+)\".*\n", st)
    # 字典存编号行号对应关系
    s3 = re.findall("(\d+).*?METHOD.*?<SUB>(\d+)", st)
    if len(s1) == 0 or len(s2) == 0 or len(s3) == 0:
        return
    create_Graph(s1, s2, s3)


def scan(path):
    # 从本地读入文件
    # path = "C:/Users/winner/Desktop/example"
    files = os.listdir(path)
    print(files)
    for f in files:
        fs = open(path + '/' + f)
        s = fs.read()
        ss = re.findall("\"(\d+)\".*?\)>.*?\n", s)
        for x in ss:
            s = s.replace(x, 'w')
        solve(s)
