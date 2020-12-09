import pytest
from pythoncode.calculator import Calculator
class TestCalc:
    def setup_class(self):
        self.calc = Calculator()
        print("开始计算")

    def teardown_class(self):
        print("结束计算")

    def setup_method(self):
        self.calc = Calculator()
        print("setup_method:用例开始执行计算")

    def teardown_method(self):
        print("teardewn_method:用例结束计算")

    @pytest.mark.parametrize("a,b,expect",[
        (3,5,8),(-1,-2,-3),(100,300,400)
    ],ids=["int","minus","bigint"])
    def test_add(self,a,b,expect):
        assert  expect == self.calc.add(a,b)

    @pytest.mark.parametrize("a,b,expect",[
        (5,3,2),(-1,-2,1),(200,100,100)
    ],ids=["int-sub","minus-sub","bigint-sub"])
    def test_sub(self,a,b,expect):
        print("a=%,b=%",a,b)
        assert  expect == self.calc.sub(a,b)

    @pytest.mark.parametrize("a,b,expect", [
        (5, 3, 15), (-1, -2, 2), (200, 100, 20000)
    ], ids=["int-mul", "minus-mul", "bigint-mul"])
    def test_mul(self, a, b, expect):
        print("a=%,b=%", a, b)
        assert expect == self.calc.mul(a, b)

    @pytest.mark.parametrize("a,b,expect", [
        (15, 3, 5), (2, -1, -2), (20000, 100, 200)
    ], ids=["int", "minus", "bigint"])
    def test_div(self, a, b, expect):
        print("a=%,b=%", a, b)
        assert expect == self.calc.div(a, b)