# Ensemble Model

## Taken from final report for class
I tested several seeds, but had trouble finding one with a validation error under .6 on the ensemble model. Most seeds resulted in an ensemble training error of 0, but occasionally increased to .1
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
