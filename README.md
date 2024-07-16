# BNForest

`BNForest` is a Python package for generating synthetic data with Bayesian networks using random forests for conditional distributions. It provides tools to sample data based on a causal Directed Acyclic Graph (DAG). If the data variables follow a temporal order, `BNForest` provides a function for specifying a causal DAG based on such an ordering.

## Features

- **Synthetic Data Generation**: Generate synthetic datasets based on a Bayesian network.
- **Temporal Ordering DAG**: Specify a causal DAG based on a temporal ordering of the variables.

## Installation

You can install the `BNForest` package directly from GitHub using pip. Open your terminal and run:

```bash
pip install git+https://github.com/hgubler/BNForest.git
```

## Usage

The class for generating synthetic data, as well as the function for specifying a causal DAG based on a temporal ordering can be imported as follows

```python
from BNForest.bn_forest_sampler import BNForestSampler
from BNForest.temporal_order_dag import temporal_order_dag
```



