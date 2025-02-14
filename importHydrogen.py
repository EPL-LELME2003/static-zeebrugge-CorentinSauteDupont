Corentin Dupont
import pyomo.environ as pyo

# Create a Pyomo model
model = pyo.ConcreteModel()


# Define model parameters
model.boat_capacity = pyo.Param

# Define model variables
model.Nbr_boats_CH4 = pyo.Var(within = pyo.NonNegativeReals)
model.Nbr_boats_NH3 = pyo.Var(within = pyo.NonNegativeReals) 


# Define the objective functions
model.obj = pyo.Objective(expr = 2*model. × 1 + 4*model. × 2, sense = pyo.maximize) 

# Define the constraints
Nbr_boats_CH4 + Nbr_boats_NH3 = 100


# Specify the path towards your solver (gurobi) file
solver = pyo.SolverFactory('C:\Users\dupti\gurobi.lic')
sol = solver.solve(model)

# Print here the number of CH4 boats and NH3 boats
##########################################
############ CODE TO ADD HERE ############
##########################################
