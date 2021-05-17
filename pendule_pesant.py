#
# Code basé sur l'exemple du TP précédent
# (exemple_oscillateur.py)
# https://github.com/MPSI1Thuillier/TP21
#

# Imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib.widgets import Slider

# Définition des constantes
m = 58.3 # masse
g = 9.81 # cte de pesanteur
l = 0.525 # longeur de la règle
J = 1/3 * m * l**2 # moment d'inertie
mu = 2 # ??? (constante qui fait que le pendule ralenti)

# Conditions initiales
theta0 = 1
thetap0 = 20

# Réglage des graphs
figure, axis = plt.subplots(2)
plt.subplots_adjust(bottom=0.2)

# Sliders (pour changer les réglages)
ax_theta0 = plt.axes([0.25, 0.1, 0.65, 0.03])
slider_theta0 = Slider(ax_theta0, 'θ(t=0)', 0, 5, valinit=theta0)

ax_thetap0 = plt.axes([0.25, 0.05, 0.65, 0.03])
slider_thetap0 = Slider(ax_thetap0, 'ω(t=0)', 0, 30, valinit=thetap0)

# Fonction du pendule pesant
def pendule(y, t):
    # On extrait les coordonnées
    theta, omega = y

    # On les dérive on fonction du temps
    dtheta = omega
    domega = - (mu / J * omega) - (m * g * l / J * np.sin(theta))
    return (dtheta, domega)

def calculer(val):
    # Récupère les valeurs
    theta0 = slider_theta0.val
    thetap0 = slider_thetap0.val

    # On résout l'équa diff
    t = np.linspace(0, 15, 1001)
    solution = odeint(pendule, (theta0, thetap0), t)

    # On extrait les coordonnées
    theta, omega = solution[:, 0], solution[:, 1]

    # On trace
    axis[0].clear()
    axis[0].set_title('θ en fonction du temps')
    axis[0].plot(t, theta)

    axis[1].clear()
    axis[1].set_title('ω en fonction de θ')
    axis[1].plot(theta, omega)

# Ajout de la méthode de calcul aux sliders
slider_theta0.on_changed(calculer)
slider_thetap0.on_changed(calculer)

# On calcul la trajectoire initiale
calculer(None)

# On affiche
plt.show()
