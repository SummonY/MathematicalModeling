#!/usr/bin/python
#-*- coding:utf-8 -*-

import pulp

prob = pulp.LpProblem('IP1', pulp.LpMinimize)

#x1 = pulp.LpVariable('x1', lowBound = 0)
#x2 = pulp.LpVariable('x2', lowBound = 0)

x1 = pulp.LpVariable('x1', lowBound = 0, cat = pulp.LpInteger)
x2 = pulp.LpVariable('x2', lowBound = 0, cat = pulp.LpInteger)

prob += x1 + x2
prob += 2 * x1 + 4 * x2 == 6

prob.solve()

for v in prob.variables():
    print v.name, '=', v.varValue

print 'objective =', pulp.value(prob.objective)
