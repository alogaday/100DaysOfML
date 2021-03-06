# 100DaysOfML


Day 1: 2nd February:

Started the streak.

- Had a glance at Andrew ng notes
	- Hypothesis function
		prediction or y hat >> h(theta) = theta0 + theta1 * X1
	- Cost function
		sum of root squared error
		difference between actual value and hypothesis function value
		J(theta0, theta1) = Root mean squared error
	- Gradient descent:
		derivative of cost function with respective to theta, i.e: dJ/dTheta
		update theta values >> theta = theta - alpha * dJ/dTheta

Day 2: 3rd February:

- More on gradient descent, linear regression and logistic regression
	- Batch Gradient descent
		computes gradient of the cost function on all the training data
	- Stochastic gradient descent
		computers gradient of the cost function on one training data point or observation
	- Mini batch gradient descent
		computers gradient of the cost function on some training data points in a batch mode.
		i.e. all the training points are divided into M parts, and each time one part will be used to 
		calculate the gradient of the cost function
	
	- Regularization:
		- to avoid over fitting, to decrease the weights
		- adds regularization parameter to the cost function
		- L2 regularization or Ridge regression:
			- J(w) = i/n SIGMA (y(x) - y)2 + lambda || W || 2
			- more weights, more peanlizes
			
		- L1 regularization or Lasso regression:
			- J(w) = J(w) = i/n SIGMA (y(x) - y)2 + lambda || W ||
			- spars, peanlizes weights equally
			
	- Logistic regression:
		- hypothesis function is a sigmoid function
		- h(theta) = 1/(1+e-Z)
		- this function gives ouput always between 0 and 1
		- cost function for logistic regression is negative log likeli hood
		- If the target is assigned low prob, then cost will be high, if the target is assigned high prob, then cost is low.
		
		
Day 3: 4th February:

- KNN model

	- no training required, the training data points acts as training the model
	- no parameters to tune
	- pick the nearest K value to determine the target class
	- for regression problems, average of the K nearest data points
	- standadize the data so that distance will be calcualted correctly
	
- Normalization vs. standardization:

	- https://medium.com/@zaidalissa/standardization-vs-normalization-da7a3a308c64
	- standardization is to make the data in the gaussian distribution, i.e. mean = 0, std = 1
	- standardization = (X-mean)/std
	
	- Normalization: Min, max scaling
	- (X - min)/ Max - Min
	- result values are between 0 and 1
	
Day 4: 5th February:

- KNN on MNIST dataset
- 10000 dataset and quiz pending

Day 1: 22nd Feb

- SVM
    
    - Max margin classifier
    - Soft margin classifier when the points are not separable
        - Regularization parameter C - Large values of C means classifies more points correctly with less margin, small values of C means, misclassifies more points with higher margin
    - Kernal methods - when the points are not linearly separable
        - maps the data to higher dimension so that it can be linearly separable in the higher dimension, when we look back to normal dimension, the separator becomes non linear
        - gamma controls the range of points to influence on the separator
    - SVM quiz pending
    

Date: 28th Feb

- Naive Bayes

    - Parametric models vs. Non parametric model
        - Parametric models will have an equation with parameters to predict
            - example: logistic regression
        - Non parametric model, no parameters
            - example: KNN
    - Naive bayes algo
        - it's naive because of its assumtion --> all features are independent of each other
         - P(y|X) = P(y) * P(X/y) / P(X)
    

- AA

    - till page num 130
        - DB vista rules: similar to vista rules but can be mapped to a generic values using FTP uploads
            - example: sales person name --> sales region mapping
            - sales person can change but region can be used as a key for the mapping
            
Date: 4th March

- AA

    - till page num 150
        - traffic vars, doesn't get retained
        - two traffic vars, on same page can be broken down; if only one traffic var on that page, then breakdown shows unspecified
        - traffic vars breakdown is called correlation
        - conv vars breakdown is sub-relation
        - at the time of success event, if one or both of the eVars doesn't have any value, then it will show it in None row item
        - pathing reports are based on visit level
        - pathing report for cross visit is not possible as pathing is done at the visit level
		- To-do:
			- <data sources, importing online data, stitching offline vs. online data>

- ML

	- some notes:		
		- Cheatsheets: https://elitedatascience.com/vault
		- https://elitedatascience.com/machine-learning-interview-questions-answers#big-picture
		- Machine-Learning-A-Z-Q-A.pdf - <START THIS>
		- Next steps for projects:
		- list of projects in digital
		- visitor scoring <Get model walk through - internal>
		- segmentation
		- churn analysis
		- pathing
				
Date: 6th March

- ML

	- segmentation for visits:
		- visit based segmentation, identify K clusters and do the visitor profiling based on the clustered data
		- visit based, so derive visit id >> visitor id + visit number, Question: check if each row is a visit based (i.e. hits data is clubed for that visit?)
		- intense researchers vs. focused customers vs others
		- check the distribution of the data for each of these segments
		- how much % of leads comes from each of these segments, and conversion rate of each of the segment
		
	- visitor scoring
		- for visitor scoring, use logistic regression (supervised algo)
		- predicts weather visitor converts or not
		- this should also be done based on the visits based, (if we do at visitor based, the duration will be very large and we don't know when visitor data will end, but for visit the duration or hits are limited).

Date: 9th March

- AA

	- Multi suite tagging - when data is sent to more than one report suite
	- concept of global report suite: data gets send to global report suite as a common report suite for all the countries
		- unique visitor identification happens across the regions
	- SAINT (site catalyst attributes importing and naming tool) - for classification of the data
	- Merchandising variables:
		- https://analyticsdemystified.com/adobe-analytics/merchandising-evars-omniture/
		- connecting a different eVar value to the product at the time success event takes place
		- prod syntax
		- prod var syntax: cat;prod;quantity;incrementor;merchadising
		- conversion syntax
		- a traditional eVar can't associate a different value for each product; a traditional variable assigns only for value for all the products, i.e if I search X and add prod A to cart, search Y and prod B to cart, then I order A and B, search term Y gets the credit as it is last allocation traditional evars-omniture/
		- binding event >> I searched for X and then after 2 pages I reached the product A, now I would like to associate the merchandising value of the eVar to the product I viewed, I could assign prodview as the binding event (or scAdd). Basically, Adobe Analytics will tie that merchanding value of the eVar to that specific production at the time of success event
	- Participation:
		- participation is applied for an event, if it's enabled then the value will be allocated to all the eVars participated before this success event takes place
		- it is similar to linear allocation of the conversion variable, however linear allocation devides the success event equally, but participation gives the full credit for all the eVars which led to that specific conversion event

	- question: click map and activity map
	- question: add event to the pages report?
	- Pagetype >> to track error pages, page not found report, populates
		- s.pageType = "errorPage"; s.pageName = "" (can be blank to capture URL, else pass some string 404); s.pageName = "404 Page" + window.location.href
	- question: list prop
	- next steps: business practitioner sample questions
	
Date: March 10

- AA
	- Business practitioner certification prep:
		- conducting business analysis
			- conversion funnels
			- interpret solution design
			- identify outliers and anomalies in the reports
		- reporting and dashboarding
		- segmenting
		- Administring and troubleshooting