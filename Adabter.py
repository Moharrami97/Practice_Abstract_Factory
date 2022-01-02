from main import Mobile


class PriceAdabter:
    def __init__(self, rate):
        self.rate = rate

    def exchange(self, product):
        return self.rate * product._price


if __name__ == "__main__":
    mobile1 = Mobile("samsung", "A30", 20)
    mobile2 = Mobile("Apple", "A2275", 100)

    adapter = PriceAdabter(rate=28000)
    mobile_list = [mobile1, mobile2]

    for mobile in mobile_list:
        print(f"{mobile.name}: {adapter.exchange(mobile)}")
