# -
给助教整理作业上交情况的小工具

for TAs
记录实验作业上交情况
作业格式：姓名+学号+labx
不守规矩的学生总是不按顺序写作业名字:(

目前学生的学号开头都是11,共8位
可以根据自己的情况修改 30: sid_start = fn.index('11')  
                     34: sid.append(fn[sid_start:sid_start+8])

使用命令： python recordLabHW.py HWfolder_path excel_path labname
e.g. python recordLabHW.py lab2 lab成绩.xlsx LabHW2
