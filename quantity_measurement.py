from logger import *


class QuantityMeasurement:

    def compare_length(self, unit1, unit2, quantity1, quantity2):
        """

        :param unit1: unit of 1st length
        :param unit2: unit of 2nd length
        :param quantity1: 1st length
        :param quantity2: 2nd length
        :return: equality of the lengths if both are not null
        """
        try:
            if quantity1 is not None and quantity2 is not None:
                if unit1 == "ft":
                    quantity1 *= 12
                if unit2 == "ft":
                    quantity2 *= 12
                if quantity1 == quantity2:
                    return True
                else:
                    return False
            elif quantity1 is None or quantity2 is None:
                return None
            return 0
        except Exception as e:
            logger.error(e)
