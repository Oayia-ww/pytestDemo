"""工厂函数"""
import pytest


@pytest.fixture(name='outx')
def before_out():
    print('\nbefore_out')


@pytest.mark.usefixtures('outx')  # 类引用可以引用类内部和类外部的工厂函数，作用于类中的每一个测试方法
class TestFixture:

    @pytest.fixture(name='inx')  # 工厂函数被调用时是优先运行的，默认方法名作为工厂函数名字，当指定name残烛时，那么函数名不再作为工厂函数的名字
    def before_in(self):
        print('\nbefore_in')

    # 方式一：参数引用
    # def test_query_all(self, outx, inx):  # 工厂函数按参数先后顺序执行
    #     print('\n查询员工')
    #     assert True

    # 方式二：函数引用，类可以使用函数引用方法引用工厂函数，函数引用和类引用同时存在时，最先调用的时函数引用方法
    # @pytest.mark.usefixtures('outx', 'inx')  # 按参数先后顺序执行
    # def test_query(self):
    #     print('查询员工')
    #     assert True

    # 函数引⽤和类引⽤⼯⼚函数同时存在时，函数引⽤优先级⾼于类引⽤优先级
    # ★ 前提是函数引用和类引用采用的都是方式二，若测试方法采用的是方式一参数引用先执行的是类引用而并非函数引用！！！
    @pytest.mark.usefixtures('inx')
    def test_query_all(self):
        print('\n查询员工')
        assert True