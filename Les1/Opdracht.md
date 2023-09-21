# Oefeningen Labo 1 en 2

## Agents

- Wat is een agent ? Wat is rationaliteit ?

Vraag1

      Een agent is een reëel of digitaal systeem dat informatie binnenkrijgt uit zijn omgeving.
      Op basis van interne logica zal deze dan een actie of een set van acties uitvoeren.
      Deze worden uitgevoerd op basis van actuatoren. Het doel: De situatie verbeteren.


Vraag2

      Rationaliteit betekent in dit geval dat een agent voor elke input een actie heeft die resulteert
      in een maximale output. Om een output te score heb je dan een meetstaaf voor performatie nodig.
      Dit noemen we de doelfunctie. Het is natuurlijk vanzelfsprekend dat als men elke keer een maximale 
      output moeten vinden dat dit zorgt voor een hoge werklast. We kunnen dus beter een historiek inbouwen.  

- Stel voor volgende taken een POAS beschrijving op

    (a) Een gymnastische oefening uitvoeren op een trampoline.  
          P: score van jury
          O: Atletiek veld?
          A: De spieren (gereedschap)
          S: Evenwichtsorgaan, ogen, tastzin
    (b) De oceanen ontdekken. 
          P: % oceaan ontdekt
          O: Oceaan
          A: Motor van boot, Zeil van boot
          S: Kaart, gps?
    (c) Voetbal spelen.  
          P: Aantal goals
          O: Voetbal veld
          A: De spieren
          S: Ogen, Evenwichtsorgaan, Oren
    (d) Automatisch gebruikte AI boeken vinden op het internet.  
          P: 
          O: 
          A: 
          S:
    (e) Tennis spelen tegen een muur.  
          P: 
          O: 
          A: 
          S:
    (f) Een hoge sprong uitvoeren.  
          P: 
          O: 
          A: 
          S:
    (g) Op een veiling bieden op een item.
          P: 
          O: 
          A: 
          S:
- Veronderstel dat we een thermostaat hebben die de verwarming opzet wanneer de temperatuur minstens 3 graden kouder is dan een instelling en die de verwarming afzet wanneer de temperatuur minstens 3 graden warmer is dan die instelling. Is deze thermostaat een eenvoudige reflex agent, een model-based reflex agent of een goal-based agent? 
- Bepaal voor volgende probleem een model-based reflex agent, die dus een interne state heeft, een transition model, sensormetingen kan doen en de state kan updaten. Het probleem is een tegenvloer in een woonkamer die moet worden gestofzuigd door een robotstofzuiger. Je krijgt volgende informatie:
    - Een tegel is altijd vuil of proper.
    - De stofzuiger is exact even groot en kuist precies 1 tegel
    - De stofzuiger kan ofwel zich verplaatsen, ofwel stofzuigen, ofwel blijven staan
    - De stofzuiger kent de ruimte (10 op 5 tegels) en weet dat hij in de hoek start, bij het laadstation
    - Uitbreidingen:
        - tegels zijn na 7 dagen niet poetsen zeker vuil
        - er kunnen obstakels op een tegel staan (de robot kan die met een bumper voelen, niet van ver zien)
        - de stofzuiger kent de ruimte niet
- Implementeer in Python een klasse die de interne state van deze robot voorsteld en alles wt de robot nodig heeft om deze ruimte te kuisen. Voorzie een methode `clean()`, `move_down()`, `clean_tile()`, ... Bedenk een goede strategie. Er zijn heel simpele strategiëen die zullen werken. Voorzie wat testcode om je werk te demonstreren.

## Conda installeren
- Alle codefiles voor dit vak hou je best bij in 1 lokale folder, die al dan niet gesynchroniseerd kan worden met Github of dergelijke
- Creëer een nieuwe conda omgeving voor dit vak, genaamd `ai_programming_env`. Zoek zelf hoe je dit op een terminal binnen VSCode kan doen.
- Test deze omgeving door ze te activeren, en python erin op te starten
- In deze omgeving kun je nu bepaalde packages installeren op het moment dat je deze nodig hebt
- Schrijf de details van deze conda omgeving weg naar een file, met het commando `conda env export > environment.yml`. Dit is good practise, want als iemand anders nu van Github je code wil gebruiken, heeft die ineens de conda file met exact de juiste requirements.

## Self Driving car
Bouw je eigen model-based reflex agent (in Python) en pas het toe op het volgende probleem. Je agent moet zijn voorligger volgen op 10m afstand. Ga ervan uit dat er een LIDAR sensor ter beschikking is die als perceptie op elk moment de afstand toont tot je voorligger. De actuatoren ter beschikking geven de mogelijkheid om extra gas bij te geven of te remmen. Je moet remmen als de tijd tot collisie (botsing) minder dan 5 seconden is.

## Sortering

- Implementeer een klasse in python die lijsten kan sorteren. Opgelet, je schrijft zelf de sorting, en maakt dus geen gebruik van interne sorteringslibraries.
    - implementeer Insertion Sort: Hierbij wordt elk nieuw item dat wordt toegevoegd aan een lijst meteen op de juiste plaats gestoken, zo wordt een lijst item per item gesorteerd
    - implementeer Quick Sort. Bij Quick Sort kies je uit je ongeordende lijst een element (de zogenaamde pivot), en je maakt nu 2 deellijsten: de items kleiner dan de pivot, en de items groter dan de pivot. Vervolgens ga je deze 2 deellijsten op dezelfde manier ordenen.
    - vergelijk voor lijsten met 10, 100, 1000 en 100 000 items de snelheid van sortering tussen beiden.

