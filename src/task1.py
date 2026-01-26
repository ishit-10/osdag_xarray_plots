import xarray as xr
import matplotlib.pyplot as plt

CENTRAL = [15, 24, 33, 42, 51, 60, 69, 78, 83]


def make_sequence(i_vals, j_vals):
    seq = []
    for i, j in zip(i_vals, j_vals):
        seq.append(i)
        seq.append(j)
    return seq


def plot_task1():
    ds = xr.open_dataset("data/xarray_data.nc")

    # Extracting Mz_i, Mz_j, Vy_i, Vy_j
    Mz_i = [ds["forces"].sel(Element=e, Component="Mz_i").item() for e in CENTRAL]
    Mz_j = [ds["forces"].sel(Element=e, Component="Mz_j").item() for e in CENTRAL]

    Vy_i = [ds["forces"].sel(Element=e, Component="Vy_i").item() for e in CENTRAL]
    Vy_j = [ds["forces"].sel(Element=e, Component="Vy_j").item() for e in CENTRAL]

    bmd = make_sequence(Mz_i, Mz_j)
    sfd = make_sequence(Vy_i, Vy_j)
    x = list(range(len(bmd)))

    # BMD (Bending Moment Diagram)
    plt.figure(figsize=(10, 4))
    plt.plot(x, bmd)
    plt.title("Bending Moment Diagram – Central Longitudinal Girder")
    plt.xlabel("Position")
    plt.ylabel("Mz")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("outputs/task1_bmd.png")
    plt.close()

    # SFD (Shear Force Diagram)
    plt.figure(figsize=(10, 4))
    plt.plot(x, sfd, color="red")
    plt.title("Shear Force Diagram – Central Longitudinal Girder")
    plt.xlabel("Position")
    plt.ylabel("Vy")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("outputs/task1_sfd.png")
    plt.close()

    print("Task-1 completed.")
