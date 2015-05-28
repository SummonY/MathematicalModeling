#!/usr/bin/python
#-*- coding:utf-8 -*-

import pulp

prob = pulp.LpProblem("lpd", pulp.LpMinimize)

x1 = pulp.LpVariable('x1', lowBound = 0)
x2 = pulp.LpVariable('x2', lowBound = 0)
x3 = pulp.LpVariable('x3', lowBound = 0)
x4 = pulp.LpVariable('x4', lowBound = 0)
x5 = pulp.LpVariable('x5', lowBound = 0)

prob += 2 * x1 + 3 * x2 + 5 * x3 + 2 * x4 + 3 * x5

prob += x1 + x2 + 2 * x3 + x4 + 3 * x5 >= 4
prob += 2 * x1 - x2 + 3 * x3 + x4 + x5 >= 3

prob.solve()

for v in prob.variables():
    print v.name, '=', v.varValue

print 'objective =', pulp.value(prob.objective)
