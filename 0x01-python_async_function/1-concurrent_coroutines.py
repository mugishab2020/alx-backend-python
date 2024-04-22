#!/usr/bin/env python3
'''
import asyncio
from typing import List
'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    delays = [wait_random(max_delay) for _ in range(n)]
    completed_delays = []
    for coro in asyncio.as_completed(delays):
        completed_delays.append(await coro)
    return completed_delays
