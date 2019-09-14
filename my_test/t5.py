import os
path = input('请输入文件路径(结尾加上/)：')       

#获取该目录下所有文件，存入列表中
file_list = os.listdir(path)


for i in range(len(file_list)):
    
    #设置旧文件名（就是路径+文件名）
    oldname = path + os.sep + file_list[i] # os.sep添加系统分隔符
    
    #设置新文件名
    newname = path + os.sep +'a'+ str(i+1)+'.JPG'
    
    os.rename(oldname,newname)   #用os模块中的rename方法对文件改名
    print(oldname,'======>',newname)
    

