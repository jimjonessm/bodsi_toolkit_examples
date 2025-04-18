"""
 This example demonstrates how to frame the system identification problem 
 using the "bodsi" class, which aims to provide solutions, in the form of 
 functions, for each step of the system identification process, such as 
 generating candidate terms, structure detection, parameter estimation in 
 an unbiased manner through a bi-objective estimator, model simulation, 
 and dynamic and static validation.

The data used in this example is real and was collected from a real variable 
reluctance heater where the input and output are normalized in per unit (p.u.).

 The functions presented here are based on the work: 
 Márcio F.S. Barroso, Ricardo H.C. Takahashi, Luis A. Aguirre, 
 Multi-objective parameter estimation via minimal correlation criterion, 
 Journal of Process Control, Volume 17, Issue 4, 2007, Pages 321-332, 
 ISSN 0959-1524. https://doi.org/10.1016/j.jprocont.2006.10.005.
"""


# Import necessary functions from numpy and matplotlib
from numpy import mean
from matplotlib.pyplot import figure, subplot, plot, title, ylabel, xlabel, legend, grid, box, close, suptitle
from os import system
from scipy.io import loadmat

# Import functions from bodsi
from bodsi_toolkit import (
    generateCandidateTerms, removeClusters, sortByERR, AkaikeInformationCriterion,
    getClusters, buildRegressorMatrix, buildStaticMatrix, buildMapping,
    generateParetoSet, correlationDecisionMaker, getInfo, simulateModel,
    displayModel, buildStaticModel, displayStaticModel, rmse, correla, 
    correlationFunction
)

# Clears variables and closes all plots (Python equivalent for MATLAB commands)
system('cls')
close('all')

# Load the identification and validation data, 
#dynamic and static (only identification)
data = loadmat('Heater_dynamic_dataset.mat')
datas = loadmat('Heater_static_dataset.mat')
ti = data['ti'].flatten()
ui = data['ui'].flatten()
yi = data['yi'].flatten()
tv = data['tv'].flatten()
uv = data['uv'].flatten()
yv = data['yv'].flatten()
u = datas['u'].flatten()
y = datas['y'].flatten()


# Plot real data
figure(1)
suptitle("Real Data")

# Subplot with input data
subplot(2, 1, 1)
plot(ti, ui, 'r', label="Identification Data")
plot(tv, uv, 'b', label="Validation Data")
title("Input and Output Data")
ylabel("u[k]")
legend()
grid(True)
box(True)

# Subplot with output data
subplot(2, 1, 2)
plot(ti, yi, 'r', label="Identification Data")
plot(tv, yv, 'b', label="Validation Data")
ylabel("y[k]")
xlabel("k[s]")
legend()
grid(True)
box(True)

# Determines the conditions for generating candidate terms
nonlinearityDegree = 2
delay_y = 2
delay_u = 2
N = 4000

# Generates the candidate process terms
Model, Tterms, term_type = generateCandidateTerms(nonlinearityDegree, [delay_y, delay_u])
Model = removeClusters(Model, 2, 0)
#Model = removeClusters(Model, 1, 1)
#Model = removeClusters(Model, 0, 0)

# Performs structure detection using AKAIKE and ERR criteria
Model, ERR = sortByERR(Model, ui, yi)
f, mint = AkaikeInformationCriterion(Model, ui, yi)
Model = Model[:mint, :]

# Sets up the bi-objective problem
clusters = getClusters(Model)
P = buildRegressorMatrix(Model, ui, yi)
E = buildStaticMatrix(clusters, u, y)
A = buildMapping(Model)

# Generates the Pareto-Optimal set and makes a decision
PARAMETERS, VAL = generateParetoSet(P, E, A, yi, y, N, 1)
Parameters, correl, p, r = correlationDecisionMaker(Model, PARAMETERS, uv, yv)

# Simulates the identified model
_, maxDelay, _, _ = getInfo(Model)
yhat = simulateModel(Model, Parameters, uv, yv[:maxDelay])
eq = displayModel(Model, Parameters, 1)

# Builds the static model
staticModel = buildStaticModel(Model, Parameters)
yest, eqest = displayStaticModel(staticModel, u, y, 1)

# Plot comparison between real dynamic data and simulated data
figure()
plot(tv, yv, 'b', label="Real Data")
plot(tv, yhat, 'r-.', label="Simulated Data")
title("Validation Data Set")
xlabel("t[k]")
ylabel("y[t]")
legend()
grid(True)
box(True)

# Plot comparison between static data and simulated data
figure()
plot(u, y, 'b*', label="Real Data")
plot(u, yest, 'r-.', label="Simulated Data")
title("Static Data Set")
xlabel("u")
ylabel("y")
legend()
grid(True)
box(True)

# Analyze errors and display results
R = rmse(yv, yhat)
res = correla(y, yest)
H, Y = correlationFunction(yv - yhat, len(yv) - 1, 0)
resid = mean(Y)

print()
print("Analysis of the error between real data and the free simulation of the model:")
print(f"The RMSE (R) value is {R:.3f}")
print("Analysis of the autocorrelation of validation residuals")
print(f"The Correlation (r) value is {resid:.3f}")
print("Analysis of the autocorrelation between the static model and static data")
print(f"The Correlation (r) value is {res:.3f}")

