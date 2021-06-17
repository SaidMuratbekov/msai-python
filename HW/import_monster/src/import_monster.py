# -*- coding: utf-8 -*-
import importlib
from types import ModuleType
from typing import Callable, List, Union


def methods_importer(
    method_name: str, modules: List[Union[str, ModuleType]]) -> List[Callable]:
    methods_list = []
    for module in modules:
        try:

            if isinstance(module, ModuleType):
                mod = module
            elif isinstance(module, str):
                mod = importlib.import_module(module)
            else:
                raise TypeError("Ahctung! Neither the str not the module")
            met = getattr(mod, method_name, None)
            if met and isinstance(met, Callable):
                methods_list.append(met)
        except ImportError:
            continue
    return methods_list
