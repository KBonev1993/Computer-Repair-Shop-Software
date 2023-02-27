class Customer:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

class Item:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

class Repair:
    def __init__(self, customer, item, issue):
        self.customer = customer
        self.item = item
        self.issue = issue

class ComputerRepairShop:
    def __init__(self):
        self.repairs = []

    def add_repair(self, repair):
        self.repairs.append(repair)

    def remove_repair(self, repair):
        self.repairs.remove(repair)

    def get_repairs(self):
        return self.repairs

    def search_repairs_by_customer(self, customer_name):
        return [repair for repair in self.repairs if repair.customer.name == customer_name]

    def search_repairs_by_item(self, item_name):
        return [repair for repair in self.repairs if repair.item.name == item_name]

    def search_repairs_by_issue(self, issue):
        return [repair for repair in self.repairs if repair.issue == issue]
