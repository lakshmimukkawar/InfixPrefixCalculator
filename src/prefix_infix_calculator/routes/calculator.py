from fastapi import APIRouter
from prefix_infix_calculator.services.calculator_service import Infix, Prefix
from pydantic import BaseModel
from prefix_infix_calculator.services.utils import get_logger
logger = get_logger(__name__)

router = APIRouter()


class InfixPrefixRequest(BaseModel):
    expression: str


class InfixResponse(BaseModel):
    expression: str
    infix_answer: float


class PrefixResponse(BaseModel):
    expression: str
    prefix_answer: float


@router.post("/infix", response_model=InfixResponse)
def calculate_infix_expression(infix_request: InfixPrefixRequest) -> InfixResponse:
    """
    This is the main function for infix call. It returns the response from the calculator service.
    Parameters
    ----------
    infix_request: InfixPrefixRequest: Request containing the expression

    Returns: InfixResponse: returns the expression and the value
    -------

    """
    answer = Infix.calculate_infix_expression(infix_request.expression)
    response = {"expression": infix_request.expression, "infix_answer": answer}
    return response



@router.post("/prefix", response_model=PrefixResponse)
def calculate_infix_expression(prefix_request: InfixPrefixRequest) -> PrefixResponse:
    """
    This is the main function for prefix call. It returns the response from the calculator service.
    Parameters
    ----------
    prefix_request: InfixPrefixRequest: Request containing the expression

    Returns: PrefixResponse: returns the expression and the value
    -------

    """
    answer = Prefix.calculate_prefix_expression(prefix_request.expression)
    response = {"expression": prefix_request.expression, "prefix_answer": answer}
    return response
