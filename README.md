This repository contains my code for Osdag : Software Development Screening Task.
The goal is to extract internal force data from an Xarray dataset and generate both 2D and 3D structural response diagrams for a bridge grillage model.
The project includes **Shear Force Diagrams (SFD)** and **Bending Moment Diagrams (BMD)** for the main longitudinal girder and all five girders of the bridge system.

# The Implementation involves:
* Reading internal forces/moments stored in an Xarray dataset
* Mapping element IDs to node coordinates and member connectivity
* Constructing 2D diagrams for bending moment and shear force
* Generating interactive 3D extruded visualizations that resemble MIDAS Civil post-processing


# Project Structure

osdag_plots/
│
├── data/
│   ├── xarray_data.nc        
│   ├── node.py               
│   ├── element.py            
│
├── src/
│   ├── task1.py              
│   ├── task2.py              
│
├── outputs/                  # Generated plots (PNG for 2D deigns + HTML for 3D designs) (manually added screenshots of 3D visualizations by running HTML)
│
├── main.py 
├── requirements.txt
└── README.md


# Detailed Implementation

## Task 1: SFD and BMD from Xarray dataset for Central Longitudinal Girder
The central girder consists of the following elements:
`[15, 24, 33, 42, 51, 60, 69, 78, 83]`
From the Xarray dataset (xarray_data.nc), the following force components are extracted:
- Mz_i, Mz_j → Bending Moment
- Vy_i, Vy_j → Shear Force

Using these:
* i-end and j-end values are merged into continuous sequences
* Matplotlib plots clear 2D diagrams
* Outputs are saved as:
  - outputs/task1_bmd.png
  - outputs/task1_sfd.png


## Task2: 3D Extruded SFD & BMD for All Girders
For each girder (G1 to G5), the script:
* Uses element connectivity from element.py
* Retrieves 3D coordinates from node.py
* Extracts internal forces from the Xarray dataset
* Creates vertical extrusion of Mz or Vy:
  `z_ex = [z1 + value_i, z2 + value_j]`
* Plots extruded beam segments using Plotly 3D
* Saves fully interactive diagrams:
  - outputs/task2_bmd.html
  - outputs/task2_sfd.html
* Run these .html files in browser to view the interactive diagram


# Running the project

## Install Dependencies
`pip install -r requirements.txt`

## Run Both Tasks
`python3 main.py`

# Outputs will be stored in outputs/
  



