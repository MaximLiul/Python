# -*- coding: utf-8 -*-
#   расчет уровней энергий для одного кубита
#   для e=1 d=2.5 

from sympy import *
init_printing(use_latex=True)
e, E, d = symbols('e, E, d')
M=Matrix([[e + 2*E, d],
          [d, - e + 2*E]])
pprint(M)
det = M.det()
det_collected = collect(det, E)
print(det_collected)
det_subs = det_collected.subs(d,2.5)
print(det_subs)
print(det_subs.subs(e,1))

print(nroots(det_subs.subs(e,1), 25))
#111

print(det_subs.subs([(e,1),(E,1.346291201783626007812678)]))

# -1.346291201783626007812678
# 1.346291201783626007812678
