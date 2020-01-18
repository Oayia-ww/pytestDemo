from appium import webdriver


def get_driver():
    desired_caps = {'platformName': 'android',
                    'platformVersionName': '5.1',
                    'deviceName': '192.168.192.101:5555',
                    'appPackage': 'com.android.settings',
                    'appActivity': '.Settings',
                    'unicodeKeyboard': True}
    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
