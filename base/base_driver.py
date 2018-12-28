from appium import webdriver


def init_driver(apppackage,appactivity):
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android' #平台名称
    desired_caps['platformVersion'] = '5.1'  #平台版本
    desired_caps['deviceName'] = '192.168.56.101:5555' #设备号
    # app信息
    desired_caps['appPackage'] = apppackage #应用的包名
    desired_caps['appActivity'] = appactivity #代表启动的activity
    desired_caps['automationName'] = "Uiautomator2"

    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True

    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #声明driver对象