from behave import *

from src.functions.functions import jugar


@given("que es solicitado por el sistema")
def step_impl(context):
    assert

@when("se introducen las sílabas de \+(.*)")
def step_impl(context):
    jugar(context)

@then("las coincidencias esperadas 'context'")
def step_impl(context):
    pass