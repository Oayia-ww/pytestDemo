"""工厂函数和初始化函数比较"""
import pytest


class Test:

    def setup(self):  # 工厂函数优先级高于setup
        print("\n函数初始化方法setup")

    def setup_class(self):  # 工厂函数优先级低于setup_class
        print("\n----类初始化方法setup_class")

    @pytest.mark.usefixtures("inx")
    def test_001(self):
        print("\n---测试方法")
        assert True

    @pytest.fixture(name="inx")
    def before(self):
        print("\n-----工厂方法before")
