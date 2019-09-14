import sys
runCounter=0

maxredepth=9999
#此数字是平台有关的.默认递归深度是1000(1000-4=996),
# 当前环境可测出为:3220-3225之间
sys.setrecursionlimit(maxredepth)

def fact(n):
    global runCounter
    runCounter += 1
    print(runCounter)

#---------------栈消费区-----------
#随便写点什么东西改变一下函数的大小，建议往这里塞点垃圾指令
    if (1==2):
        print("WTF????")
    elif(1==1):
        if(2==2):
            if (10%2==0):
                print("duang!")
                pass
#---------------栈消费区-----------

    if n == 1:
        return 1
    else:
        return fact(n-1)*n



if __name__=='__main__':
    s=0
    try:
        #s=fact(1000)#默认
        s = fact(maxredepth-4) # -4/-3调参
    except Exception as e:
        print(e)
    finally:
        print('阶乘结果--->',s,'\n递归深度--->',runCounter)

