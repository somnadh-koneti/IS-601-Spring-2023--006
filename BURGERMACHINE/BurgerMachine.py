from enum import Enum
import sys
from BurgerMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, \
    NeedsCleaningException, OutOfStockException
from BurgerMachineExceptions import InvalidPaymentException


class Usable:
    name = ""
    quantity = 0
    cost = 99

    def __init__(self, name, quantity=10, cost=99):
        self.name = name
        self.quantity = quantity
        self.cost = cost

    def use(self):
        self.quantity -= 1
        if (self.quantity < 0):
            raise OutOfStockException
        return self.quantity

    def in_stock(self):
        return self.quantity > 0

    def __repr__(self) -> str:
        return self.name


class Bun(Usable):
    pass


class Patty(Usable):
    pass


class Topping(Usable):
    pass


class STAGE(Enum):
    Bun = 1
    Patty = 2
    Toppings = 3
    Pay = 4


class BurgerMachine:
    # Constants https://realpython.com/python-constants/
    USES_UNTIL_CLEANING = 15
    MAX_PATTIES = 3
    MAX_TOPPINGS = 3

    buns = [Bun(name="No Bun", cost=0), Bun(name="White Burger Bun", cost=1), Bun("Wheat Burger Bun", cost=1.25),
            Bun("Lettuce Wrap", cost=1.5)]
    patties = [Patty(name="Turkey", quantity=10, cost=1), Patty(name="Veggie", quantity=10, cost=1),Patty(name="Beef", quantity=10, cost=1)]
    toppings = [Topping(name="Lettuce", quantity=10, cost=.25), Topping(name="Tomato", quantity=10, cost=.25),
                Topping(name="Pickles", quantity=10, cost=.25),
                Topping(name="Cheese", quantity=10, cost=.25), Topping(name="Ketchup", quantity=10, cost=.25),
                Topping(name="Mayo", quantity=10, cost=.25), Topping(name="Mustard", quantity=10, cost=.25),
                Topping(name="BBQ", quantity=10, cost=.25)]

    # variables
    remaining_uses = USES_UNTIL_CLEANING
    remaining_patties = MAX_PATTIES
    remaining_toppings = MAX_TOPPINGS
    total_sales = 0
    total_burgers = 0

    inprogress_burger = []
    currently_selecting = STAGE.Bun

    # rules
    # 1 - bun must be chosen first
    # 2 - can only use items if there's quantity remaining
    # 3 - patties can't exceed max
    # 4 - toppings can't exceed max
    # 5 - proper cost must be calculated and shown to the user
    # 6 - cleaning must be done after certain number of uses before any more burgers can be made
    # 7 - total sales should calculate properly based on cost calculation
    # 8 - total_burgers should increment properly after a payment

    def pick_bun(self, choice):
        if self.currently_selecting != STAGE.Bun:
            raise InvalidStageException
        for c in self.buns:
            if c.name.lower() == choice.lower():
                c.use()
                self.inprogress_burger.append(c)
                return
        raise InvalidChoiceException
        
    def pick_patty(self, choice):
        if self.currently_selecting != STAGE.Patty:
            raise InvalidStageException
        if self.remaining_uses <= 0:
            raise NeedsCleaningException
        if self.remaining_patties <= 0:
            raise ExceededRemainingChoicesException
        for f in self.patties:
            if f.name.lower() == choice.lower():
                f.use()
                self.inprogress_burger.append(f)
                self.remaining_patties -= 1
                self.remaining_uses -= 1
                return
        raise InvalidChoiceException
        
    def pick_toppings(self, choice):
        if self.currently_selecting != STAGE.Toppings:
            raise InvalidStageException
        if self.remaining_toppings <= 0:
            raise ExceededRemainingChoicesException
        for t in self.toppings:
            if t.name.lower() == choice.lower():
                t.use()
                self.inprogress_burger.append(t)
                self.remaining_toppings -= 1
                return
        raise InvalidChoiceException
        
    def reset(self):
        self.remaining_patties = self.MAX_PATTIES
        self.remaining_toppings = self.MAX_TOPPINGS
        self.inprogress_burger = []
        self.currently_selecting = STAGE.Bun

    def clean_machine(self):
        self.remaining_uses = self.USES_UNTIL_CLEANING

    def handle_bun(self, bun):
        self.pick_bun(bun)
        self.currently_selecting = STAGE.Patty

    def handle_patty(self, patty):
        if patty == "next":
            self.currently_selecting = STAGE.Toppings
        else:
            self.pick_patty(patty)

    def handle_toppings(self, toppings):
        if toppings == "done":
            self.currently_selecting = STAGE.Pay
        else:
            self.pick_toppings(toppings)

    def handle_pay(self, expected, total):
        if self.currently_selecting != STAGE.Pay:
            raise InvalidStageException
        if total == str(expected):
            print("Thank you! Enjoy your burger!")
            self.total_burgers += 1
            self.total_sales += expected  # only if successful
            # print(f"Total sales so far {self.total_sales}")
            self.reset()
        else:
            raise InvalidPaymentException

    def print_current_burger(self):
        print(f"Current Burger: {','.join([x.name for x in self.inprogress_burger])}")

    def calculate_cost(self):
        # TODO add the calculation expression/logic for the inprogress_burger
        # sk3395 18-march 
        # iterating the selections from the list and using i.cost to find out the cost of the product , and checking the data type int or float and adding it to
        # the variable val and retur it .
        val=0
        for i in self.inprogress_burger:
            if type(i.cost)==float:
                val+=i.cost
            elif type(i.cost)==int:
                val+=i.cost
        
        return val

    def run(self):
        try:
            if self.currently_selecting == STAGE.Bun:
                bun = input(
                    f"What type of bun would you like {', '.join(list(map(lambda c: c.name.lower(), filter(lambda c: c.in_stock(), self.buns))))}?\n")
                self.handle_bun(bun)
                self.print_current_burger()
            elif self.currently_selecting == STAGE.Patty:
                patty = input(
                    f"Would type of patty would you like {', '.join(list(map(lambda f: f.name.lower(), filter(lambda f: f.in_stock(), self.patties))))}? Or type next.\n")
                self.handle_patty(patty)
                self.print_current_burger()
            elif self.currently_selecting == STAGE.Toppings:
                toppings = input(
                    f"What topping would you like {', '.join(list(map(lambda t: t.name.lower(), filter(lambda t: t.in_stock(), self.toppings))))}? Or type done.\n")
                self.handle_toppings(toppings)
                self.print_current_burger()
            elif self.currently_selecting == STAGE.Pay:
                expected = self.calculate_cost()
                # show expected value as currency format
                # require total to be entered as currency format
                total = input(f"Your total is {expected}, please enter the exact value.\n")
                self.handle_pay(expected, total)

                choice = input("What would you like to do? (order or quit)\n")
                if choice == "quit":
                    # exit() in recursive functions creates stackoverflow
                    # use return 1 to exit
                    print("Quitting the burger machine")
                    return 1
        except KeyboardInterrupt:
            # quit
            print("Quitting the burger machine")
            sys.exit()
        # sk3395 18-march
        # first i was trying out to find out in which stage the out of exception was ocurred and printing the bun or patty or toppings was out of stock. The bun or patty or topping variable
        # stores the input we enter.
        except OutOfStockException:
            # show an appropriate message of what stage/category was out of stock
            if self.currently_selecting == STAGE.Bun:
                print(f"{bun} was out of stock,Please choose other bun in the list.\n")
            elif self.currently_selecting == STAGE.Patty:
                print(f"{patty} was out of stock, Please choose other patty in the list.\n")
            elif self.currently_selecting == STAGE.Toppings:
                print(f"{toppings} was out of stock, Please choose other toppings in the list.\n")

        #sk3395 18-march
        # I was asking the user to type the command clean. if the user enters the correct commnad cleaning gets sucessfull, if the command enterd is wrong machine cleaning fails and displays
        #  an message to enter correct command
        except NeedsCleaningException:
            val=input(f"Machine needs to be cleaned,Please enter clean.\n")
            while True:
                if val.lower()=="clean":
                    self.clean_machine()
                    print("Machine cleaned Sucessfully")
                    break
                else:
                    val=input(f"Machine cleaning failed,Please enter correct command=clean.\n")
        #sk3395 18-march
        # first i was trying out to find out in which stage the invalid choice exception was ocurred and printing the bun or patty or toppings entered was not in list. The bun or patty or topping variable
        # stores the input we enter.
        except InvalidChoiceException:
            # show an appropriate message of what stage/category was the invalid choice was in
            if self.currently_selecting == STAGE.Bun:
                print(f"Selected item {bun} was not in list buns, Please choose bun from the provided list.\n")
            elif self.currently_selecting == STAGE.Patty:
                print(f"Selected item {patty} was not in list patty, Please choose patty from the provided list.\n")
            elif self.currently_selecting == STAGE.Toppings:
                print(f"Selected item {toppings} was not in list toppings, Please choose toppings from the provided list.\n ")
        #sk3395 18-march
        #first i was trying out to find out in which stage the exceeeded remaining choices was ocurred and printing you have exeeced the limit of chossing patty or toppings. if it is in patty moving 
        # it to next stage toppings or if it is in toppings moving it to next stage payment section 
        # stores the input we enter
        except ExceededRemainingChoicesException:
            # show an appropriate message of which stage/category was exceeded
            # move to the next stage/category
            if self.currently_selecting == STAGE.Patty:
                print("You have exceeded the limit of choosing patty, You will be redirected to toppings section.\n")
                self.currently_selecting = STAGE.Toppings
            elif self.currently_selecting == STAGE.Toppings:
                print("You have exceeded the limit of choosing toppings, You will be redirected to paymnent.\n")
                self.currently_selecting = STAGE.Pay
        #1sk3395 18-march
        # if invalid payment exception occurs, it will display an message enterd wrong amount payment fialed. 
        except InvalidPaymentException:
            print(f"Payment Failed, please enter the exact value.\n")
        except:
            # this is a default catch all, follow the steps above
            print("Something went wrong")

        self.run()

    def start(self):
        self.run()


if __name__ == "__main__":
    bm = BurgerMachine()
    bm.start()