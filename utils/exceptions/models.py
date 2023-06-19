#-*- coding: utf-8 -*-
class ResponseError(Exception):
    code: str
    message: str
    
    def __init__(self, code, message):
        self.code = code
        self.message = message
        
    def set_message(self, message):
        return ResponseError(self.code, message)