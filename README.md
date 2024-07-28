# BNForest

`BNForest` is a Python package for generating synthetic data with Bayesian networks using random forests for the estimation of conditional distributions. It is the implementation of my final strategy for causal synthetic data generation developped during my Master's thesis. `BNForest` provides tools to sample data based on a causal Directed Acyclic Graph (DAG). If the data variables follow a temporal order, `BNForest` provides a function for specifying a causal DAG based on such an ordering.

## Features

- **Synthetic Data Generation**: Generate synthetic datasets based on a Bayesian network.
- **Temporal Ordering DAG**: Specify a causal DAG based on a temporal ordering of the variables.

## Installation

The `BNForest` package can be installed directly from GitHub using pip. Simply open the terminal and run:

```bash
pip install git+https://github.com/hgubler/BNForest.git
```

## Usage

The class for generating synthetic data, as well as the function for specifying a causal DAG based on a temporal ordering can be imported as follows.

```python
from BNForest.bn_forest_sampler import BNForestSampler
from BNForest.temporal_order_dag import temporal_order_dag
```

Besides a basic introduction below, a specific example for generating synthetic data can be found in the examples folder.

### Synthetic data generation

For a pandas dataframe `data`, one can generate synthetic data based on a networkx digraph `causal_dag` as follows. Note that BNForest requires either binary or numerical variables.  Discrete variables that contain more than two values are treated as numerical.

```python
synth_data_model = BNForestSampler(data=data, causal_dat=causal_dag)
synth_data = synth_data_model.get_causal_synthetic_data()
```
See the documentation of the BNForestSampler class for more parameters.

### Temporal order DAG

One potential way to specify a causal DAG is based on the temporal ordering within the data variables. The function `temporal_order_dag` requires a list of lists containing the variable names in the order of the temporal ordering to provide a temporal order DAG.

```python
causal_DAG = temporal_order_dag(temporal_ordering)
```

A jupyter notebook in the `examples` folder contains an example for specifyng a causal DAG based on a temporal ordering using the `temporal_order_dag` function. This causal DAG is then used to generate synthetic data using the `BNForestSampler` class.





