import matplotlib.pyplot as plt
import numpy as np
from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
iris = fetch_ucirepo(id=53) 
  
# data 
X = iris.data.features[["petal length"]]
y = iris.data.targets
  
# metadata 
print(iris.metadata) 
  
# variable information 
print(iris.variables) 

plt.plot(X.values.flatten(), y.values.flatten(), marker='o', ls='None', color='b')
plt.xlabel("petal length cm")
plt.ylabel("Class")
plt.title("Iris Dataset: Petal Length vs Class")
plt.grid(True)
plt.show()