class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        money = input("Сколько положить на счет? ")
        self._balance += money

    def _kill(self):
        self._balance = 0

    def __jackpot(self):
        self._balance *= 10

    def _unite(self, client):
        self._balance += client._balance

