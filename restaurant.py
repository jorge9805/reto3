class MenuItem:
    def __init__(self,name,price):
        self.name=name
        self.price=price
class Beverage(MenuItem):
    def __init__(self,name,price,volume,alcohol_content,lactose_free):
        super().__init__(name,price)
        self.volume=volume
        self.alcohol_content=alcohol_content
        self.lactose_free=lactose_free
class Appetizer(MenuItem):
    def __init__(self,name,price,calories):
        super().__init__(name,price)
        self.calories=calories

class MainCourse(MenuItem):
    def __init__(self,name,price,calories,is_vegan):
        super().__init__(name,price)
        self.calories=calories
        self.is_vegan=is_vegan
class Dessert(MenuItem):
    def __init__(self,name,price,calories,is_gluten_free):
        super().__init__(name,price)
        self.calories=calories
        self.is_gluten_free=is_gluten_free
class Order:
    def __init__(self,table_number):
        self.table_number=table_number
        self.menu_items=[]
    def add_menu_item(self,menu_item):
        self.menu_items.append(menu_item)
    def calculate_total_bill(self):
        total=0
        for item in self.menu_items:
            total+=item.price
        return total
    def apply_discount(self,discount):
        #based on the person
        if "senior" in discount:
            return self.calculate_total_bill()*0.9
        if "student" in discount:
            return self.calculate_total_bill()*0.8
        if "birthday" in discount:
            return self.calculate_total_bill()*0.7
        #based on the order composition
        if "beverage" in discount:
            for item in self.menu_items:
                if isinstance(item,Beverage):
                    return self.calculate_total_bill()*0.9
        if "combo" in discount:
            for item in self.menu_items:
                if isinstance(item,MainCourse) and isinstance(item,Appetizer) and isinstance(item,Dessert):
                    return self.calculate_total_bill()*0.8
        if "huge" in discount:
            if len(self.menu_items)>=4:
                return self.calculate_total_bill()*0.85

#items
roasted_chicken=MainCourse("Roasted Chicken",15,500,False)
chicken_wings=Appetizer("Chicken Wings",10,300)
chocolate_cake=Dessert("Chocolate Cake",5,400,True)
beer=Beverage("Beer",5,0.5,0.05,False)
salmon=MainCourse("Salmon",20,600,False)
fries=Appetizer("Fries",5,200)
ice_cream=Dessert("Ice Cream",4,300,True)
wine=Beverage("Wine",8,0.75,0.12,False)
lemonade=Beverage("Lemonade",3,0.3,0,False)
lentil_soup=Appetizer("Lentil Soup",6,250)
apple_pie=Dessert("Apple Pie",5,350,True)
water_with_ice=Beverage("Water with Ice",0,0.5,0,False)
pork_cheeks=MainCourse("Pork Cheeks",18,550,False)
orange_chiken=MainCourse("Orange Chicken",16,500,False)
vegan_hamburguer=MainCourse(" Vegan Hamburguer",14,450,True)
#orders
order1=Order(1)
order1.add_menu_item(roasted_chicken)
order1.add_menu_item(chicken_wings)
order1.add_menu_item(chocolate_cake)
order1.add_menu_item(beer)
order2=Order(2)
order2.add_menu_item(salmon)
order2.add_menu_item(fries)
order2.add_menu_item(ice_cream)
order2.add_menu_item(wine)
order3=Order(3)
order3.add_menu_item(lemonade)
order3.add_menu_item(lentil_soup)
order3.add_menu_item(apple_pie)
order3.add_menu_item(water_with_ice)
order1.apply_discount("senior")
order2.apply_discount("combo")
order3.apply_discount("huge")
print("the discount is",order1.apply_discount("senior"))
print("your bill is",order1.calculate_total_bill())
print("the discount is",order2.apply_discount("combo"))
print("your bill is",order2.calculate_total_bill())
print("the discount is",order3.apply_discount("huge"))
print("your bill is",order3.calculate_total_bill()) 
