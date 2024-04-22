#!/usr/bin/env/python3
'''This is for using the  time package'''


import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''measures the total execution
    '''
    a = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    delay = (time.perf_counter() - a) / n
    return delay
