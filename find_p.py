# -*- coding = utf-8 -*-
# @Time: 2023/11/28 12:52
# @Author: Jiahao Xu
# @File：find_p.py
# @Software: PyCharm

import pandas as pd


def find_p(numbers):
    """
    计算indicators的p分位值（0-90）
    :param numbers:因子值的百分位rank序列
    :return: p分位值序列
    """
    if pd.isna(numbers):
        return None
    values = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
    p_value = max(val for val in values if val < numbers)

    return p_value


if __name__=='__main__':

    data = {}
    data = pd.DataFrame(data)
    factor = 'xxx'
    data[factor+'_rank'] = data[factor].rolling(242).apply(
            lambda x: pd.Series(x).rank(pct=True).iloc[-1] * 100)

    data[factor + '_p'] = data[factor+'_rank'].apply(
            lambda x: find_p(x) if not pd.isna(x) else None)