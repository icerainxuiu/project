## Yaml数据

应用场景

概念和语法规则

Yaml是一种所有编程语言可用的友好的数据序列化标准，语法和其他高阶语言类似，并且可用简单表达字典，列表和其他基本数据类型的形态，语法规则如下：

1. 大小写敏感
2. 使用缩进表示层级关系
3. 缩进时不允许使用Tab键，只允许使用空格
4. 缩进的空格数目不重要，只要相同层级的元素左对齐即可

demo.py

```python
import yaml
with open("./data.yaml", 'r') as f:
    data = yaml.load(f)
    print(data)
```

data.yaml

```yaml
name: "xiaoming"
age: "18"
```

- yaml数据格式文件后缀：yaml或yml

```yaml
# 规律：
# 是一个字典还是一个列表
# 	如果是字典，直接写key， 冒号空格
# 	如果是列表，直接写 "-"， 空格
# 如字典对应的value，
#   如果是字典或列表，加回车缩进，回到第一个问题
#   如果不是字典或列表，直接写
# 列表中的元素，如果不是字典或列表，直接写
# {"name":"xiaoming", "age":"18"}
name: "xiaoming"
age: "18"
# ["1","2","3"]
- "1"
- "2"
- "3"
```

### yaml注意点

- 在pycharm中，如果使用tab键做缩进，它自动转换，如果是复制的tab键，不会进行转化
- 在同级别内容左对齐，多少个空格无所谓

### yaml其他基本数据类型

- 整数
  - 直接写数字，不要小数点
- 浮点数
  - 直接写数字，要小数点
- 布尔
  - True
  - TRUE
  - true
  - False
  - FALSE
  - false
- 空值
  - NULL
  - null
  - Null
- 时间
  - 年-月-日 时：分：秒.毫秒
- 字符串
  - "字符串"
  - '字符串'

### 将xml转成html

#### 安装

```
http://bintray.com/qameta/generic/allure2 下载allure-2.6.0.zip
解压缩到一个目录(不经常用的目录)
将压缩包内的bin目录配置到path系统环境变量
在命令行汇中敲allure命令，如果提示有这个命令，即为成功
```

#### 使用步骤

在保证项目中的report目录下有xml文件的时候，执行以下步骤

1. 进入report上级目录执行命令

   ```
   allure generate report/ -o report/html --clean
   ```

2. report 目录下会生成html文件夹，html下会有一个index.html, 右键浏览器打开即可

### 参数和命令详解

应用场景

修改xml所在的目录名称和index.html所在的目录名称

疑问和解答

1. ` addopts = -s --alluredir report ` 中的 ` --alluredir report ` 是什么意思
   - --alluredir 后面的report 为xml输出的目录名
   - 如果希望目录名叫result 那么可以将命令行参数改为 ` --alluredir result`
2. ` allure generate report/ -o report/html --clean` 是什么意思
   - report/ 表示xml所在的目录
   - -o 表示output 输出
   - report/html 表示将index.html 报告生成到哪个文件夹

### allure与pytest结合

#### 添加测试步骤

应用场景

一套登录流程需要至少三个步骤，输入用户名，输入密码，点击登录，我们可以通过添加测试步骤，让这些步骤在报告中进行提现

使用方式

在page中的所有方法上加上` @allure.step(title="测试步骤001"))` 装饰器即可

