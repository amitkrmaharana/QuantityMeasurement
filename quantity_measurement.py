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
            unit_dict = {"ft": 3, "in": 36, "yd": 1}
            if quantity1 is not None and quantity2 is not None:
                quantity1 /= unit_dict[unit1]
                quantity2 /= unit_dict[unit2]
                if quantity1 == quantity2:
                    return True
                else:
                    return False
            else:
                return None
        except Exception as e:
            logger.error(e)
