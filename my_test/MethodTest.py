from types import FunctionType
import requests
class MethodTest:
    def makeDynamicMethod(self):
        methodList=['createInstance','getNetTypeById']
        urlList=['www.baidu.com','www.qq.com']
        methodObj = MethodTest()
        for i in range(0,len(methodList)):
            testmethod=methodList[i]
            url = urlList[i]
            method_str = u'''def test_%s(self):                       
                        url="%s"
                        print('url',url)           
                        res = requests.get(url=url ,verify=False)    
                        print('动态创建函数返回结果=',res.text)
                        return res
                      ''' % (testmethod, url)
            func_code = compile(method_str, "", "exec")
            methodName = "test_%s" % testmethod
            func = FunctionType(func_code.co_consts[0], globals(), methodName)
            print (MethodTest.func)
            print (methodObj.func)
if __name__ =='__main__':
    method = MethodTest()
    method.makeDynamicMethod()