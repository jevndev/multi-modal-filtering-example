# Multi Modal Filtering Example

A small demo of different classes of multi modal filtering techniques

**This project is currently undergoing development and is not in its minimal working state yet**

## Description

In this analysis, various state estimation techniques are applied to a simulated target and their accuracies are compared. The target to be filtered loosely follows three modes; staying stationary, 
moving with a constant velocity and turning with a constant turn rate. The target simulation switches between these three modes via a small markov chain with some interpolation between them.

Three simple models are used to correspond to these three modes; a constant position, constant velocity and constant turn rate model.

First, three single-modal kalman filters estimate the state of the target with these models. Then 
three multi-modal filters are implemented to estimate the state of the target using various techniques from the referenced literature.

## TODO:

* [ ] Implement Target Simulation
* [ ] Implement Single Modal Filters for each mode of target
* [ ] Implement Autonomous Multi Modal Filter
* [ ] Implement Cooperative Multi Modal Filter
* [ ] Implement Variable Structure Multi Modal Filter

## References

[1] X. Rong Li and V. P. Jilkov, “Survey of maneuvering target tracking. Part V. Multiple-model methods,” in IEEE Transactions on Aerospace and Electronic Systems, vol. 41, no. 4, pp. 1255-1321, Oct. 2005, doi: 10.1109/TAES.2005.1561886.
