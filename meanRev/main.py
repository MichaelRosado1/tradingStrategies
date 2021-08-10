'''
    Mean reversion strategy assumes that the price volitility and historical returns will revert to teh
    long run mean or average


'''
import stream
from trader import Trader
from mean_reversion import meanReversion

#main function will handle trade initialization
def main():
    trader = Trader('SPY', 10)
    stream.load_trader(trader)

    strat = meanReversion(trader)

    strat.start_trading()







if __name__ == '__main__':
    main()

