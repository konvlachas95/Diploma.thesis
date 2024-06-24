# Diploma thesis on the effects of socioethical norms on multiagent systems

This project simulates a bargaining game on a 2D lattice graph with a von Neumann neighborhood structure.
The simulations involve various parameters for the interactions of the agents and generate various plots to visualize the results.
One such parameter (alpha) models a norm and by adding or altering it we derive to certain conclusion concerning its effects on the agents population.

## Installation

To install the necessary dependencies, run:
```bash
pip install -r requirements.txt
```

## Usage

To run the simulations, execute the `simulations.py` script:
```bash
python simulations.py
```

## Project Structure

- `games.py`: Contains the `bargain` class which handles the game simulation logic.
- `graphs.py`: Contains functions for generating and manipulating graphs.
- `simulations.py`: Main script to run simulations with various parameters.
- `requirements.txt`: Lists all the dependencies required to run the project.

## Parameters

The following parameters can be adjusted in `simulations.py`:
- `betas`: List of beta values.
- `alphas`: List of alpha values.
- `lamdas`: List of lambda values.
- `J0_vals`: Initial J values.

Other stable parameters include:
- `n`: Size of the lattice (default is 21).
- `gamma`: Gamma value (default is 0.1).
- `N_tags`: Number of tags (default is 1).
- `N_epochs`: Number of epochs (default is 1000).
- `num_runs`: Number of runs (default is 1).
- `lattice`: Type of lattice (default is "lattice_von_neumann").

## Results

The simulation generates various plots:
- Graph plots
- Statistics plots
- Simplex plots
- Bar plots

## Credits

This project is based on work by George Arampatzis (garampat at ethz.ch) and Pantelis Vlachas (pvlachas at ethz.ch) at CSElab, ETH Zurich, 2020.
