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
		
	
	
	
