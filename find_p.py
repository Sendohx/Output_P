# -*- coding = utf-8 -*-
# @Time: 2023/12/7 9:44
# @Author: Jiahao Xu
# @File：find_p.py
# @Software: PyCharm

import pandas as pd


class Output_P:
    """输出因子值分位值组件"""
    def __init__(self, data, factor_list):
        """
        :param data: 因子数据dataframe
        :param factor_list： 因子名称列表， 例： factor_list = ['yang_zhang_sigma','ILLIQ']
        """
        self.data = data
        self.factor_list = factor_list

    def formula(self, numbers):
        """
        计算因子的p分位值（0,10,20...90）
        :param numbers: 0~100的数值 
        :return: p分位值序列
        """
        if pd.isna(numbers):
            return None
        else:
            values = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
            p_values = max(val for val in values if val < numbers)
        
            return p_values
            
            
    def transform_to_p(self):
        for factor in self.factor_list:
            factor_ranks = self.data[factor].rolling(242).apply(
                        lambda x: pd.Series(x).rank(pct=True, na_option='keep').iloc[-1] * 100)
            self.data[factor + '_P'] = factor_ranks.apply(lambda x: self.formula(x) if not pd.isna(x) else None)
    
        return self.data

if __name__=='__main__':

    data = {}
    data = pd.DataFrame(data)
    factor_list = ['ILLIQ','yang_zhang_sigma','stock_sigma_mean']

    P = Output_P(data, factor_list)
    data1 = P.transform_to_p()
    data1 = data1[data1['date'] >= '20210101']
