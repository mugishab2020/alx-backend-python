#!/usr/bin/env python3
'''This is for More involved type annotations
'''
from typing import Union, TypeVar, Optional, Mapping, Any


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    '''returnis the dataypes of these lists'''
    if key in dct:
        return dct[key]
    else:
        return default
