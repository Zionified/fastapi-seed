#-*- coding: utf-8 -*-
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from utils.exceptions import add_response_exception_handler, add_exception_handler
from models.response import RESPONSE_INTERNAL_SERVER_ERROR, RESPONSE_INVALID_PARAMS, ResponseError
from utils.fastapi import add_api_routers
from conf import get_configuration

app = FastAPI()
config = get_configuration()

app = add_api_routers(app, "api")
app = add_response_exception_handler(app)
app = add_exception_handler(app, RequestValidationError, RESPONSE_INVALID_PARAMS, config.DEBUG)
app = add_exception_handler(app, Exception, RESPONSE_INTERNAL_SERVER_ERROR)

