#Creado por CAGM
Feature: Parametro ingresado
  Se validará que la data ingresada corresponda a la establecida en el sistema.

  Scenario Outline: Ingresar correctamente el parámetro
    Given que es solicitado por el sistema
    When se introducen las sílabas de "<opciones>"
    Then las coincidencias esperadas "<coincidencia>"
    And continua el juego

    Examples: Juego
      |opciones   |coincidencias|
      |pi         |piedra       |
      |pa         |papel        |
      |ti         |tijera       |