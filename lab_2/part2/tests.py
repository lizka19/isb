import sys
sys.path.append(r'C:\Users\lizak\PycharmProjects\isb\lab_2')
import math

from work_files import *


def frequency_bit_test(sequence: str) -> float:
    """
    Выполняет тест на частоту битов.
    :param sequence: Битовая последовательность
    :return: P-значение
    """
    n = len(sequence)

    if n == 0:
        raise ValueError("Sequence is empty")

    s = sum([1 if bit == "1" else -1 for bit in sequence])

    p_value = math.erfc((abs(s) / math.sqrt(n)) / math.sqrt(2))

    return p_value



