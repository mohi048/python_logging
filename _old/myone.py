import logging
import inspect # used to find the class method names

logger = logging.getLogger('My First Logger') # creates logger object
myformat = '%(asctime)s - %(name)s - %(levelname)s - %(message)s' # Defines the log file formatting
logging.basicConfig(level=logging.DEBUG, filename='myprog.log', format=myformat) # defines the logging basic parameters

'''
Logging levels -:
1. DEBUG = detailed info
2. INFO = confirmation that things according to plan
3. WARNING = Somthing unexpected
4. ERROR = Some function failed
5. CRTITICAL = Something failed application must close
'''

class Item(object):

    def __init__(self,item):
	self.item = item
	logger.debug("Debugging at line number {2} Item created {0} in function call -- {1} -- called at line number {3}".format(self.item, inspect.stack()[0][3], inspect.stack()[0][2], inspect.stack()[1][2])) #This is the only way to get function name

    def buy(self,quantity):
	self.quantity = quantity
	print "Buy {0} number {1}".format(self.quantity,self.item)
	logger.debug("Debugging at line number {3} Item {0} buy out {1} in function call -- {2} -- called at line number {4}".format(self.item, self.quantity, inspect.stack()[0][3], inspect.stack()[0][2], inspect.stack()[1][2]))

    def sell(self,quantity):
	self.quantity = quantity
	print "sold out {0} number {1}".format(self.quantity,self.item)
	logger.debug("Debugging at line number {3} Item {0} buy out {1} in function call -- {2} -- called at line number {4}".format(self.item, self.quantity, inspect.stack()[0][3], inspect.stack()[0][2], inspect.stack()[1][2]))


s = Item('Apples')
s.buy(90)
s.sell(10)