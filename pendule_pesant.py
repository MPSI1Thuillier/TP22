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
m = 0.0583 # masse
g = 9.81 # cte de pesanteur
l = 0.525 # longeur de la règle
J = 1/3 * m * l**2 # moment d'inertie

# Conditions initiales
theta0 = np.pi / 4
thetap0 = 0

# Fonction du pendule pesant
def pendule(y, t):
    # On extrait les coordonnées
    theta, omega = y

    # On les dérive on fonction du temps
    dtheta = omega
    domega = - (m * g * l / J) * np.sin(theta)
    return (dtheta, domega)

# On résout l'équa diff
t = np.linspace(0, 15, 1001)
solution = odeint(pendule, (theta0, thetap0), t)

# On extrait les coordonnées
theta, omega = solution[:, 0], solution[:, 1]

# On trace
figure, axis = plt.subplots(2)

axis[0].set_title('θ en fonction du temps')
axis[0].plot(t, theta, label="θ(t)")

axis[1].set_title('ω en fonction de θ')
axis[1].plot(theta, omega, label="ω(θ)")

plt.legend()
plt.show()
