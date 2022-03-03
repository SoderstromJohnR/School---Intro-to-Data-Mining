# Binary Document Classification
  keywords.txt - A list of keywords with no given classification
  trainingData.txt - A list of statements with classification represented by a 0 or 1 at each end
  testData.txt - A list of statements with classification represented by a 0 or 1 at each end
  
In the example data, statements either belong to Computer Science material (such as a textbook, classified as 1) or come from another source (classified as 0). Keywords are assigned probabilities for each classification based on their appearance in known statements from the training data, then used to sort statements from test data into those classifications.

Keywords should not be generic. If they appear similarly often in statements regardless of classification, the probability a keyword determines a statement belongs to it will be near 50% and will be nearly useless in sorting data - keywords such as 'the' will be a poor use of time. If a keyword rarely shows up in only one classification, the probability will be closer to 0% or 100%, and forms a much stronger indicator of what classification a statement should belong to.

Test data statements still need their classification shown in the file, which will test the keyword probabilities from the training phase for usefulness. If effective, those keywords and probabilities could be used to sort other statements.

## Taken from final report for class
Over 200 statements were selected. No more than 3 came from a single chapter, or from the full source in case of smaller sources. Before selecting any statements, I decided to start from the third sentence of the first paragraph, the second sentence of the second paragraph, and the first sentence of the third paragraph where possible. I ended each selection at 15 words or the end of the paragraph, whichever came first. This was not always possible, particularly when selecting data from non-CS sources.

99 statements were selected from CS sources: an AI textbook and a compilers textbook. More diverse statements could have been selected from CS material covering different topics. Statements from other CS material may also not be classified correctly as often.

Statements from non-CS sources were obtained from a wider variety of material, including random Wikipedia pages, news articles, a textbook, and novels. I used a greater number of statements from this classification to try to handle the wider spread of keywords that may or may not exist compared to the CS sources.

My original set of keywords was insufficient to test the data - most of them barely appeared in the training set after I finished preparing the data. In order to improve the keywords, I tallied every word in the training data without seeing their classifications. I believe this let me obtain more meaningful keywords without adding bias, but it may still be a mistake. Even if it added bias, I believe it limited the effect of it.
