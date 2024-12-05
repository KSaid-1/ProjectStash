# Description: This file contains the model dispatcher which is used to select the model based on the model name
# and defines a dictionary with keys that are names of models and values are the models themselves.
# Two decision tree models are defined in this file. The first one uses gini as the criterion and the second one uses entropy.

from sklearn import tree
from sklearn import ensemble

models = (
    {
        "decision_tree_gini": tree.DecisionTreeClassifier(criterion='gini'),
        "decision_tree_entropy": tree.DecisionTreeClassifier(criterion='entropy'),
        "rf": ensemble.RandomForestClassifier(),
    }
)
