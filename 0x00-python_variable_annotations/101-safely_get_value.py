#!/usr/bin/env python3
'''This is for More involved type annotations
'''
from typing import Union, TypeVar, Optional, Mapping, Any


M= TypeVar('M')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[M] = None) -> Union[Any, M]:

   
    if key in dct:
        return dct[key]
    else:
        return default