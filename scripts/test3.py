"""常用断言方式"""
import time

from util import get_driver


class TestSetLocation:

    def setup_class(self):
        # 声明我们的driver对象
        self.driver = get_driver()

    def teardown_class(self):
        """退出driver"""
        self.driver.quit()

    def test_loction(self):
        """测试方法"""
        # 存储
        save = self.driver.find_element_by_xpath("//*[contains(@text,'存储')]")
        # WLAN
        wlan = self.driver.find_element_by_xpath("//*[contains(@text,'WLAN')]")
        # 存储 -> WLAN
        self.driver.drag_and_drop(save, wlan)
        # 点击位置信息
        self.driver.find_element_by_xpath("//*[contains(@text,'位置信息')]").click()
        # 点击模式
        self.driver.find_element_by_xpath("//*[contains(@text,'模式')]").click()
        time.sleep(1)
        # 选择仅限设备
        self.driver.find_element_by_xpath("//*[contains(@text,'GPS确定位置')]").click()
        time.sleep(1)
        # 点击返回按钮
        self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        # 断言结果
        """方式一：捕获断言"""
        # try:
        #     # 找预期结果
        #     self.driver.find_element_by_xpath("//*[contains(@text,'仅限设备')]")
        #     # 找到 断言成功
        #     assert True
        # except:
        #     # 没找到 断言失败
        #     assert False
        """方式二：列表断言"""
        # 获取所有文本信息
        results = self.driver.find_elements_by_id("android:id/summary")
        # 断言 仅限设备 在结果列表中
        assert "仅限设备" in [i.text for i in results]
