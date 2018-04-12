import logging
import time 

logging.basicConfig(filename="test_{}.log".format(time.ctime()),
                    format='%(asctime)s - %(levelname)s: %(message)s',
                    datefmt='%I:%M:%S.%f',
                    level=logging.DEBUG)

class test(object):
    def __init__(self):
        logging.info("New object was created.")

    def sum(self, arg1, arg2):
        try:
            sum = arg1 + arg2
            logging.info("Summed to {}".format(sum))
        except TypeError:
            logging.warning("Arguments are of different types.")

if __name__ == "__main__":
    obj = test()
    obj.sum(1,2)
    obj.sum(1,'a')