#
# Code basé sur l'exemple du TP précédent
# (exemple_oscillateur.py)
# https://github.com/MPSI1Thuillier/TP21
#

# Imports
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# Définition des constantes
m = 58.3 # masse
g = 9.81 # cte de pesanteur
l = 0.525 # longeur de la règle
J = 1/3 * m * l**2 # moment d'inertie
mu = 2 # ??? (constante qui fait que le pendule ralenti)

# Conditions initiales
theta0 = np.pi / 4
thetap0 = 0

# Fonction du pendule pesant
def pendule(y, t):
    # On extrait les coordonnées
    theta, omega = y

    # On les dérive on fonction du temps
    dtheta = omega
    #domega = - omp**2 * np.sin(theta) # pendule simple
    domega = - (mu / J * omega) - (m * g * l / J * np.sin(theta)) # pendule pesant
    return (dtheta, domega)

# On résout l'équa diff
t = np.linspace(0, 15, 1001)
solution = odeint(pendule, (theta0, thetap0), t)

# On extrait les coordonnées
theta, omega = solution[:, 0], solution[:, 1]

# On trace
#plt.title('θ et ω en fonction du temps')
plt.title('θ en fonction du temps')
plt.plot(t, theta, label="θ(t)")
#plt.plot(t, omega, label="ω(t)")
plt.legend()
plt.show()
