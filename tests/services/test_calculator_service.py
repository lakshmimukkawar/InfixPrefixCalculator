import pytest
from prefix_infix_calculator.services.calculator_service import Infix, Prefix


class TestIsOperator:
	@pytest.mark.unittest
	def test_is_operator_is_correct(self):
		assert Infix.is_operator("*") == True
		assert Infix.is_operator("-") == True
		assert Infix.is_operator("+") == True
		assert Infix.is_operator("/") == True

	@pytest.mark.unittest
	def test_is_operator(self):
		assert Infix.is_operator("7") == False


class TestApplyMathOperations:
	@pytest.mark.unittest
	def test_apply_math_operations(self):
		operand1 = 5
		operand2 = 5
		operator = ["*", "+", "-", "/"]
		assert Infix.apply_math_operations(operand1, operand2, operator[0]) == 25
		assert Infix.apply_math_operations(operand1, operand2, operator[1]) == 10
		assert Infix.apply_math_operations(operand1, operand2, operator[2]) == 0
		assert Infix.apply_math_operations(operand1, operand2, operator[3]) == 1


class TestInfixCalculation:
	@pytest.mark.unittest
	def test_calculate_infix_expression(self, get_infix_expressions_list):
		list_of_inputs = get_infix_expressions_list
		assert Infix.calculate_infix_expression(list_of_inputs[0]) == float(3)
		assert Infix.calculate_infix_expression(list_of_inputs[1]) == float(7)
		assert Infix.calculate_infix_expression(list_of_inputs[2]) == float(5)
		assert Infix.calculate_infix_expression(list_of_inputs[3]) == float(-1.8)


class TestPrefixCalculation:
	@pytest.mark.unittest
	def test_calculate_prefix_expression(self, get_prefix_expressions_list):
		list_of_inputs = get_prefix_expressions_list
		assert Prefix.calculate_prefix_expression(list_of_inputs[0]) == float(3)
		assert Prefix.calculate_prefix_expression(list_of_inputs[1]) == float(7)
		assert Prefix.calculate_prefix_expression(list_of_inputs[2]) == float(5)
		assert Prefix.calculate_prefix_expression(list_of_inputs[3]) == float(3)
		assert Prefix.calculate_prefix_expression(list_of_inputs[4]) == float(-3)
		assert Prefix.calculate_prefix_expression(list_of_inputs[5]) == float(1)
