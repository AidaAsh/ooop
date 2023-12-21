class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        print("У вас на счету ", self._balance)
        money = input("Сколько положить на счет? ")
        self._balance = self._balance + int(money)
        print("сейчас у вас на счету ", self._balance)

    def _kill(self):
        self._balance = 0

    def __jackpot(self):
        self._balance *= 10

    def jackpot(self):
        #  Так как я забыла как обойти приватный метод
        self.__jackpot()
        return self._balance

    def print_balance(self):
        return self._balance

    def _unite(self, client):
        self._balance += client.print_balance()


client1 = Bank("Mir", 100)
client2 = Bank("Nur", 200)
client1.moneyX()
client2.moneyX()
client1._unite(client2)
print("после метода unite()", client1.print_balance())
client1._kill()
print("после метода kill", client1.print_balance())
print("после метода jackpot", client2.jackpot())
