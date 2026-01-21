import matplotlib.pyplot as plt
import numpy as np
from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
iris = fetch_ucirepo(id=53) 
  
# data 
X = iris.data.features[["petal length"]]
y = iris.data.features[["petal width"]]
species = iris.data.targets
  
# metadata 
print(iris.metadata) 
  
# variable information 
print(iris.variables) 

# Plot with different colors for each species
colors = ['red', 'green', 'blue']
unique_species = species.iloc[:, 0].unique()
for i, species_name in enumerate(unique_species):
    mask = species.iloc[:, 0] == species_name
    plt.plot(X[mask].values.flatten(), y[mask].values.flatten(), 
             marker='o', ls='None', color=colors[i], label=species_name)

plt.xlabel("petal length cm")
plt.ylabel("petal width cm")
plt.title("Iris Dataset: Petal Length vs Width by Species")
plt.legend()
plt.grid(True)
plt.show()