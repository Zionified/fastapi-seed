#-*- coding: utf-8 -*-
from lib2to3.pgen2 import driver
from dotenv import load_dotenv
from pydantic import BaseModel, BaseSettings
import yaml

class MySQLConfiguration(BaseModel):
  driver: str = "pymysql"
  host:str 
  port: int = 3306
  user: str
  password: str = ""
  name: str
  echo: bool = False
  
  @property
  def DSN(self):
      if self.password == "":
          return "mysql+{}://{}@{}:{}/{}".format(self.driver, self.user, self.host, self.port, self.name)
      else:
          return "mysql+{}://{}:{}@{}:{}/{}".format(self.driver, self.user, self.password, self.host, self.port, self.name)
      
class ServerConfiguration(BaseModel):
    secret: str

class Configuration(BaseModel):
    DEBUG: bool | None = None
    DB: MySQLConfiguration
    server: ServerConfiguration

class EnvSetting(BaseSettings):
    DEBUG: bool = False
    ENV: str | None = None
    

load_dotenv()

__CONFIGURATION__ = None


def get_configuration():
    global __CONFIGURATION__
    if __CONFIGURATION__ is not None:
        return __CONFIGURATION__

    env = EnvSetting()
    config_path = "config.yaml" if env.ENV is None else "config-{}.yaml".format(env.ENV)
    # print(config_path)
    with open(config_path, "r") as f:
        # print(yaml.load(f, yaml.FullLoader))
        __CONFIGURATION__ = Configuration.parse_obj(yaml.load(f, yaml.FullLoader))
    __CONFIGURATION__.DEBUG = env.DEBUG if __CONFIGURATION__.DEBUG is None else __CONFIGURATION__.DEBUG
    # print(__CONFIGURATION__.DB.DSN)
    return __CONFIGURATION__

__all__ = ["get_configuration", "Configuration"]
    