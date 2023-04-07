import pandas as pd
import numpy as np
import math

chat_id = 616199784 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    t = np.full(x.shape, 4)
    lt = x.sum()
    l = lt / t.mean()
    return l
