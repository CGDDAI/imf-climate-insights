"""
viz.py — helpers de visualización (estilos y utilidades).
"""
import matplotlib.pyplot as plt

def set_default_style():
    plt.rcParams["figure.dpi"] = 120
    plt.rcParams["axes.grid"] = True
    plt.rcParams["figure.autolayout"] = True
