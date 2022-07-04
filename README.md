# task1

Step 1.1：用py脚本把数据集里所有以_old结尾的txt文件转换为_old.java文件，从而满足joern工具的解析格式。并为每一个_old文件生成一个文件夹，附加一个del_line.txt文件(因为后续还要用它做codeBERT并获取其中的行号信息)

Step 1.2：写一个脚本，将Step 1.1整理好的数据集进行过滤，过滤掉的数据特征有：命名不规范(存在’$’、’_’等)、del_line.txt文件为空、_old.java文件为空等。

Step 2：写一个脚本，可以利用joern工具，为每一个数据生成相应pdg的dot文件，在ubuntu上跑(很慢，过滤后的14w数据预计要跑10天左右)，之后过滤掉dot文件大小为0的数据。

Step 3：写一个脚本，利用Step 2中的dot文件，为每一个数据生成edgelist行边集放到一个txt文件里
，让它满足graph emb..的输入。之后过滤掉行边集为空的数据

