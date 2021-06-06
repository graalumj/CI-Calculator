# Calculator App Tests
# By Alex Graalum
import calculator


class Test_CalculatorApp:
    def test_add(self):
        assert 5 == calculator.add(2, 3)

    def test_subtract(self):
        assert 5 == calculator.subtract(10, 5)

    def test_multiply(self):
        assert 15 == calculator.multiply(3, 5)

    def test_divide(self):
        assert 3 == calculator.divide(15, 5)
