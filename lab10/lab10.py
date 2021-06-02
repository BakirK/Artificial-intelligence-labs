import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definisanje ulaza i izlaza
hrana = ctrl.Antecedent(np.arange(0, 11, 1), 'hrana')
usluga = ctrl.Antecedent(np.arange(0, 11, 1), 'usluga')
napojnica = ctrl.Consequent(np.arange(0, 51, 1), 'napojnica')

# Automatsko dodavanje funkcija pripadnosti
# pomocu automf funkcije (3, 5, ili 7 funkcija pripadnosti)
# hrana.automf(3)
# usluga.automf(3)

hrana['losa'] = fuzz.trimf(hrana.universe, [0, 2, 4])
hrana['prihvatljiva'] = fuzz.trapmf(hrana.universe, [2, 4, 6, 8])
hrana['odlicna'] = fuzz.trimf(hrana.universe, [6, 8, 10])

usluga['losa'] = fuzz.trimf(usluga.universe, [0, 2, 4])
usluga['prihvatljiva'] = fuzz.trapmf(usluga.universe, [2, 4, 6, 8])
usluga['odlicna'] = fuzz.trimf(usluga.universe, [6, 8, 10])

# Rucno pravljenje funkcija pripadnosti
napojnica['mala'] = fuzz.trimf(napojnica.universe, [0, 0, 25])
napojnica['srednja'] = fuzz.trimf(napojnica.universe, [0, 25, 50])
napojnica['velika'] = fuzz.trimf(napojnica.universe, [25, 50, 50])

# Definisanje pravila
# Ona se definišu pomoću metode ctrl.Rule te se u prvi argument šalje
# IF dio, a u drugi THEN dio
p1 = ctrl.Rule(hrana['losa'] | usluga['losa'], napojnica['mala'])
p2 = ctrl.Rule(usluga['prihvatljiva'], napojnica['srednja'])
p3 = ctrl.Rule(usluga['odlicna'] | hrana['odlicna'], napojnica['velika'])

# Sada se jednostavno moze kreirati sistem upravljanja
sistem = ctrl.ControlSystem([p1, p2, p3])
# Kako bi se sistem koristio, mora se prevesti u simulaciju
sistemSim = ctrl.ControlSystemSimulation(sistem)

# Sada se moze izvrsiti simulacija:
sistemSim.input['hrana'] = 8.5
sistemSim.input['usluga'] = 9.5

# Sracunaj izlaz iz fuzzy sistema
sistemSim.compute()
print(sistemSim.output['napojnica'])

hrana.view()
usluga.view()
napojnica['mala'].view()

input()



