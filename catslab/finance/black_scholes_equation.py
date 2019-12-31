
from scipy.stats import norm
from math import exp,log,sqrt


class BlackScholesEquation():
    """[Black Scholes Equation]
    Refer: 
        1. https://www.monte-carlo-note.com/2017/04/python-option-premium-BS.html
        2. https://www.jpx.co.jp/learning/derivatives/options/02.html
    Returns:
        [type] -- [description]
    """
    
    
    @classmethod
    def call(cls, S0, sigma ,r, q, T, K):
        """[Call option theoretical price]
        
        Arguments:
            S0 {[type]} -- [当日のオプション生産指数]
            sigma {[type]} -- [description]
            r {[type]} -- [description]
            q {[type]} -- [description]
            T {[type]} -- [description]
            K {[type]} -- [description]
        
        Returns:
            [type] -- [description]
        """
        d1 = (log(S0 / K) + (r - q ) * T) / (sigma * sqrt(T))+sigma*sqrt(T)/ 2
        d2 = (log(S0 / K) + (r - q ) * T) / (sigma * sqrt(T))-sigma*sqrt(T)/ 2
        BS_Call = S0 * exp(-q * T)* norm.cdf(x=d1, loc=0, scale=1)\
        -K * exp(-r * T) * norm.cdf(x=d2, loc=0, scale=1)
        return BS_Call

    @classmethod
    def put(cls, S0, sigma ,r, q, T, K):
        """[Put option]
        
        Arguments:
            S0 {[type]} -- [description]
            sigma {[type]} -- [description]
            r {[type]} -- [description]
            q {[type]} -- [description]
            T {[type]} -- [description]
            K {[type]} -- [description]
        
        Returns:
            [type] -- [description]
        """
        d1 = (log(S0 / K) + (r - q + sigma**2 / 2) * T) / (sigma * sqrt(T))
        d2 = d1 - sigma * sqrt(T)
        BS_Put = K * exp(-r * T) * norm.cdf(x=-d2, loc=0, scale=1)\
        -S0 * exp(-q * T) * norm.cdf(x=-d1, loc=0, scale=1)
        return BS_Put
