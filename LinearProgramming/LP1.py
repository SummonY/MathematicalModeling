#!/usr/bin/python
#-*- coding:utf-8 -*-

from pulp import *

prob = LpProblem('lp', LpMaximize)

x1 = LpVariable('x1', lowBound = 0)
x2 = LpVariable('x2', lowBound = 0)
x3 = LpVariable('x3', lowBound = 0)

prob += 2 * x1 + 3 * x2 - 5 * x3

prob += x1 + x2 + x3 == 7
prob += 2 * x1 - 5 * x2 + x3 >= 10
prob += x1 + 3 * x2 + x3 <= 12

prob.solve()

for v in prob.variables():
    print v.name, '=', v.varValue

print 'objective =', value(prob.objective)
