
.项目背景
    口语项目频繁回归测试，耽误大量人力成本回归测试，针对主功能进行自动化回归，达到替代部分人力回归成本，节约时间，做到提质增效的作用。
.安装步骤
    本地的环境是Windows 10版本 64位系统（32位的同学自己想办法哦）
    Java：1.8.0_181 （64位）
    Python：3.7 （推荐）                     https://www.python.org/
    nodejs：16.13                            https://nodejs.org/en/
    Appium：1.7.1 （nodejs和Appium需要对应） https://bitbucket.org/appium/appium.app/downloads/
    PyCharm: 5.0.6                           https://download.jetbrains.com/python/pycharm-community-2017.3.2.exe
    android-sdk: android-sdk_r24.3.4-windows http://tools.android-studio.org/index.php/sdk/
.目录结构描述
    kyxl
        Page                公共方法定义，手机参数，系统，程序包，package等
        TestCase            存放测试case
        report              存放项目的测试最终结果报告
        screenShot          截图功能，在实际的自动化项目运行过程中，App可能会出现很多异常，为了更好的定位到问题，除了捕捉日志，我们还需要对运行的设备状态进行截图。
        app                 存放待测试的apk
        config              需要参数化的字段，邮箱，机器配置，可以代码和参数分离
        README.md           自动化项目介绍
        Test_Flow_xx.py     测试流 运行自动化程序的入口

.使用
    实现功能：
        登录，题型，答题，成绩报告。
.框架具备能力：            Python3 + Appium + unittest + 真机
    1、测试流  能以流程化形式跑case，也可单独针对一个功能模块跑，Test_Flow_xx.py\case_a_login.py\
    方便调试，维护，可依据测试人员的想法随意定制测试流。
    2、以当前系统运行时间命名测试报告
    3、查找最近测试结果报告
    4、截图功能封装
    5、手机滑动功能封装
    6、公共参数提取
    7、发送邮件给相关人员
    8、可移植，多平台适用、 web\移动端
.相关项目（可选）
    web端UI自动化;web接口自动化;
.主要项目负责人
    丁亚      https://github.com/cfanding
.参与贡献方式
    相关英文文档，网站，以及相关blog。


① APPIUM¶
    Appium是一款开源的自动化测试工具，支持IOS、Android、Windows和Mac应用。

跨平台¶
    appium可以在OSX，Windows以及Linux桌面上运行。

跨语言¶
    appium采用了C/S的设计模式，扩展了WebDriver协议，因此Client用Python、Java、Js/Nodejs、Ruby、OC、C#等各种语言来实现。

原理介绍¶
    Appium的核心是一个遵守REST设计风格的Web服务器，他会用来接受客户端的连接和指令。由于统一的接口设计，客户端便可以用多种语言来实现，从而用自己喜欢的语言来实现测试用例。

服务端收到测试指令后会发送给设备，在设备层则使用了设备商提供的原生测试框架，比如IOS的XCUITest Driver和UIAutomation Driver, 安卓的UIAutomator和UIAutomator2等等。

