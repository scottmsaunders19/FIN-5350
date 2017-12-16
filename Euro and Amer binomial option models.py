import numpy as np
from scipy.stats import binom

class VanillaOption(object):

	def __init__(self, strike, expiry):
		self.strike = strike
		self.expiry = expiry

	def payoff(self, spot):
		pass

class VanillaCallOption(VanillaOption):

	def payoff(self, spot):
		return np.maximum(spot - self.strike, 0.0)

class VanillaPutOption(VanillaOption):

	def payoff(self, spot):
		return np.maximum(self.strike - spot, 0.0)
def EuropeanBinomialModel(option, spot, rf, dividend, volatility, T, steps):
    #dividend = beta, volatility = sd
    H = T/steps
    up = np.exp((rf-dividend) * H + volatility* (np.sqrt(H)))
    down = np.exp((rf-dividend) * H - volatility* (np.sqrt(H)))
    prob_up = (np.exp((rf-dividend)*H)-down)/(up-down)
    prob_down = 1 - prob_up
    spotT = 0.0
    callT = 0.0
    N = steps
    numNodes = N + 1
    for i in range(numNodes):
        spotT = spot * (up ** (N - i)) * (down ** (i))
        callT += option.payoff(spotT) * binom.pmf(N - i, N, prob_up)
    callPrice = callT * np.exp(-rf * T)
    return callPrice

def AmericanBinomialModel(option, spot, rf, dividend, volatility, T, steps):
    H = T/steps
    up = np.exp((rf-dividend)*H + volatility * (np.sqrt(H)))
    down = np.exp((rf - dividend) * H - volatility * (np.sqrt(H)))
    prob_up = (np.exp((rf - dividend) * H)-down)/(up - down)
    prob_down = 1- prob_up
    N = steps
    numNodes = N + 1
    disc_prob_up = prob_up * np.exp(-rf * H)
    disc_prob_down = prob_down * np.exp(-rf * H)
    Ct = np.zeros(numNodes)
    St = np.zeros(numNodes)
    for i in range(numNodes):
        St[i] = spot * (up ** (N - i)) * (down ** i)
        Ct[i] = option.payoff(St[i])
    for i in range ((N - 1), -1, -1):
        for j in range(i + 1):
            Ct[j] = disc_prob_up * Ct[j] + disc_prob_down * Ct[j + 1]
            St[j] = St[j] / up
            Ct[j] = np.maximum(Ct[j], option.payoff(St[j]))
    return Ct[0]

def main():
    P = 41
    K = 40
    rf = .08
    volatility = .3
    dividend = 0.0
    T = 1
    N = 3
    option = VanillaCallOption(K, T)
    x = EuropeanBinomialModel(option,P,rf,dividend,volatility,T,N)
    y = AmericanBinomialModel(option,P,rf,dividend,volatility,T,N)
    print("The two period European Binomial Price is = {0:.4f}".format(x),"\n")
    print("The two period American Binomial Price is = {0:.4f}".format(y))
    
main()  

    