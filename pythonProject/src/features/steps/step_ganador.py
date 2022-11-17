from behave import *

from src.functions.functions import gano_el_jugador


@given("que ingresó la opción PI")
def step_impl(context):
    assert

@when("se lo solicitó el sistema")
def step_impl(context):
    gano_el_jugador(context)

@then("la máquina sacó TI")
def step_impl(context):
    pass


@given("que ingresó la opción TI")
def step_impl(context):
    assert

@when("se lo solicitó el sistema")
def step_impl(context):
    gano_el_jugador(context)

@then("la máquina sacó PA")
def step_impl(context):
    pass


@given("que ingresó la opción PA")
def step_impl(context):
    assert

@when("se lo solicitó el sistema")
def step_impl(context):
    gano_el_jugador(context)

@then("la máquina sacó PI")
def step_impl(context):
    pass


@given("que ingresó la opción correspondiente")
def step_impl(context):
    assert

@when("se lo solicitó el sistema")
def step_impl(context):
    gano_el_jugador(context)

@then("la máquina sacó la misma opción")
def step_impl(context):
    pass