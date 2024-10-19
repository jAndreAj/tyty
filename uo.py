import numpy as np
import matplotlib.pyplot as plt
from astropy.coordinates import SkyCoord
from astropy import units as u


# Funzione per creare il grafico della Via Lattea
def plot_milky_way_equatorial():
    # Generiamo punti che simulano la posizione della Via Lattea
    l = np.linspace(0, 360, 1000)  # Longitudine galattica da 0 a 360 gradi
    b = np.linspace(
        -5, 5,
        1000)  # Latitudine galattica, stretta attorno al piano galattico

    # Convertiamo le coordinate galattiche in coordinate equatoriali (ICRS: ascensione retta e declinazione)
    milky_way_coords = SkyCoord(l=l * u.degree,
                                b=b * u.degree,
                                frame='galactic').transform_to('icrs')
    ra = milky_way_coords.ra.wrap_at(
        180 * u.deg).radian  # Ascensione retta (in radianti)
    dec = milky_way_coords.dec.radian  # Declinazione (in radianti)

    # Definiamo una mappa di colori in base alla latitudine galattica
    colors = plt.cm.viridis(
        (b - min(b)) /
        (max(b) - min(b)))  # Mappa di colori in base alla latitudine

    # Creiamo il grafico con proiezione Mollweide
    plt.figure(figsize=(10, 5))
    ax = plt.subplot(111, projection="mollweide")

    # Tracciamo i punti della Via Lattea con colore e dimensione variabili
    scatter = ax.scatter(ra,
                         dec,
                         s=2 + np.abs(b),
                         c=colors,
                         alpha=0.75,
                         edgecolor='none')

    # Aggiungiamo una griglia e la personalizziamo
    ax.grid(True, color='white', linestyle='--', linewidth=0.5, alpha=0.6)

    # Aggiungiamo etichette per la griglia (ascensione retta e declinazione)
    ax.set_xticklabels([
        '14h', '16h', '18h', '20h', '22h', '0h', '2h', '4h', '6h', '8h', '10h'
    ],
                       fontsize=10)
    ax.set_yticklabels([
        '-75°', '-60°', '-45°', '-30°', '-15°', '0°', '15°', '30°', '45°',
        '60°', '75°'
    ],
                       fontsize=10)

    # Titolo migliorato
    plt.title('Simulazione della Via Lattea in Coordinate Equatoriali',
              pad=20,
              fontsize=14,
              color='white')

    # Impostiamo un colore di sfondo scuro per un effetto visivo migliore
    ax.set_facecolor("black")

    # Mostriamo il grafico con un effetto visivo di alto contrasto
    plt.tight_layout()
    plt.show()


# Esegui la funzione per creare il grafico
plot_milky_way_equatorial()
