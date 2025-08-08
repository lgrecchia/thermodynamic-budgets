# Thermodynamic Budgets Cookbook

<img src="thumbnails/thumbnail.png" alt="thumbnail" width="300"/>

[![nightly-build](https://github.com/ProjectPythia/cookbook-template/actions/workflows/nightly-build.yaml/badge.svg)](https://github.com/ProjectPythia/cookbook-template/actions/workflows/nightly-build.yaml)
[![Binder](https://binder.projectpythia.org/badge_logo.svg)](https://binder.projectpythia.org/v2/gh/ProjectPythia/cookbook-template/main?labpath=notebooks)
[![DOI](https://zenodo.org/badge/475509405.svg)](https://zenodo.org/badge/latestdoi/475509405)

_See the [Cookbook Contributor's Guide](https://projectpythia.org/cookbook-guide) for step-by-step instructions on how to create your new Cookbook and get it hosted on the [Pythia Cookbook Gallery](https://cookbooks.projectpythia.org)!_

This Project Pythia Cookbook is a step-by-step guide for how to calculate components of the moist static energy and ocean heat content budgets.

## Motivation

This cookbook will help you understand the mathematical derivation of thermodynamic budgets, common simplifications of certain terms and how to include boundary conditions. It will also demonstrate how to calculate each term from real data and what the mathematical equations look like from a coding perspective. 

## Authors

[Lucy Recchia](https://github.com/lgrecchia).

### Contributors

<a href="https://github.com/ProjectPythia/thermodynamic-budgets/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ProjectPythia/thermodynamic-budgets" />
</a>

## Structure

This cookbook is broken into two main sections:

### Moist static energy budget 

Walkthrough example showing the mathematical derviation of each term and how to calculate this from real data. The moist static energy budget is comprised of horizontal advection, vertical advection, surface fluxes and radiative terms.

### Ocean heat content budget 

 Walkthrough example showing the mathematical derviation of each term and how to calculate this from real data. The ocean heat content budget is comprised of horizontal advection, vertical advection, horizontal diffusion, vertical diffusion, surface fluxes and radiative terms.

## Running the Notebooks

You can either run the notebook using [Binder](https://binder.projectpythia.org/) or on your local machine.

### Running on Binder

The simplest way to interact with a Jupyter Notebook is through
[Binder](https://binder.projectpythia.org/), which enables the execution of a
[Jupyter Book](https://jupyterbook.org) in the cloud. The details of how this works are not
important for now. All you need to know is how to launch a Pythia
Cookbooks chapter via Binder. Simply navigate your mouse to
the top right corner of the book chapter you are viewing and click
on the rocket ship icon, (see figure below), and be sure to select
“launch Binder”. After a moment you should be presented with a
notebook that you can interact with. I.e. you’ll be able to execute
and even change the example programs. You’ll see that the code cells
have no output at first, until you execute them by pressing
{kbd}`Shift`\+{kbd}`Enter`. Complete details on how to interact with
a live Jupyter notebook are described in [Getting Started with
Jupyter](https://foundations.projectpythia.org/foundations/getting-started-jupyter).

Note, not all Cookbook chapters are executable. If you do not see
the rocket ship icon, such as on this page, you are not viewing an
executable book chapter.


### Running on Your Own Machine

If you are interested in running this material locally on your computer, you will need to follow this workflow:

1. Clone the `https://github.com/ProjectPythia/thermodynamic-budgets` repository:

   ```bash
    git clone https://github.com/ProjectPythia/thermodynamic-budgets.git
   ```

1. Move into the `thermodynamic-budgets` directory
   ```bash
   cd thermodynamic-budgets
   ```
1. Create and activate your conda environment from the `environment.yml` file
   ```bash
   conda env create -f environment.yml
   conda activate thermodynamic-budgets
   ```
1. Move into the `notebooks` directory and start up Jupyterlab
   ```bash
   cd notebooks/
   jupyter lab
   ```
