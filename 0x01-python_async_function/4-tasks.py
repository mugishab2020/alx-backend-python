#!/usr/bin/env python3
''' Tasks
'''
from typing import List
import asyncio


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''takes in n and max_delay and
       spawn task_wait_random n times with the
       specified max_delay
    '''
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
