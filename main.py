from abc import ABC, abstractmethod


class ProductBase(ABC):
    @abstractmethod
    def detail(self):
        pass

    @abstractmethod
    def price(self):
        pass


class ProductShow(ABC):
    @abstractmethod
    def show(self):
        pass


class Rugs(ProductBase):
    def __init__(self, name, price):
        self.name = name
        self._price = price

    def detail(self):
        return DetailRugs(self)

    def price(self):
        return PriceRugs(self)


class DetailRugs(ProductShow):
    def __init__(self, rugs):
        self.rugs = rugs

    def show(self):
        return f"name of the rug: {self.rugs.name}"


class PriceRugs(ProductShow):
    def __init__(self, rugs):
        self.rugs = rugs

    def show(self):
        return f"price of the rug: {self.rugs._price}"


class Mobile(ProductBase):
    def __init__(self, name, model, price):
        self.name = name
        self.model = model
        self._price = price

    def detail(self):
        return DetailMobile(self)

    def price(self):
        return PriceMobile(self)


class DetailMobile(ProductShow):
    def __init__(self, mobile):
        self.mobile = mobile

    def show(self):
        return f"model of the mobile: {self.mobile.model}"


class PriceMobile(ProductShow):
    def __init__(self, mobile):
        self.mobile = mobile

    def show(self):
        return f"price of the mobile: {self.mobile._price} "


class GiftCart(ProductBase):
    def __init__(self, company, min_price, max_price):
        self.company = company
        self.min_price = min_price
        self.max_price = max_price

    def detail(self):
        return DetailGiftCart(self)

    def price(self):
        return PriceGiftCart(self)


class DetailGiftCart(ProductShow):
    def __init__(self, cart):
        self.cart = cart

    def show(self):
        return f"company of the giftcart: {self.cart.company}"


class PriceGiftCart(ProductShow):
    def __init__(self, cart):
        self.cart = cart

    def show(self):
        return f"minimum price of the GiftCart: {self.cart.min_price}" \
               f"maximum price of the GiftCart: {self.cart.max_price}"


if __name__ == "__main__":
    r1 = Rugs("persian rugs", 320)
    r2 = Rugs("nain rugs", 150)

    m1 = Mobile("samsung", "A30", 250)
    m2 = Mobile("Apple", "A2275", 1000)

    g1 = GiftCart("Google", 20, 60)
    g2 = GiftCart("Apple", 30, 70)

    products = [r1, r2, m1, m2, g1, g2]

    for product in products:
        print(f"{product.detail().show()} ----> {product.price().show()}")
