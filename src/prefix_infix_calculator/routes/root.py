from fastapi import APIRouter, Request

router = APIRouter()


@router.get("/healthcheck")
def calculate_infix_expression(
) :
    return "OK"