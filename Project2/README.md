# Ensemble Model
Training and validation data are hard-coded at the bottom of the script, but may be replaced or have a new function written to read values from an input file. Data is expected to be in the format [0, 1, ... , "+"] with n columns where columns from 1 to n-1 are 0 or 1, and column n is + or - (a binary classification).

Create multiple models from random subsets of training data, and test effectiveness over the entire set. Keeps the model as long as error is under 50% across all training data. Once all models are complete, run the ensemble on validation data to test effectiveness.

Models are created by taking a subset of training data and creating a binary tree. Internal nodes are labeled with a column number up to the number of 0's and 1's in each data point, and leaf nodes are either + or -. Tree creation looks at each data point that would reach that subtree and determines which column would cause the greatest split, where 0 follows the left child and 1 follows the right child. When all data points left on that subtree have the same classification, it creates a leaf node with the classification.

In Model 2 from outputs below, the root node uses column 2 (3, because it starts from 0). A point represented by [1, 0, 1, "+"] will follow the right path, because the value in column 2 is 1. That node is labeled 1, and column 1 is 0, so the point follows the left path. This is a leaf node labeled "+", which is the label of the point, so it would correctly be classifed.

## Taken from final report for class
I tested several seeds, but had trouble finding one with a validation error under .6 on the ensemble model. Most seeds resulted in an ensemble training error of 0, but occasionally increased to .1. The seed used for these results was 67.
### Outputs
Model 1
[[0, 0, 1, '+'],
 [0, 0, 1, '+'],
 [1, 1, 0, '-'],
 [1, 0, 1, '+'],
 [1, 1, 0, '-'],
 [1, 0, 0, '+'],
 [1, 1, 0, '-'],
 [1, 1, 0, '-'],
 [1, 0, 1, '+'],
 [1, 1, 0, '-']]
Tree 1
root: 1
 left child: +
 right child: -

Model 2
[[1, 0, 0, '+'],
 [0, 1, 1, '-'],
 [0, 0, 0, '+'],
 [0, 1, 0, '+'],
 [1, 0, 0, '+'],
 [0, 0, 0, '+'],
 [0, 1, 0, '+'],
 [1, 0, 1, '+'],
 [0, 1, 0, '+'],
 [0, 0, 1, '+']]
Tree 2
root: 2
 left child: +
 right child: 1
  left child: +
  right child: -

Model 3
[[0, 0, 1, '+'],
 [1, 0, 1, '+'],
 [1, 0, 0, '+'],
 [0, 1, 1, '-'],
 [1, 1, 0, '-'],
 [1, 1, 0, '-'],
 [0, 0, 0, '+'],
 [1, 1, 0, '-'],
 [1, 1, 0, '-'],
 [0, 1, 0, '+']]
Tree 3
root: 1
 left child: +
 right child: 0
  left child: 2
   left child: +
   right child: -
  right child: -

Model 4
[[0, 1, 0, '+'],
 [1, 0, 0, '+'],
 [1, 1, 0, '-'],
 [0, 0, 0, '+'],
 [1, 0, 1, '+'],
 [0, 1, 1, '-'],
 [1, 1, 0, '-'],
 [0, 0, 0, '+'],
 [1, 0, 0, '+'],
 [0, 1, 0, '+']]
Tree 4
root: 1
 left child: +
 right child: 0
  left child: 2
   left child: +
   right child: -
  right child: -

Model 5
[[1, 1, 0, '-'],
 [1, 1, 0, '-'],
 [0, 0, 0, '+'],
 [1, 1, 0, '-'],
 [1, 0, 1, '+'],
 [1, 0, 0, '+'],
 [0, 1, 1, '-'],
 [0, 0, 0, '+'],
 [0, 1, 0, '+'],
 [1, 1, 0, '-']]
Tree 5
root: 1
 left child: +
 right child: 0
  left child: 2
   left child: +
   right child: -
  right child: -

Model 6
[[0, 0, 0, '+'],
 [0, 1, 0, '+'],
 [1, 1, 0, '-'],
 [0, 1, 1, '-'],
 [1, 0, 1, '+'],
 [0, 0, 1, '+'],
 [1, 1, 0, '-'],
 [0, 0, 0, '+'],
 [1, 0, 0, '+'],
 [1, 1, 0, '-']]
Tree 6
root: 1
 left child: +
 right child: 0
  left child: 2
   left child: +
   right child: -
  right child: -

Model 7
[[1, 0, 1, '+'],
 [0, 1, 0, '+'],
 [0, 1, 1, '-'],
 [1, 1, 0, '-'],
 [1, 1, 0, '-'],
 [0, 0, 0, '+'],
 [1, 1, 0, '-'],
 [1, 0, 0, '+'],
 [1, 1, 0, '-'],
 [0, 0, 1, '+']]
Tree 7
root: 1
 left child: +
 right child: 0
  left child: 2
   left child: +
   right child: -
  right child: -

Model 8
[[1, 1, 0, '-'],
 [0, 0, 1, '+'],
 [1, 0, 0, '+'],
 [1, 0, 1, '+'],
 [1, 1, 0, '-'],
 [0, 1, 1, '-'],
 [0, 0, 0, '+'],
 [0, 1, 0, '+'],
 [1, 1, 0, '-'],
 [1, 0, 1, '+']]
Tree 8
root: 1
 left child: +
 right child: 0
  left child: 2
   left child: +
   right child: -
  right child: -

Model 9
[[1, 0, 1, '+'],
 [0, 1, 1, '-'],
 [1, 0, 0, '+'],
 [0, 0, 1, '+'],
 [1, 0, 1, '+'],
 [1, 0, 0, '+'],
 [1, 0, 0, '+'],
 [1, 1, 0, '-'],
 [1, 1, 0, '-'],
 [1, 1, 0, '-']]
Tree 9
root: 1
 left child: +
 right child: -

Model 10
[[1, 1, 0, '-'],
 [1, 0, 0, '+'],
 [0, 0, 0, '+'],
 [0, 0, 1, '+'],
 [1, 0, 0, '+'],
 [0, 0, 1, '+'],
 [1, 1, 0, '-'],
 [0, 1, 1, '-'],
 [1, 0, 1, '+'],
 [0, 0, 1, '+']]
Tree 10
root: 1
 left child: +
 right child: -

Ensemble training error: 0.0
Ensemble validation error: 0.6
