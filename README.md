#### Problem statement

A scientific magazine, RealScience, believes that it's social media presence should offer a haven of truth and meaning that is easily distinguishable from the tabloid-esque style of its technology oriented competitors.

RealScience is impressed by the substantial following of r/Science at 29.1 million subscribers, and hopes to grow its social media following to similar numbers.  With proper curation and delivery of content, magazine subscriptions can be expected to increase proportionately, as this is the primary source of the company's publicity.  

To assist in the company's efforts I will use reddit data from the subreddits technology and science to determine if they are distinguishable through machine learning models.  These can then be used to identify posts from the technology subreddit that may offer insight into how best to craft a post that can have appeal to potensially receptive audiences within the world of technology enthusiasts while maintaining a scientific flavor.

#### Methods

I used part of speech and character count statistics for the initial modeling approach.  I then looked at sentiment and text analysis separately, and finally combined all approaches into a model that provided 89.33% classification accuracy, which exceeded baseline accuracy of ~ 68% (preponderance of the most prequent class, technology.)

#### Modeling process

I tested a number of modeling packages including logistic regression and random forests, but the best model proved to be xgboost tuned through gridsearch to arrive at the optimal eta.  The text vectorizer that I used was tfidf, as this generated features with weights according to their likely significance to a model accourding to their frequency.

Stacking did not improve results, so I chose to combine data and analyze after column transforming.

#### Conclusions

The findings of this report demonstrate that it is possible for a model to distinguish, with substantial improvement over the baseline, between posts from the science and technology subreddits.

The model has also demonstrated that there is significant overlap between the science and technology subreddits, with around 25% of the scientific posts being classified as technological and around 5% of the technological posts being classified as scientific.  The difference in these misclassification magnitudes is likely due in part to the unbalanced priors of the classes, with around 68% of the posts being from the technology subreddit. Upon inspecting examples of these misclassifications, it became clear that many of the posts from technology that were classified as scientific were in fact highly scientific in nature.

The takeaway is that a technological tilt would not be amiss in RealScience's social media presence.  While this is not surprising, these findings offer that audiences appreciate findings that intertwine technological and scientific elements.