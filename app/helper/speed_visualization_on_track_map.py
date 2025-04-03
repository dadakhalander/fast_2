import streamlit as st
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib.collections import LineCollection


def render(target_lap):
    fig, ax = plt.subplots(figsize=(8.0, 4.9))
    tel = target_lap.get_telemetry()
    x = np.array(tel['X'].values)
    y = np.array(tel['Y'].values)
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    speed = tel['Speed'].to_numpy().astype(float)
    cmap = mpl.cm.plasma

    norm = plt.Normalize(speed.min(), speed.max())
    lc_comp = LineCollection(segments, norm=norm, cmap=cmap)
    lc_comp.set_array(speed)
    lc_comp.set_linewidth(4)

    fig.gca().add_collection(lc_comp)
    ax.axis('equal')
    ax.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

    fig.colorbar(mappable=lc_comp, label='Speed', boundaries=np.arange(speed.min(), speed.max()))
    st.pyplot(fig)
