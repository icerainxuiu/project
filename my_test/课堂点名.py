#import random as rd
from datetime import datetime as time
import secrets as se
import copy


if __name__ == '__main__':

    名单 = '_2018级_名单.txt'#注意名单文件中要把最后一行留一个空白回车
    提问顺序 = '提问log.txt'



    题数 = int(input('要提问多少道题?'))
    人数 = 0
    with open(名单,'r',encoding='UTF-8') as f:
        人数 = len(f.readlines())
    print('*'*5,'读取人数:' ,人数, '*'*5)

    已经提问过的人 = []
    没有提问过的人 = []
    提问日志 = []

    for i in range(1,人数+1):
        没有提问过的人.append(i)

    for i in range(题数):
        if len(没有提问过的人) == 0:
            没有提问过的人 = sorted(copy.deepcopy(已经提问过的人))
            已经提问过的人.clear()
            #num=rd.randint(0,len(没有提问过的人)-1)
            num=se.randbelow(len(没有提问过的人))
            人 = 没有提问过的人.pop(num)
            已经提问过的人.append(人)
            提问日志.append(人)
        elif len(没有提问过的人)>0:
            #num = rd.randint(0,len(没有提问过的人)-1)
            num=se.randbelow(len(没有提问过的人))
            人 = 没有提问过的人.pop(num)
            已经提问过的人.append(人)
            提问日志.append(人)



    name_list = []
    with open(名单,'r',encoding='UTF-8') as f:
        name_list = f.readlines()
        #print('*'*5, len(name_list), '*'*5)

    #print(name_list)
    stu_info_dict=dict()
    for stu_name in name_list:
        stu_info=stu_name.split('\t')
        key=int(stu_info[0])
        stu_info_dict[key]=stu_info


    题号 = 1
    for i in 提问日志:
        stu_name = str(stu_info_dict[i][2][:-1])
        log = stu_name
        print(log)
        grade=input('得分(A-F):')
        题号 += 1
        with open(提问顺序,'a',encoding='UTF-8') as f:
            f.write(log+'\t'+grade.upper()+'\t'+str(time.now())+'\n')
