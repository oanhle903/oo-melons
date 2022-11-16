"""Classes for melon orders."""

class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""

    # the following 2 lines can be included, but are not necessary because 
    # AbstractMelonOrder should never be instantiated directly

    # order_type = None
    # tax = 0

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False

   

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super().__init__(species,qty)
        self.order_type = "domestic"
        self.tax = 0.08

    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5
        if 'Christmas' in self.species: # order1 = Domestic...('Chrismas watermelon', 7)
            base_price = base_price * 1.5
        
        total = (1 + self.tax) * self.qty * base_price

        return total


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""


    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species,qty)
        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5
        if 'Christmas' in self.species: # order1 = Domestic...('Chrismas watermelon', 7)
            base_price = base_price * 1.5
        
        if self.qty < 10:
            total = (1 + self.tax) * self.qty * base_price + 3
        else:
            total = (1 + self.tax) * self.qty * base_price

        return total


class GovernmentMelonOrder(AbstractMelonOrder):
    def __init__(self, species, qty):
        super().__init__(species,qty)
        self.order_type = "government"
        self.tax = 0
        self.passed_inspection = False

    def marked_inspection(self):

        self.passed_inspection = True