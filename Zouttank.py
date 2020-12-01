#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

import numpy as np
import matplotlib
import matplotlib.pyplot as plt


# fysische informatie:
TANK_INHOUD = 100          # liter
CONCENTRATIE_INSTROOM = 0.2 # kg / liter

INSTROOM = 6 / 60           # liter per seconde
INSTROOM_B = 1 / 60          # Instroom IN A VAN B, liter per seconde
UITSTROOM = 4 / 60          # liter per seconde
UITSTROOM_B = 3 / 60          # Uitstroom VAN A NAAR B, liter per seconde

INSTROOM2 = 0 / 60           # liter per seconde
INSTROOM2_A = 3 / 60          # Instroom IN B VAN A, liter per seconde
UITSTROOM2 = 2 / 60          # liter per seconde
UITSTROOM2_A = 1 / 60          # Uitstroom VAN B NAAR A, liter per seconde
    
# Ingevulde instroom/uitstroom voor beide tanks. Worden niet allemaal gebruikt.
constInstroom_1 = CONCENTRATIE_INSTROOM * INSTROOM
instroom_1 = INSTROOM + UITSTROOM2_A          # Wat tank 1 instroomt
instroom_2 = INSTROOM2 + UITSTROOM_B          # Wat tank 2 instroomt
instroom_kg_per_s = CONCENTRATIE_INSTROOM * (INSTROOM + UITSTROOM2_A)
instroom_kg_per_s_2 = CONCENTRATIE_INSTROOM * (INSTROOM2 + UITSTROOM_B)

uitstroom_1 = UITSTROOM + UITSTROOM_B          # Wat tank 1 uitstroomt
uitstroom_2 = UITSTROOM2 + UITSTROOM2_A          # Wat tank 2 uitstroomt
uitstroom_kg_per_s = CONCENTRATIE_INSTROOM * (UITSTROOM + UITSTROOM_B)
uitstroom_kg_per_s_2 = CONCENTRATIE_INSTROOM * (UITSTROOM2 + UITSTROOM2_A)

    
def simLoop(stapgrootte=100):
    # de simulation loop: Deze wordt aangeroepen door de interactive.
    
    DUUR = 3*3600 # 3600 seconden = 1 uur, dus ingesteld op 3 uur
    AANTAL_STAPPEN = stapgrootte
    stapgrootte = DUUR / AANTAL_STAPPEN # in seconden

    # Aanmaken van de twee arrays: tijd en zout. Het zout-array geeft op 
    # ieder tijdstip het aantal kg zout in de tank.
    # We nemen het aantal elementen 1 meer dan het aantal stappen
    tijd = ( stapgrootte * np.arange(AANTAL_STAPPEN + 1) ) / 60
    zout = np.zeros(AANTAL_STAPPEN + 1)
    zout2 = np.zeros(AANTAL_STAPPEN + 1)

    zout[0] = 0 # beginconditie, niet echt nodig hier, maar toch.
    zout2[0] = 20 # beginconditie, hier wel nodig
    
    for stap in range(1, AANTAL_STAPPEN + 1):
        concentratie_t_min1 = zout[stap - 1] / TANK_INHOUD # kg / liter, Zouttank 1
        concentratie_t_min1_2 = zout2[stap - 1] / TANK_INHOUD # kg / liter, Zouttank 2
    
        # Zouttank 1
        zout[stap] = zout[stap - 1] + stapgrootte * (((concentratie_t_min1_2 * INSTROOM_B) + constInstroom_1) - concentratie_t_min1 * uitstroom_1)
    
        # Zouttank 2
        zout2[stap] = zout2[stap - 1] + stapgrootte * ((concentratie_t_min1 * INSTROOM2_A) - concentratie_t_min1_2 * uitstroom_2)
    
    matplotlib.pyplot.plot(tijd, zout/TANK_INHOUD, label='Zouttank 1')
    matplotlib.pyplot.plot(tijd, zout2/TANK_INHOUD, label='Zouttank 2')
    matplotlib.pyplot.legend(('Zouttank 1', 'Zouttank 2'), loc='lower right')
    
    axes = matplotlib.pyplot.gca()
    axes.set_title('Zoutconcentratie in de tank')
    axes.set_xlabel('tijd (minuten)')
    axes.set_ylabel('zout concentratie (kg / liter)')
    matplotlib.pyplot.show()

interact(simLoop, stapgrootte=(1, 175));

