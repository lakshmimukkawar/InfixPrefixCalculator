from typing import Callable
from prefix_infix_calculator.routes import calculator, root
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from starlette.responses import JSONResponse, Response


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(root.router)
    # Enrich endpoint
    app.include_router(calculator.router)

    @app.exception_handler(HTTPException)
    async def http_exception_handler(exc: HTTPException):
        """
        Generic HTTPException handler, used for 404s and 405s
        """
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "status": exc.status_code,
                "error": str(exc.detail).lower().replace(" ", "_"),
                "error_description": str(exc.detail),
            },
        )

    @app.middleware("http")
    async def internal_server_error_exception_handler(
        request: Request, call_next: Callable[[Request], Response]
    ) -> JSONResponse:
        """
        Generic internal server error handler
        """
        try:
            return await call_next(request)
        except Exception as err:
            return JSONResponse(
                status_code=500,
                content={
                    "status": 500,
                    "error": "internal_server_error",
                    "error_description": "",
                },
            )


    return app
