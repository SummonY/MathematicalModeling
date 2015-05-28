#!/usr/bin/python
#-*- coding:utf-8 -*-

import pulp

prob = pulp.LpProblem('LP2', pulp.LpMaximize)

x1 = pulp.LpVariable('x1', lowBound = 0)
x2 = pulp.LpVariable('x2', lowBound = 0)

prob += 4 * x1 + 3 * x2

prob += 2 * x1 + x2 <= 10
prob += x1 + x2 <= 8
prob += x2 <= 7

prob.solve()

for v in prob.variables():
    print v.name, '=', v.varValue

print 'objective =', pulp.value(prob.objective)
