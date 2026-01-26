import xarray as xr
import plotly.graph_objects as go

from data.node import nodes
from data.element import members

GIRDERS = {
    "G1": [13, 22, 31, 40, 49, 58, 67, 76, 81],
    "G2": [14, 23, 32, 41, 50, 59, 68, 77, 82],
    "G3": [15, 24, 33, 42, 51, 60, 69, 78, 83],
    "G4": [16, 25, 34, 43, 52, 61, 70, 79, 84],
    "G5": [17, 26, 35, 44, 53, 62, 71, 80, 85]
}


def get_value(ds, e, component):
    """Fetch correct value from the dataset."""
    return ds["forces"].sel(Element=e, Component=component).item()


def plot_3d(value_key, title, save_path):
    ds = xr.open_dataset("data/xarray_data.nc")
    fig = go.Figure()

    comp_i = value_key + "_i"
    comp_j = value_key + "_j"

    for girder, elems in GIRDERS.items():
        for e in elems:
            n1, n2 = members[e]

            x1, y1, z1 = nodes[n1]
            x2, y2, z2 = nodes[n2]

            vi = get_value(ds, e, comp_i)
            vj = get_value(ds, e, comp_j)

            z_ex = [z1 + vi, z2 + vj]

            fig.add_trace(go.Scatter3d(
                x=[x1, x2],
                y=[y1, y2],
                z=z_ex,
                mode="lines",
                line=dict(width=6),
                showlegend=False
            ))

    fig.update_layout(
        title=title,
        scene=dict(
            xaxis_title="X",
            yaxis_title="Y",
            zaxis_title=value_key
        )
    )

    fig.write_html(save_path)
    print("Saved:", save_path)


def run_task2():
    plot_3d("Mz", "3D Bending Moment Diagram", "outputs/task2_bmd.html")
    plot_3d("Vy", "3D Shear Force Diagram", "outputs/task2_sfd.html")
    print("Task-2 completed.")
