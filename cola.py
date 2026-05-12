

import networkx as nx
import matplotlib.pyplot as plt
import numpy
def collatz(n):
    trayectoria = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        trayectoria.append(n)
    return trayectoria
for n0 in [6, 7, 12, 19]:
    tray = collatz(n0)
    print(f"n = {n0:>3}  |  pasos: {len(tray)-1:>3}  |  maximo: {max(tray):>5}  |  trayectoria: {tray}")
