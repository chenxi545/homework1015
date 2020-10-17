import pytest
from pythoncode.calculator import Calculator


class TestCalc:
    def setup_class(self):
        print("类里面的测试用例开始执行")
        self.calc = Calculator()

    def teardown_class(self):
        print("类里面的测试用例执行完成")

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("计算结束")

    @pytest.mark.parametrize('a,b,expect', [
        [0, 0, 0],
        [0, 234, 234],
        [234, 0, 234],
        [0, -345, -345],
        [-345, 0, -345],
        [0, 0.23, 0.23],
        [0.23, 0, 0.23],
        [0, -0.23, -0.23],
        [-0.23, 0, -0.23],
        [124, 235, 359],
        [23, -679, -656],
        [-23, 100, 77],
        [234, 123.45, 357.45],
        [123.45, 234, 357.45],
        [23.14, 66.99, 90.13],
        [-23.14, -66.11, -89.25],
        [23.14, -66.11, -42.97],
        [-23.14, 66.11, 42.97],
        [999999999.99, 0.01, 1000000000]
    ], ids=[f"add_case{i}" for i in range(1, 20)])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect

    @pytest.mark.parametrize('a1,b1,expect1', [
        [34, 0, '被除数不能为0'],
        [0, 100, 0],
        [0, -100, 0],
        [0, -12.3, 0],
        [23, 876, 0.03],
        [5, 10, 0.5],
        [125, 5, 25],
        [2343, 25, 93.72],
        [2343, 26, 90.12],
        [12.645, 234.12, 0.05],
        [569.34, 6.854, 83.07],
        [-2343, -25, 93.72],
        [-2343, -26, 90.12],
        [-12.645, -234.12, 0.05],
        [-569.34, -6.854, 83.07],
        [234, 1234.456, 0.19],
        [234.445, 123, 1.91],
        [234, -1234.456, -0.19],
        [-234, 1234.456, -0.19],
        [-234, -1234.456, 0.19],
        [-234.445, 123, -1.91],
        [234.445, -123, -1.91],
        [-234.445, -123, 1.91]
    ], ids=[f"div_case{i}" for i in range(1, 24)])
    def test_div(self, a1, b1, expect1):
        if b1 == 0:
            result = '被除数不能为0'
        else:
            self.result1 = self.calc.div(a1, b1)
            result = round(self.result1, 2)
        assert result == expect1