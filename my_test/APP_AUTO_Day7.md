### pytest与Allure的结合

1. 添加测试步骤

   在方法上面添加装饰器

   ```python
   @allure.set(title="测试步骤01")
   ```

2. 添加文字描述

   ```python
   # allure.attach("描述","描述的详情","描述的类型")
   allure.attach("输入",text, allure.attach_type.TEXT)
   ```

3. 添加图片描述

   ```python
   allure.attach("截图",self.driver.get_screenshot_as_png(),allure.attach_type.PNG)
   ```

4. 添加严重级别

   ```python
   @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
   ```

   ```python
   BLOCKER 最严重的
   CRITICAL 严重
   NORMAL 普通
   MINOR 不严重
   TRIVIAL 最不严重
   ```

### Monkey

作用：Monkey主要用于Android的压力测试，自动的一个压力测试小工具，主要目的就是为了测试app是否会Crash(崩溃)

monkey本质上是一个在android系统中执行的linux命令，是java写的

想要在android上执行linux命令有几种

- 直接在电脑上敲adb shell monkey
- 直接在电脑上先敲adb shell 再monkey
- 在手机上装一个类似cmd的软件，然后输入monkey

### Monkey

- -p 指定启动app

- -v 日志级别 (level 0 : -v(缺省值) ,level 1:-v -v, level2:-v -v -v )

  ```python
  level 0: 仅提供启动提示，测试完成，和最终结果等少量信息
  level 1: 提供较为详细的日志，包括每个发送到Activity的时间信息
  level 2：最详细的日志，包括了测试中选中/未选中的Activity信息 
  ```

- -s 随机数种子
- -throttle 毫秒(事件间隔时间)

```
--pct-touch <percent>
调整触摸事件的百分比(触摸事件是一个down-up事件，它发生在屏幕上的某单一 位置)。
--pct-motion <percent>
调整动作事件的百分比(动作事件由屏幕上某处的一个down事件、一系列的伪随机事 件和一个up事件组成)。
--pct-pinchzoom <percent>
缩放事件百分比
--pct-trackball <percent>
调整轨迹事件的百分比(轨迹事件由一个或几个随机的移动组成，有时还伴随有点击)。
--pct-rotation <percent>
屏幕旋转事件百分比
--pct-nav <percent>
调整“基本”导航事件的百分比(导航事件由来自方向输入 设备的up/down/left/right组成)。
--pct-majornav <percent>
调整“主要”导航事件的百分比(这些导航事件通常引发图 形界面中的动作，如：回退按键、菜单按键)
--pct-syskeys <percent>
调整“系统”按键事件的百分比(这些按键通常被保留，由 系统使用，如Home、Back、Start Call、End Call及音量控
制键)。
--pct-appswitch <percent>
调整启动Activity的百分比。在随机间隔里，Monkey将执行一个startActivity()调 用，作为最大程度覆盖包中全部
Activity的一种方法。
--pct-flip <percent>
键盘翻转事件百分比
--pct-anyevent <percent>
调整其它类型事件的百分比。它包罗了所有其它类型的事件，如：按键、其它不常用的设备按钮、等等。
```

### Monkey日志分析

1. 通过monkey命令 输出日志
2. 查看日志的最后是不是有 动作的总数 和 一共花费的时间以及monkey finished 
   1. 如果有，则通过
   2. 如果没有
      1. 搜索关键字 “anr” “exception”
      2. 如果初心anr可能是因为卡，并不是因为产品的bug
      3. 如果出现exception 表示有bug，需要再次复现
         1. 再次根据seed值，重新执行命令，并观察模拟器
         2. 如果无法复现，需要根据log进行复现

## 多线程

- 主线程
  - 我们常说的一个程序代码会从谁给你往下执行，默认就是主线程来执行的
- 子线程
  - 人工开启的线程，主线程会等待子线程结束后再结束
- 线程和线程之间会进行资源的抢夺

### 线程的两种创建方式 

- 直接使用threading模块的Tread类，指定要执行的方法，在调用start()
- 使用继承的方式，继承Thread类，重写run方法，创建这个对象后，在调用start()

### 查看当前程序的线程数量

- threading.enumerate()
  - 获取所有的线程，返回的是个列表
  - 如果需要个数，使用len(threading.enumerate())

### 为子线程传递参数

target方式

```python
t1 = threading.Thread(target=sing,args=(3,))
```

类继承方式

```python
# 重写父类的__init__方法
class work(threading.Thread):
    def __init__(self, nums):
        super().__init__()
        self.nums = nums
    def run(self):
        for i in range(self.nums):
            print("i love u")
            
    
```

