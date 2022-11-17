#Creado por CAGM
Feature: Ganador del juego
  Se corroborará el ganador o se informará un empate.
  # Opciones:
  # PI -> Piedra.
  # TI -> Tijera.
  # PA -> Papel.

  Scenario : Gana el jugador con Piedra
    Given que ingresó la opción PI
    When se lo solicitó el sistema
    Then la máquina sacó TI

  Scenario : Gana el jugador con Tijera
    Given que ingresó la opción TI
    When se lo solicitó el sistema
    Then la máquina sacó PA

  Scenario : Gana el jugador con Papel
    Given que ingresó la opción PA
    When se lo solicitó el sistema
    Then la máquina sacó PI

  Scenario : Hay empate
    Given que ingresó la opción correspondiente
    When se lo solicitó el sistema
    Then la máquina sacó la misma opción