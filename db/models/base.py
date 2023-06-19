#-*- coding: utf-8 -*-
from typing import TypeVar, Tuple, Optional, Any
from sqlalchemy import delete, update, util, select, func
from sqlalchemy.sql.selectable import Select
from sqlalchemy.sql._typing import _ColumnExpressionArgument
from sqlalchemy.orm._typing import OrmExecuteOptionsParameter
from sqlalchemy.engine.interfaces import _CoreAnyExecuteParams
from sqlalchemy.orm.session import _BindArguments
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from db.engine import get_engine

_T = TypeVar("_T")

_session = sessionmaker(get_engine())

class Base(DeclarativeBase):
     pass

     @classmethod
     def where(cls, *whereclauses: _ColumnExpressionArgument[bool]):
          if len(whereclauses) == 0:
               return select(cls)
          return select(cls).where(*whereclauses)
     
     @staticmethod
     def session():
          return _session()
     
     @classmethod
     def first(
          cls,
          statement: Select[Tuple[_T]],
          params: Optional[_CoreAnyExecuteParams] = None,
          *,
          execution_options: OrmExecuteOptionsParameter = util.EMPTY_DICT,
          bind_arguments: Optional[_BindArguments] = None,
          **kw: Any
     ):
          with cls.session() as session:
               return session.scalars(
                    statement = statement.limit(1),
                    params = params,
                    execution_options = execution_options,
                    bind_arguments = bind_arguments,
                    **kw
               ).first()

     @classmethod
     def all(
          cls,
          statement: Select[Tuple[_T]],
          params: Optional[_CoreAnyExecuteParams] = None,
          *,
          execution_options: OrmExecuteOptionsParameter = util.EMPTY_DICT,
          bind_arguments: Optional[_BindArguments] = None,
          **kw: Any
     ):
          with cls.session() as session:
               return list(
                         session.scalars(
                         statement = statement,
                         params = params,
                         execution_options = execution_options,
                         bind_arguments = bind_arguments,
                         **kw
                    ).all()
               )

     @classmethod
     def update(
          cls,
          *whereclauses: _ColumnExpressionArgument[bool]
     ):
          if len(whereclauses) == 0:
               return update(cls)
          return update(cls).where(*whereclauses)
     
     @classmethod
     def delete(
          cls,
          *whereclauses: _ColumnExpressionArgument[bool]
     ):
          if len(whereclauses) == 0:
               return delete(cls)
          return delete(cls).where(*whereclauses)
     
     @classmethod
     def count(
          cls,
          *whereclauses: _ColumnExpressionArgument[bool]
     ):
          statement = select(func.count('*')).select_from(cls)
          if len(whereclauses) > 0:
               statement = statement.where(*whereclauses)
          return statement
     