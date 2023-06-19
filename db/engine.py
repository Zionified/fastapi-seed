#-*- coding: utf-8 -*-
from sqlalchemy import create_engine

from conf import get_configuration

config = get_configuration()

engine = create_engine(config.DB.DSN, echo=config.DB.echo)

__DEFAULT_ENGINE__ = engine

def get_engine():
    return __DEFAULT_ENGINE__

__all__ = ["get_engine"]
