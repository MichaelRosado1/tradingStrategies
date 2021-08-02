'''
    Mean reversion strategy assumes that the price volitility and historical returns will revert to teh
    long run mean or average


'''
from trader import Trader
from mean_reversion import mean_reversion

#main function will handle trade initialization
def main():
    trader = Trader('SPY', 10)

    strat = mean_reversion(trader)

    ave = strat.calculate_moving_average()

    print('{} has a 100 day moving average of {}'.format(trader.symbol, ave))






if __name__ == '__main__':
    main()

