transactionfee = 0.001425
discount = 0.0028
tax = 0.003

class ProfitLoss():
    def __init__(self, high, low, my, units):
        self.units = units
        self.high = high
        self.low = low
        self.my = my

    def Buy(self):
        cost = self.my * transactionfee * discount
        Buy = self.my + cost
        return Buy * self.units

    def Loss(self):
        cost = (self.my * transactionfee * discount) + (self.low * transactionfee * discount) + (self.low * tax)
        loss = self.low - self.my - cost
        return loss * self.units

    def Profit(self):
        cost = (self.my * transactionfee * discount) + (self.high * transactionfee * discount) + (self.high * tax)
        profit = self.high - self.my - cost
        return profit * self.units

    def profitper(self):
        result = self.Profit() / (self.my * self.units)
        return result * 100

    def lossper(self):
        result = self.Loss() / (self.my * self.units)
        return result * 100

