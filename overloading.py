class Products:
    def __init__(self, prod_name, country, volume, summa):
        self.prod_name = prod_name
        self.country = country
        self.volume = volume
        self.summa = summa

    def __gt__(self, other):
        if self.prod_name == other.prod_name:
            if self.volume == other.volume:
                return self.country > other.country
            else:
                return self.volume > other.volume
        else:
            return self.prod_name > other.prod_name

    def __lt__(self, other):
        if self.prod_name == other.prod_name:
            if self.volume == other.volume:
                return self.country < other.country
            else:
                return self.volume < other.volume
        else:
            return self.prod_name < other.prod_name

    def __ge__(self, other):
        if self.prod_name == other.prod_name:
            if self.volume == other.volume:
                return self.country >= other.country
            else:
                return self.volume >= other.volume
        else:
            return self.prod_name >= other.prod_name

    def __le__(self, other):
        if self.prod_name == other.prod_name:
            if self.volume == other.volume:
                return self.country <= other.country
            else:
                return self.volume <= other.volume
        else:
            return self.prod_name <= other.prod_name