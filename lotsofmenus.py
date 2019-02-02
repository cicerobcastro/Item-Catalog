from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem, User

engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# create user
User1 = User(name="admin", email="cicerobcastro@gmail.com")
session.add(User1)
session.commit()

# Menu for UrbanBurger
restaurant1 = Restaurant(name="Urban Burger")

session.add(restaurant1)
session.commit()

menuItem2 = MenuItem(name="Veggie Burger",
                     description="Juicy grilled veggie patty with tomato",
                     price="$7.50", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


menuItem1 = MenuItem(name="French Fries",
                     description="with garlic and parmesan",
                     price="$2.99", course="Appetizer", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Chicken Burger",
                     description="Chicken patty with tomato mayo",
                     price="$5.50", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Chocolate Cake", description="fresh baked",
                     price="$3.99", course="Dessert", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Sirloin Burger",
                     description="Made with grade A beef",
                     price="$7.99", course="Entree", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name="Root Beer", description="16 of refreshing goodness",
                     price="$1.99", course="Beverage", restaurant=restaurant1)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(name="Iced Tea", description="with Lemon",
                     price="$.99", course="Beverage", restaurant=restaurant1)

session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(name="Grilled Cheese Sandwich",
                     description="On texas toast with American Cheese",
                     price="$3.49", course="Entree", restaurant=restaurant1)

session.add(menuItem7)
session.commit()

menuItem8 = MenuItem(name="Veggie Burger",
                     description="Made with freshest of ingredients",
                     price="$5.99", course="Entree", restaurant=restaurant1)

session.add(menuItem8)
session.commit()


# Menu for Super Stir Fry
restaurant2 = Restaurant(name="Super Stir Fry")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(name="Chicken Stir Fry",
                     description="With your choice of noodles vegetables",
                     price="$7.99", course="Entree", restaurant=restaurant2)
session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Peking Duck",
                     description="Prepared since the imperial ey the skin.",
                     price="$25", course="Entree", restaurant=restaurant2)
session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Spicy Tuna Roll",
                     description="Seared rare ahi, cucumber with wasabi",
                     price="15", course="Entree", restaurant=restaurant2)
session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Nepali Momo ",
                     description="Steamed dumplings made with vegetables.",
                     price="12", course="Entree", restaurant=restaurant2)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name="Beef Noodle Soup",
                     description="A Chinese noodle soup made of stewed.",
                     price="14", course="Entree", restaurant=restaurant2)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(name="Ramen", description="a Japanese noodle soup dish.",
                     price="12", course="Entree", restaurant=restaurant2)

session.add(menuItem6)
session.commit()

print "added menu items!"
