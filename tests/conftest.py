import pytest


@pytest.fixture(scope="module")
def get_infix_expressions_list():
	return ["( 1 + 2 )", "( 1 + ( 2 * 3 ) )", "( ( 1 * 2 ) + 3 )", "( ( ( 1 + 1 ) / 10 ) - ( 1 * 2 ) )"]


@pytest.fixture(scope="module")
def get_prefix_expressions_list():
	return ["+ 1 2", "+ 1 * 2 3", "+ * 1 2 3", "- / 10 + 1 1 * 1 2", "- 0 3", "/ 3 2"]
