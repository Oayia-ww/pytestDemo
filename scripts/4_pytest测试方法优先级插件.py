import pytest


# ★pytest失败重试插件不建议和setup_class方法使用，如果一定要使用，要么测试方法之间没有前后依赖关系 pip install pytest-rerunsfailures
# pytest测试方法优先级插件：pip install pytest-ordering，使用方式：注解的形式
# pytest测试报告插件：pip install pytest-html(可生成xml/html报告)

class TestFile:

    def setup_class(self):
        print("\n声明手机驱动对象")

    # 全为整数或负数时越小优先级越高，有正有负时，正数优先级高于负数
    # 负数优先级低于未标记的测试方法，正数优先级高于未被标记的测试方法
    # 0最高
    # @pytest.mark.run(order=2)
    def test_001(self):
        print('\n登录')
        assert True

    # @pytest.mark.run(order=1)
    def test_002(self):
        print('\n查询订单')
        assert False
