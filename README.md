# Project description

This project aims to explore and build an accurate, explainable (and potentially a simple) approach to **predict weekly bookings for each hotel over time** for a hotel
chain that operates multiple hotels across Europe.


# Instructions

## Setting up

This section outline how to initialize the runtime environment of the project that are required to run the notebook and the scripts that do model-training, evaluation & forecasting.

This project is built on **Python-3.10.12**. It manages its dependencies using [`pip-tools`](https://pip-tools.readthedocs.io/en/latest/). 

Follow the steps below to set up the environment (assuming you have `python3` and `python3-venv` installed):

1. We set up the virtual environment and install the dependencies. To do this, run the following commands from the root of the project:

```bash
python3 -m venv ./venv
```

2. Activate the virtual environment:

```bash
source ven/bin/activate
```

3. Install `pip-tools`:

```bash
pip3 install pip-tools==7.3.0
```

4. Compile the `txt` files:

```bash
pip-compile requirements/requirements.in && pip-compile requirements/requirements-dev.in
```

4. Install the dependencies:

```bash
pip-sync requirements/requirements-dev.txt
```
Note, in this step we intentionally install the dev dependencies because the packages we use to run the notebook are being treated as dev dependencies.
(This is just an application design choice)

5. Connect the jupyter kernel to the virtual environment:

```bash
python3 -m ipykernel install --user --name=companyx_task_venv
```

If you already have the `venv` folder then you can execute step 2 and 5 directly.

## Running the notebooks

The notebooks are in the form of jupyter notebooks (i.e. in `.ipynb` format) and they all live under the [`./notebooks`](./notebooks/) folder. Inside it there are the following notebooks:
1. `data_prep.ipynb` - The main objectives of this notebook are:
    * To understand the data and its structure.
    * To clean the data and make it ready for further analysis.
    * To save the cleaned data in a format that is easy to load and use for further analysis.
2. `eda.ipynb` - This notebook corresponds to Task - 1. The main objectives of this notebook are:
    * Conduct a thorough exploratory data analysis on the dataset provided. 
    * Answer all the questions raised as part of this task. 
    * Additionally, try to highlight a few more insights that could be interesting for the design of an optimal price recommendation engine.
3. `model_engineering.ipynb` - This notebook corresponds to Task - 2. The main objectives of this notebook are:
    * Choose two model training algorithms and briefly explain the rationale behind these choices.
    * Train two forecasting models that give predictions at *per hotel per week* aggregation level for a fixed number of time-steps (weeks) in the future. It also potentially tries to exploit all the insights gained from task 1.
    * Conduct a holistic evaluation of the two models and make some general observations about their performance, interpretability and scalability.

To run the notebooks, execute the following command from the root (or from the `notebooks` directory) of the project:
```bash
jupyter lab
```

Run all the cells in the notebooks in the order they appear. The notebooks are designed to be self-contained and should run without any issues. 

Please run all the notebooks in the order as they appear in the list above. This is because data produced in the previous notebooks are used as inputs to the subsequent notebooks. 

The first notebook `data_prep.ipynb` expects the raw data `hotel_bookings.csv` in the `data` folder.

All data produced as part of the execution of the notebooks are saved in the `data` folder in `parquet` format.