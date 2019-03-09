'''
for TAs
记录实验作业上交情况
作业格式：姓名+学号+labx
不守规矩的学生总是不按顺序写作业名字:(
目前学生的学号开头都是11
可以根据自己的情况修改
by: lisiyuan 2019.03.09
'''

import os
import sys
import pandas as pd

def is_Chinese(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
        return True
    else:
        return False
    
def extractNames(folder_dir = sys.argv[0], labName = 'lab'):
    file_names = os.listdir(folder_dir)
    name = []
    sid = []
    is_handin = []
    for i in range(len(file_names)):
        fn = file_names[i]
        try:
            sid_start = fn.index('11')
        except:
            print(fn)        
        name.append(''.join([c for c in fn if is_Chinese(c)]))
        sid.append(fn[sid_start:sid_start+8])
        is_handin.append(1)
    hws = {'names': name, 'SID': sid, labName: is_handin}
    return hws

def recordGrades(hw_new, grade_file, labName):
    # hw_new is pd.DataFrame
    # grade_file is path
    if not os.path.exists(grade_file):
        # 第一次使用，file不存在
        hw_new.to_excel(grade_file)
        return hw_new
    else:        
        hw_old = pd.read_excel(grade_file)
        if hw_new.shape[0]>hw_old.shape[0]:
            print('WARNING：有新同学加入！')
            #TO DO
        newScore = [0 for i in range(len(hw_old))]
        for i in range(len(hw_old)):
            newScore[i] = hw_new.loc[hw_new.names==hw_old.names[i],labName].values[0]
        hw_old[labName] = newScore
        hw_old.to_excel(grade_file)
        return hw_old


if __name__ == '__main__':
    # python recordLabHW.py HWfolder_path excel_path labname
    # python recordLabHW.py lab2 lab成绩.xlsx LabHW1
    folder = sys.argv[1]
    excel_path = sys.argv[2]
    labName = sys.argv[3]
    hws = extractNames(folder,labName)
    hw_new = pd.DataFrame(hws)
    recordGrades(hw_new, excel_path,labName)

    