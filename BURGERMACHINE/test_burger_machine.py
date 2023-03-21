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
# 
def test1(machine):
    assert machine.currently_selecting.name == STAGE.Bun.name

#sk3395 18-march

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