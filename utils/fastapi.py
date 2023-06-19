#-*- coding: utf-8 -*-
import pkgutil

from fastapi import APIRouter, FastAPI

def scan_api_routers(module_paths: str):
    """scan APIRouter under designated module paths

    Args:
        module_path (str): module path
    """
    if isinstance(module_paths, str):
        module_paths = [module_paths]
    
    routers = {}
    for module_path in module_paths:
        # print(module_path)
        for (module_finder, name, ispkg) in pkgutil.walk_packages([module_path], module_path + "."):
            # print(name)
            if ispkg:
                continue
            module_loader = module_finder.find_module(name)
            module = module_loader.load_module(name)
            for attr_name in dir(module):
                if attr_name.startswith("_"):
                    continue
                attr = getattr(module, attr_name)
                if not isinstance(attr, APIRouter):
                    continue
                routers[name + "." + attr_name] = attr
    return list(routers.values())

def add_api_routers(app: FastAPI, module_paths: list[str] | str):
    for api_router in scan_api_routers(module_paths):
        app.include_router(api_router)
    return app
                    