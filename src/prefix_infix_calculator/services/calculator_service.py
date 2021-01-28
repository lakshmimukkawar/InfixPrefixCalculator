from prefix_infix_calculator.services.utils import get_logger
logger = get_logger(__name__)


class Infix:
	@classmethod
	def calculate_infix_expression(cls, expression):
		"""
		This function evaluates the infix expression using the stack approach.
		We can also use recursive functions to calculate this.
		Parameters
		----------
		expression: string: expression string

		Returns: float: evaluated answer
		-------

		"""
		logger.info(f"in the calculate infix expression {expression}")
		elements = expression.split()
		stack = []
		try:
			for e in elements:
				if not e.isdigit() and e != ")":
					stack.append(e)
				if e.isdigit() and not cls.is_operator(stack[-1]):
					stack.append(e)
				if e.isdigit() and cls.is_operator(stack[-1]):
					operator = stack.pop()
					operand1 = stack.pop()
					result = cls.apply_math_operations(float(operand1), float(e), operator)
					if stack[-1] == "(":
						stack.append(str(result))
					else:
						raise Exception("invalid input")
						break
				if e == ")":
					value = stack.pop()
					ob = stack.pop()
					if (ob == "("):
						stack.append(str(value))
					elif (cls.is_operator(ob)):
						operand1 = stack.pop()
						stack.pop()
						result = cls.apply_math_operations(float(operand1), float(value), ob)
						stack.append(str(result))

			answer = float(stack[0])
			logger.info(f"the answe is {answer}")
			return answer
		except Exception as e:
			raise Exception("Exception from the infix function")

	@staticmethod
	def apply_math_operations(operand1, operand2, operator):
		"""
		This function calculates the mathematical operations depending on the operator provided
		Parameters
		----------
		operand1: stirng: operand1
		operand2: string: operand2
		operator: string: operator

		Returns: float: answer of the mathematical operation
		-------

		"""
		logger.info("in the apply math")
		if operator == "+":
			result = operand1 + operand2
			return result

		elif operator == "-":
			result = operand1 - operand2
			return result

		elif operator == "*":
			result = operand1 * operand2
			return result

		elif operator == "/":
			result = operand1 / operand2
			return result
		else:
			logger.exception("Unrecognized operator")
			raise Exception("Not a valid operator")

	@staticmethod
	def is_operator(operator):
		"""
		This is the function to see if we are just supporting 4 operators.
		Parameters
		----------
		operator: string: operator provided

		Returns: bool: returns if the operator is a valid one or not
		-------

		"""
		list_of_operators = ["+", "-", "*", "/"]
		return operator in list_of_operators


class Prefix:
	@classmethod
	def calculate_prefix_expression(cls, expression):
		"""
		This is the function for calculating the prefix operations using stack approach.
		Parameters
		----------
		expression: string: expression string

		Returns: float: evaluated answer
		-------

		"""
		logger.info(f"in the calculate prefix expression {expression}")
		elements = expression.split()
		stack = []
		for e in reversed(elements):
			if e.isdigit():
				stack.append(int(e))
			else:
				# this is an operator
				if (len(stack) < 2):
					logger.info("invalid input")
					raise Exception("invalid input")
					break
				else:
					operand1 = stack.pop()
					operand2 = stack.pop()
					if e == "+":
						result = operand1 + operand2
						stack.append(int(result))

					elif e == "-":
						result = operand1 - operand2
						stack.append(int(result))

					elif e == "*":
						result = operand1 * operand2
						stack.append(int(result))

					elif e == "/":
						result = operand1 / operand2
						stack.append(int(result))
					else:
						logger.exception("Unrecognized operator")
						raise Exception("Not a valid operator")
		return float(stack[0])