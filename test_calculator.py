# Calculator App Tests
# By Alex Graalum
import calculator


class Test_CalculatorApp:
    def test_add(self):
        assert 5 == calculator.add(2, 3)
        
    def test_subtract(self):
        assert 5 == calculator.subtract(10, 5)

