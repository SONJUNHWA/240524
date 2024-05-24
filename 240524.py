class Bungeoppang:
    def __init__(self, name, price):
        self.taste = name
        self.price = price
        self.total = 0
    def sell(self):
        print(f"{self.taste}을 {self.price}에 팔았습니다.")
        self.total += self.price
    def eat(self):
        print(f"{self.name}을 먹습니다.")


puff_Bungeoppang = Bungeoppang("슈크림", 1000)
puff_Bungeoppang.sell()
puff_Bungeoppang.sell()
puff_Bungeoppang.sell()
puff_Bungeoppang.sell()
print(puff_Bungeoppang.total)