# -*- coding = utf-8 -*-
# @Time: 2023/12/7 9:44
# @Author: Jiahao Xu
# @File：find_p.py
# @Software: PyCharm

import pandas as pd


def find_p(data, factor_list):
    """
    计算indicators的p分位值（0-90）
    :param data:
    :param factor: 因子名称
    :return: p分位值序列
    """
    for factor in factor_list:
        factor_ranks = data[factor].rolling(242).apply(
                lambda x: pd.Series(x).rank(pct=True, na_option='keep').iloc[-1] * 100)
        if pd.isna(factor_ranks):
            return None
        else:
            values = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
            data[factor + '_P'] = max(val for val in values if val < factor_ranks)

    return data


if __name__=='__main__':

    data = {}
    data = pd.DataFrame(data)
    factor_list = ['a', 'b', 'c']

    data = find_p(data, factor_list)
