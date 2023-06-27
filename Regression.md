# Types of Regression
In supervised learning, regression is a type of learning where the goal is to predict a continuous or numerical value based on input features. There are different types of regression algorithms suited for various data types and problem domains. Here are some commonly used regression algorithms along with real-life use cases and Python code implementations:

1. **Linear Regression**:
   - Use Case: House Price Prediction
   - Description: Linear regression models the relationship between the input features and the target variable using a linear equation. It assumes a linear relationship between the independent variables and the dependent variable.
   - Python Implementation:

     ```python
     from sklearn.linear_model import LinearRegression

     # Create a Linear Regression model
     regressor = LinearRegression()

     # Train the model
     regressor.fit(X_train, y_train)

     # Make predictions on new data
     y_pred = regressor.predict(X_test)
     ```

2. **Decision Tree Regression**:
   - Use Case: Predicting Bike Rental Demand
   - Description: Decision tree regression models the target variable by splitting the feature space based on feature values and predicting the average target value within each split.
   - Python Implementation:

     ```python
     from sklearn.tree import DecisionTreeRegressor

     # Create a Decision Tree Regression model
     regressor = DecisionTreeRegressor()

     # Train the model
     regressor.fit(X_train, y_train)

     # Make predictions on new data
     y_pred = regressor.predict(X_test)
     ```

3. **Random Forest Regression**:
   - Use Case: Predicting Sales Revenue
   - Description: Random forest regression combines multiple decision trees to create an ensemble model. Each tree is trained on a random subset of features and contributes to the final prediction by averaging the predictions of all trees.
   - Python Implementation:

     ```python
     from sklearn.ensemble import RandomForestRegressor

     # Create a Random Forest Regression model
     regressor = RandomForestRegressor()

     # Train the model
     regressor.fit(X_train, y_train)

     # Make predictions on new data
     y_pred = regressor.predict(X_test)
     ```

4. **Support Vector Regression (SVR)**:
   - Use Case: Stock Price Prediction
   - Description: Support Vector Regression uses support vector machines to perform regression. It finds an optimal hyperplane that approximates the relationship between input features and target variables.
   - Python Implementation:

     ```python
     from sklearn.svm import SVR

     # Create an SVR model
     regressor = SVR()

     # Train the model
     regressor.fit(X_train, y_train)

     # Make predictions on new data
     y_pred = regressor.predict(X_test)
     ```

5. **Gradient Boosting Regression**:
   - Use Case: Demand Forecasting
   - Description: Gradient Boosting Regression builds an ensemble of weak prediction models, such as decision trees, and combines them to make accurate predictions. It iteratively trains new models to correct the errors of previous models.
   - Python Implementation:

     ```python
     from sklearn.ensemble import GradientBoostingRegressor

     # Create a Gradient Boosting Regression model
     regressor = GradientBoostingRegressor()

     # Train the model
     regressor.fit(X_train, y_train)

     # Make predictions on new data
     y_pred = regressor.predict(X_test)
     ```

These are just a few examples of regression algorithms and their implementations in Python. Real-life use cases can vary widely, but these examples demonstrate the application of regression algorithms in domains such as house price prediction, bike rental demand, sales revenue prediction, stock price prediction, and demand forecasting. The choice of the regression algorithm depends on the nature of the data, the relationship between the
