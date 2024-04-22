#!/usr/bin/env python3
''' this si to use asyncio.as-complited method'''


from typing import List
import asyncio

new_wait = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> float:
    '''We are taking the max_delay and n as arguments
    and spawn wait_random n times'''
    a = [new_wait(max_delay) for _ in range(n)]
    return [await a for a in asyncio.as_completed(a)]
