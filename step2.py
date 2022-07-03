"""
Step 2：通过共享文件夹，用该脚本在虚拟机上跑数据集，利用joern工具生成数据集的dot文件
"""
import subprocess
from tqdm import tqdm
import os
JOERNPATH = '/opt/joern/joern-cli/'


def code_to_dot(file_path, out_dir_pdg):
    # parse source code into cpg
    print('parsing source code into pdg...')
    shell_str = "sh " + JOERNPATH + "./joern-parse " + file_path
    subprocess.call(shell_str, shell=True)
    print('exporting pdg from pdg root...')
    # 导出pdg的dot文件到指定的文件夹中
    shell_export_pdg = "sh " + JOERNPATH + "./joern-export " + "--repr pdg --out " + out_dir_pdg
    subprocess.call(shell_export_pdg, shell=True)


source_dir = '/mnt/hgfs/DataSet'
dirs = os.listdir(source_dir)
for files in tqdm(dirs):
    print(files)
    in_file = os.listdir(source_dir+'/'+files)
    for f in in_file:
        if f.split('.')[-1] == 'java':
            code_to_dot(source_dir+'/'+files+'/'+f, source_dir+'/'+files+'/dot')