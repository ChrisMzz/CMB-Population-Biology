# CMB Population Biology

Currently contains : 

# 1. Predation models

All of the following exercises are located in `predation`.

## 1-1. Exercise on Budworms

Located in `budworms`.
A Python implementation of the budworm differential system from Session 1 Exercise Sheet, Exercise 1.
You can change the initial condition to view different solutions.

## 1-2. Exercise on Density-Dependent Prey-Predator model

Located in `densitydependence`.
A Python implementation of the density dependent prey predator model from Session 1 Exercise Sheet, Exercise 2.
You can change the initial condition or change some of the many parameters.

## 1-3. Exercise on Rosenzweig-McArthur model

Located in `mcarthur`.
A Python implementation of the Rosenzweig-McArthur model suggested in Session 1 Exercise Sheet, Exercise 3.
I don't fully know how this one works to be honest, try and change the initial condition but it seems to look good only for specific starting point. I included one that the professor chose in his code, but I have no idea how to find others.

## 1-4. Exercise on Food Chain

Located in `food_chain`.
A Python implementation of the food chain differential equations system from Session 1 Exercise Sheet, Exercise 4.
You can change the number of individuals, their starting conditions (in the list comprehension), and a few of the parameters. The exercise seems to want to change the value of `I`. I haven't done this but you can have fun with it. Rainbow colours and figure spacing are automatically taken care of.


## On the limitations of Liebig's law of the minimum

Based on the work by Jef Huisman and Franz J. Weissing available [here](https://www.math.utah.edu/~golden/resources/julie/Huisman_Nature_1999.pdf), I'm currently writing code to simulate coexisting species competing for resources such that the number of species exceeds the number of limiting resources, which seems to be only possible because the base state of the system does not converge to an equilibrium.

Currently I only have a working version for Figure 1c, but I will try to generate the other figures using the information they provide, and might play around with some parameters, possibly in another file.


# SIR Model

An implementation of the SIR model was included in `sir_model`. You can run `sir_tests.py` to experiment with it, read my docs to see how to use the `SIR` class I wrote.

