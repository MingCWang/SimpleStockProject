transactionfee = 0.001425
discount = 0.0028
tax = 0.003


class Percentage():
    def __init__(self, high, low, my):
        self.high = high
        self.low = low
        self.my = my

    def profit(self):
        result = (self.high - self.my) / self.my
        return result*100

    def loss(self):
        result = (self.low - self.my) / self.my
        return result * 100


class ProfitLoss(Percentage):
    def __init__(self, high, low, my, units):
        super().__init__(high, low, my)
        self.units = units

    def Loss(self):
        convert = self.units * 1000 # Convert stock price to actual money
        cost = (self.my * transactionfee * discount) + (self.low * transactionfee * discount) + (self.low * tax)
        loss = self.low - self.my - cost
        return loss * convert

    def Profit(self):
        convert = self.units * 1000
        cost = (self.my * transactionfee * discount) + (self.high * transactionfee * discount) + (self.high * tax)
        profit = self.high - self.my - cost
        return profit * convert
