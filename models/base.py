from pydantic import BaseModel


class CamelCaseAliasBaseModel(BaseModel):
    pass

    class Config:
        allow_population_by_field_name = True
        alias_generator = lambda field_name: "".join(
            [s if i == 0 else s.capitalize()
            for i, s in enumerate(field_name.split("_"))]
        )
        orm_mode=True

