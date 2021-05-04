class QuantityMeasurement:

    def compare_length(self, unit1, unit2, quantity1, quantity2):
        if unit1 == "ft":
            quantity1 *= 12
        if unit2 == "ft":
            quantity2 *= 12
        if quantity1 == quantity2:
            return True
        else:
            return False
