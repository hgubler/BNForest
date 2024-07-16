import networkx as nx
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from qosa import QuantileRegressionForest

class BNForestSampler:
    """"
    Bayesian Network Model for generating synthetic data based on random forests

    Attributes:
    data: pd.DataFrame
        original dataset to be used for estimating the conditional distributions in the Bayesian Network
    max_depth: int
        maximum depth of the random forests / distribution forests
    min_samples_leaf: int
        minimum number of samples required to be at a leaf node in the random forests / distribution forests
    n_trees: int
        number of trees in the random forests / distribution forests
    n_samples: int
        number of samples to be generated
    causal_dag: nx.DiGraph
        causal DAG of the data
    n_quantiles: int
        number of quantiles to be used in the quantile regression forests for estimating the quantile function 
    """

    def __init__(self,
                 data=None,
                 max_depth=5,
                 min_samples_leaf=6,
                 n_trees=100,
                 n_samples=1000,
                 causal_dag=None,
                 n_quantiles=10) -> None:
        self.data = data
        self.n_trees = n_trees
        self.max_depth = max_depth
        self.min_samples_leaf = min_samples_leaf
        self.n_samples = n_samples
        self.causal_dag = causal_dag
        self.topological_order = list(nx.topological_sort(self.causal_dag))
        self.n_quantiles = n_quantiles



    
    def sample_synthetic_data(self):
        """
        Sample synthetic data from the causal DAG

        Returns:
        synthetic_data: pd.DataFrame
        """
        starting_node = self.topological_order[0]
        synthetic_data = pd.DataFrame(columns=self.data.columns, dtype='float32')
        # sample self.n_samples from the first node by random sampling from the node column of self.data
        first_node_samples = self.data[starting_node].sample(self.n_samples, replace=True)
        synthetic_data[starting_node] = first_node_samples.reset_index(drop=True)
        for node in self.topological_order:
            if node == starting_node:
                continue
            parents = list(self.causal_dag.predecessors(node))
            X = synthetic_data[parents]
            qrf = self.quantile_regression_forests[node]
            if qrf is None: # case where node has no parents
                node_samples = self.data[node].sample(self.n_samples, replace=True)
                synthetic_data[node] = node_samples.reset_index(drop=True)
            if isinstance(qrf, RandomForestClassifier): # in case where node is binary
                samples_probas = qrf.predict_proba(X)[: ,1]
                # sample from Bernoulli distribution
                samples = [np.random.binomial(1, p) for p in samples_probas]
                samples = np.array(samples)
                synthetic_data[node] = samples
            if isinstance(qrf, QuantileRegressionForest): # in case where node is continuous
                alpha = np.linspace(0.01, 0.99, self.n_quantiles)
                quantiles = qrf.predict_quantile(X, alpha=alpha)
                unif_samples = np.random.uniform(0, 1, self.n_samples)
                samples = [np.interp(x=unif_samples[i], xp=alpha, fp=quantiles[i, :]) for i in range(self.n_samples)]
                samples = np.array(samples)
                # check if node is binary
                if len(np.unique(self.data[node])) == 2:
                    samples = np.round(samples)
                synthetic_data[node] = samples
        return synthetic_data


    def fit_quantile_regression_forests(self):
        """
        Fit quantile regression forests to the data
        """
        # fit quantile regression forests
        self.quantile_regression_forests = {}
        for node in self.topological_order:
            # get parents
            parents = list(self.causal_dag.predecessors(node))
            if len(parents) == 0:
                self.quantile_regression_forests[node] = None
            
            # fir random forest classifier if node is binary
            elif len(np.unique(self.data[node])) == 2:
                X = self.data[parents]
                y = self.data[node]
                rf = RandomForestClassifier(n_estimators=self.n_trees, max_depth=self.max_depth, min_samples_leaf=self.min_samples_leaf, max_features='sqrt')
                rf.fit(X, y)
                self.quantile_regression_forests[node] = rf
            
            # fit quantile regression forest
            else:
                X = self.data[parents]
                y = self.data[node]
                qrf = QuantileRegressionForest(n_estimators=self.n_trees, max_depth=self.max_depth, min_samples_leaf=self.min_samples_leaf, max_features='sqrt')
                qrf.fit(X, y)
                self.quantile_regression_forests[node] = qrf

    def get_causal_synthetic_data(self):
        """
        Get synthetic data from the causal DAG
        """
        # fit quantile regression forests
        self.fit_quantile_regression_forests()
        # sample synthetic data
        synthetic_data = self.sample_synthetic_data()
        return synthetic_data
