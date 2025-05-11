import sys
sys.path.append(r'C:\Users\lizak\PycharmProjects\isb\lab_2')
import math

from work_files import *
from scipy.special import gammainc


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


def same_bits_test(sequence: str) -> float:
    """
    Выполняет тест на идентичные последовательные биты.
    :param sequence: Последовательность
    :return: P-значение
    """

    p_value = 0

    n = len(sequence)

    p = sequence.count('1') / n

    if abs(p - 0.5) >= 2 / math.sqrt(n):
        return p_value

    v_n = 0

    for i in range(n - 1):

        if sequence[i] != sequence[i + 1]:
            v_n += 1

    numerator = abs(v_n - 2 * n * p * (1 - p))
    denominator = 2 * math.sqrt(2 * n) * p * (1 - p)

    return math.erfc(numerator / denominator)

