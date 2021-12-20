import os,sys,random

#项目根路径确定
GLOBAL_PROJECT_ROOT = os.path.abspath(os.path.pardir)
#将项目跟路径加入包路径
sys.path.append(GLOBAL_PROJECT_ROOT)

ss = [0,1,2,3,4,5,6,7,8,9]

print(ss[-3:])
print(ss[0:7])