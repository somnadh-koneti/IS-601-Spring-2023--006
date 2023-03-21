import pytest
# make sure there's an __init__.py in this tests folder and that
# the tests folder is in the same folder as the IcecreamMachine stuff
from BurgerMachine import BurgerMachine,STAGE
from BurgerMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, OutOfStockException
#this is an example test showing how to cascade fixtures to build up state

@pytest.fixture
def machine():
    bm = BurgerMachine()
    return bm
# sample fixture, can delete if not using

# sk3395 18-march
# In this test we are checking wheather selection of bun is first selection by currently selecting is equal to stage bun
def test1(machine):
    assert machine.currently_selecting.name == STAGE.Bun.name

#sk3395 18-march
# the objective of the test case is to handle outofstock exception when quantity of patties is 0. we set quantity of the first patties[0].quantity=1. And then it handles the order by 
# machine handling method such as handle_bun, handle_patty. we use try and except to catch an outofstock exception, if quantity is 0 and exception raised then assert false
# will pass the test. If exception not raised machine.patties[0].quantity==1 will fail and test is failed.
def test2(machine):
    machine.patties[0].quantity = 1
    machine.handle_bun("White Burger Bun")
    machine.handle_patty("veggie")
    try:
        machine.handle_patty("veggie")
        assert machine.patties[0].quantity == 1
    except OutOfStockException:
        assert False

#sk3395 18-march
# the objective of the test case is to handle outofstock exception when quantity of toppings is 0. we set quantity of the first toppings[0].quantity=1. And then it handles the order by 
# machine handling method such as handle_bun, handle_patty and handle_toppings. we use try and except to catch an outofstock exception, if quantity is 0 and exception raised then assert false
# will pass the test. If exception not raised machine.toppings[0].quantity==1 will fail and test is failed.   
def test3(machine):
    machine.toppings[0].quantity = 1
    machine.handle_bun("White Burger Bun")
    machine.handle_patty("next")
    machine.handle_toppings("Tomato")
    try:
        machine.handle_toppings("Tomato")
        assert machine.toppings[0].quantity == 1
    except OutOfStockException:
        assert False

# sk3395 18-march
#the test checks that the machine can handle the max number of patties. the test handles the burger with white burger bun and loops the max limit number of turkey , and when the 
# turkey reaches to -1 exceededremainingchoices exception occurs.here,the assert keyword confirms the remaining number of patties added and final patties are 0.  

def test4(machine):
    machine.patties[0].quantity=10
    machine.handle_bun("White Burger Bun")
    for i in range(machine.MAX_PATTIES - 1):
        machine.handle_patty("turkey")
    try:
        machine.handle_patty("turkey")
        assert machine.remaining_patties == 0
    except ExceededRemainingChoicesException:
        assert False

#sk3395 18-march
# the test checks that the machine can handle the max number of toppings. the test handles the burger with white burger bun and loops the max limit number of ketchups , and when the 
# ketchup reaches to -1 exceededremainingchoices exception occurs. assert keyword confirms the remaining number of toppings added and final toppings are 0.  
def test5(machine):
    machine.handle_bun("White Burger Bun")
    machine.handle_patty("next")
    for scoop in range(machine.MAX_TOPPINGS - 1):
        machine.handle_toppings("Ketchup")
    try:
        machine.handle_toppings("Ketchup")
        assert machine.remaining_toppings == 0
    except ExceededRemainingChoicesException:
        assert False

# sk3395 18-march
# the test first uses reset() function to reset the remaining_patties and toppings and makes inprogress burger list empty and stage to bun. we select bun, toppings, patty by machine handle methods 
# and claculate the cost by calculate_cost() function and compare it with the value we enterd , the test case passes if it matches with the value we enterd.  
def test6(machine):
    machine.reset()
    machine.handle_bun("White Burger Bun")
    machine.handle_patty("turkey")
    machine.handle_patty("veggie")
    machine.handle_patty("veggie")
    machine.handle_patty("next")
    machine.handle_toppings("Mustard")
    machine.handle_toppings("BBQ")
    machine.handle_toppings("Ketchup")
    machine.handle_toppings("done")
    assert machine.calculate_cost() == 4.75
#sk3395 18-march
# In this test we select bun, toppings, patty by machine handle methods and claculate the cost by calculate_cost() function and stores it in a variable and compare it with handle pay
# and the process is repeated with other order and compare the machine.total_sales with the sum of the variables. if the values are equal test case passes.
def test7(machine):
    machine.handle_bun("White Burger Bun")
    machine.handle_patty("turkey")
    machine.handle_patty("turkey")
    machine.handle_patty("next")
    machine.handle_toppings("Mustard")
    machine.handle_toppings("done")
    bur = float(machine.calculate_cost())
    machine.handle_pay(bur, str(bur))

    machine.handle_bun("lettuce wrap")
    machine.handle_patty("turkey")
    machine.handle_patty("next")
    machine.handle_toppings("Pickles")
    machine.handle_toppings("mayo")
    machine.handle_toppings("done")
    bu = float(machine.calculate_cost())
    machine.handle_pay(bu, str(bu))

    assert machine.total_sales == bur + bu
# sk3395 18-march
# In this test we select bun, toppings, patty by machine handle methods and claculate the cost by calculate_cost() function and stores it in a variable and compare it with handle pay
# and the process is repeated with other orders and compare the machine.total_burger==3 and BurgerMachine().total_burgers==0.

def test8(machine):
    machine.handle_bun("White Burger Bun")
    machine.handle_patty("Turkey")
    machine.handle_patty("next")
    machine.handle_toppings("done")
    C1 = float(machine.calculate_cost())
    machine.handle_pay(C1, str(C1))

    machine.handle_bun("wheat burger bun")
    machine.handle_patty("next")
    machine.handle_toppings("Pickles")
    machine.handle_toppings("done")
    C2 = float(machine.calculate_cost())
    machine.handle_pay(C2, str(C2))

    machine.handle_bun("wheat burger bun")
    machine.handle_patty("next")
    machine.handle_toppings("Mustard")
    machine.handle_toppings("done")
    C3 = float(machine.calculate_cost())
    machine.handle_pay(C3, str(C3))
    
    assert BurgerMachine().total_burgers == 0 and machine.total_burgers == 3