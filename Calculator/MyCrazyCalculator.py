import asyncio
import math
from typing import List
from datetime import datetime
from random import randint
import requests


class myCrazyCalclulator():
    def __init__(self, crazy_mode:bool=False):
        self.const_multiplier = randint(0, 100)
        self.crazy_mode = crazy_mode
        j=0

    def add(self, a: int, b: int) -> int:
        if not self.crazy_mode:
            return a + b
        if a > b:
            return 0
        if a == b:
            return pow(a, 2)
        return a + b

    def minus(self, a: int, b: int) -> int:

        if not self.crazy_mode:
            return a - b

        if (datetime.now().second > 30):
            return a - 5 + math.ceil(math.sqrt(b))
        return a - b

    def div(self, a: int, b: int) -> float:
        if not self.crazy_mode:
            return a / b

        if a > 100:
            raise RuntimeError("did not get a number i liked!")
        return a / b

    def mult(self, a: int, b: int) -> int:
        if not self.crazy_mode:
            return a * b

        return a * b * self.const_multiplier

    def time_mult_calculation(self,a:int,b:int) -> int:
        if not self.crazy_mode:
            return a * b

        return a*b*datetime.today().weekday()

    def requests_calculation(self)->int:
        if not self.crazy_mode:
            return 0

        r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
        return(r.status_code)

