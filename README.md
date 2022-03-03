# Intro to Data Mining - CS 4342
Project 3 is not included because it involved no code.

## Project 1
#### Classifying documents in a binary fashion
The script takes in a collection of keywords that may or may not belong to some classification depending on the user. In the example data, statements either belong to Computer Science material (such as a textbook) or come from another source. Keywords are assigned probabilities for each classification based on their appearance in known statements from the training data, then used to sort statements from test data into those classifications.

Keywords should not be generic. If they appear similarly often in statements regardless of classification, the probability a keyword determines a statement belongs to it will be near 50% and will be nearly useless in sorting data - keywords such as 'the' will be a poor use of time. If a keyword rarely shows up in only one classification, the probability will be closer to 0% or 100%, and forms a much stronger indicator of what classification a statement should belong to.

Test data statements still need their classification shown in the file, which will test the keyword probabilities from the training phase for usefulness.

## Project 2
#### Ensemble model

## Project 4
#### K cluster
