import pytest


def test_001():
    print('\ntest_001')
    assert True  # 断言方式：assert 条件表达式，条件表达式结果true或false


def test_002():
    print('\ntest_002')
    assert False


# pytest是对unittest测试框架的一个封装，添加了很多新的功能
# 方式一：主函数运行方式，仅限于debug代码调试使用；
# 方式二：pytest命令行运行方式，命令行进入到项目根目录：pytest 路径 + 文件名
#        默认不输出打印内容，需添加-s参数才能输出打印内容
#        pytest可以不指定文件名字，默认搜索：
#               当前路径下所有以test_开头的文件
#               搜索文件中以Test开头的类
#               搜索类中以test开头的方法
# ★ 命令行运行方式是项目唯一方式，方便持续集成和项目管理
if __name__ == '__main__':
    pytest.main(['1_pytest的两种运行方式.py'])
