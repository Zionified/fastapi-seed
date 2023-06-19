#-*- coding: utf-8 -*-
import traceback
from typing import Type
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from .models import ResponseError

def add_response_exception_handler(app: FastAPI):
    async def response_exception_handler(request: Request, exc: ResponseError):
        return JSONResponse(
            status_code=200,
            content={"code": exc.code, "message": exc.message},
        )
    app.add_exception_handler(ResponseError, response_exception_handler)
    return app

def add_exception_handler(app: FastAPI, exc_class: Type[Exception], response_error: ResponseError, print_traceback: bool = True):
    async def exception_handler(request: Request, exc: Exception):
        print(print_traceback)
        print("test", print_traceback)
        if print_traceback:
            traceback.print_exc()
        return JSONResponse(
            status_code=200,
            content={"code": response_error.code, "message": response_error.message},
        )
    app.add_exception_handler(exc_class, exception_handler)
    return app
    