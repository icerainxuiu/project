## 高级手势TouchAction

1. 轻敲操作

   ```python
   TouchAction(driver).tap(element=None,x=None,y=None).perform()
   ```

2. 按下和抬起

   ```python
   TouchAction(driver).press(element=None,x=None,y=None).perform()
   TouchAction(driver).release().perform()
   ```

3. 等待操作

   ```python
   TouchAction(driver).wait(ms=0).perform()
   ```

4. 长按操作

   ```python
   TouchAction(driver).long_press(element=None,x=None,y=None,duration=1000).perform()
   ```

5. 移动操作

   ```python
   TouchAction(driver).move_to(element=None,x=None,y=None).perform()
   ```

## 手机操作API

1. 获取手机分辨率

   ```python
   driver.get_window_size()
   ```

2. 手机截图

   ```python
   driver.get_screenshot_as_file(os.getcwd() + os.sep + './screen.png')
   ```

3. 获取和设置手机网络

   ```
   driver.network_connection
   driver.set_network_connection(connectionType)
   ```

4. 发送键到设备

   ```
   driver.press_keycode(keycode, metastate=None)
   # keycode:发送给设备的关键代码
   # metastate:关于被发送的关键代码的元信息，一般为默认值
   ```

5. 操作手机通知栏

   ```
   driver.open_notifications()
   driver.press_keycode(4)
   ```

## pytest运行方式

- 主函数

  - 导入pytest模块
  - 使用pytest模块中的main方法

- 命令行[推荐]

  - 进入到项目目录下
  - 输入命令 pytest -s xxx.py

- setup

  ```python
  def setup(self):
  	pass
  def setup_class(self):
      pass
  ```

- teardown

  ```python
  def teardown(self):
  	pass
  def teardown_class(self):
      pass
  ```

  ```
  优先执行setup_class -->setup --> teardown-->teardown_class
  ```

## 配置文件

- 配置文件能够根据配置的选项，让pytest框架执行一部分测试脚本
- 文件名：pytest.ini
- 第一行内容：[pytest]
- 命令行参数：
  - addopts
  - 将命令参数的内容，拼接到pytest命令之后，一起当做一个命令执行
- 定位要执行的测试脚本
  - testpaths/pyton_files/python_classes/python_functions
  - 表示要执行哪一个文件夹下的哪一个文件，哪一个类， 哪一个函数

```ini
[pytest]
addopts = -s --html=report/report.html --reruns 0
testpaths = ./scripts
python_files = test_*.py
python_classes = Test*
python_functions = test_*
```

