# FastAPI-Seed Getting Started #

## Create Virtual Environment ##
```bash
pip install virtualenv
virtualenv env
. env/bin/activate
```
- (vscode) exit and re-enter terminal for the last step

## Install Alembic ##
```bash
pip install alembic
alembic init alembic
```

## Update Alembic Environment ##
In `env.py`, add the following lines:
```Python
if config.config_file_name is not None:
    fileConfig(config.config_file_name)
from conf.config import get_configuration
config.set_main_option("sqlalchemy.url", get_configuration().DB.DSN)

...

# target_metadata = mymodel.Base.metadata
from db.models import Base
target_metadata = Base.metadata

```

## Install Dependencies ##
```bash
pip install PyJWT, fastapi, SQLAlchemy
```

## Test Using Alembic ##
**Don't forget to create a database first and modify `config-dev.yaml`!**
```bash
alembic revision --autogenerate -m "xxxxx”
```

## Relevant Resources ##
1. ORM Quick Start: https://docs.sqlalchemy.org/en/20/orm/quickstart.html
2. Token-based Authorization: https://github.com/jpadilla/pyjwt/
3. FastAPI Tutorial: https://fastapi.tiangolo.com/lo/tutorial/
4. Pydantic Model Usage: https://docs.pydantic.dev/latest/usage/models/
5. Alembic Installation: https://alembic.sqlalchemy.org/en/latest/front.html#installation





