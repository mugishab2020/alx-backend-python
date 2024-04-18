#!/usr/bin/env python3
'''this is the function that returns the datatyoe of
itaratable objects'''


from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:

    return [(i, len(i)) for i in lst]
