import pytest
import yaml
import allure
from pythoncode.calculator import Calculator


def get_datas():
    with open(r'C:\Users\Administrator\PycharmProjects\pythonProject\data\data.yml', encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        add_datas = datas['add']['datas']
        div_datas = datas['div']['datas']
        sub_datas = datas['sub']['datas']
        mul_datas = datas['mul']['datas']
    return [add_datas, div_datas, sub_datas, mul_datas]

class TestCalc:

    # def setup_class(self):
    #     print("类里面的测试用例开始执行")
    #     self.calc = Calculator()
    #
    # def teardown_class(self):
    #     print("类里面的测试用例执行完成")

    # def setup(self):
    #     print("setup开始计算")
    #
    # def teardown(self):
    #     print("teardown计算结束")
    calc = Calculator()
    @allure.feature('加法')
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a,b,expect', get_datas()[0], ids=[f"add_case{i}" for i in range(1, 20)])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect

    @allure.feature('除法')
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('a1,b1,expect1', get_datas()[1], ids=[f"div_case{i}" for i in range(1, 24)])
    def test_div(self, a1, b1, expect1):
        if b1 == 0:
            result = '被除数不能为0'
        else:
            self.result1 = self.calc.div(a1, b1)
            result = round(self.result1, 2)
        assert result == expect1

    @allure.feature('减法')
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a,b,expect', get_datas()[2], ids=[f"sub_case{i}" for i in range(1, 5)])
    def test_sub(self, a, b, expect):
        result = self.calc.sub(a, b)
        assert result == expect

    @allure.feature('乘法')
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('a,b,expect', get_datas()[3], ids=[f"mul_case{i}" for i in range(1, 6)])
    def test_mul(self, a, b, expect):
        result = self.calc.mul(a, b)
        assert result == expect
