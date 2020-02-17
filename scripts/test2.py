"""pytest初始化和结束方法"""

# 3、模块级别setup_module
#   1 只能作⽤于测试类外部
#   2 只会在整个⽂件中最开始运⾏⼀次
def setup_module():
    print('\n ---模块级别setup_module')


# 4、功能级别setup_function，仅限于类外面的测试方法
def setup_function():
    print('\n ---功能级别setup_function')


class Test:
    # 1、类级别setup_class和teardown_class
    def setup_class(self):
        print('\n ---类级别setup_class')

    def teardown_class(self):
        print('\n ---类级别teardown_class')

    # 2、方法级别setup 和 teardown
    def setup(self):
        print('\n ---方法级别setup')

    def teardown(self):
        print('\n ---方法级别teardown')

    def test_001(self):
        print('测试方法test_001')
        assert True

    def test_002(self):
        print('测试方法test_002')
        assert True


def test_001():
    print('测试类外的测试方法test_001')
    assert True


def test_002():
    print('测试类外的测试方法test_002')
    assert True
