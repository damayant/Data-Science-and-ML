## What is missing data ? Why do we need to handle missing data ?
Missing data, or Missing values, occur when no value is stored for the particular feature in a Data. Missing data are a common occurrence and can have a significant effect on the conclusions that can be drawn from the data.

##How to check missing data?
How to know if we have any missing data?
> data.isnull().values.any()

## How to handle missing data?

Handling missing values is an important step in data preprocessing to ensure the quality and integrity of the dataset. There are several common techniques to deal with missing values:

- <strong>Deleting Rows </strong>: If the number of missing values is relatively small compared to the total dataset, you can simply remove the rows with missing values. However, this approach is only suitable if the missing values are randomly distributed and not informative for your analysis.

- <strong>Deleting Columns </strong>: If a specific feature has a large number of missing values or is irrelevant to your analysis, you can choose to remove the entire column. Similar to deleting rows, this approach should be used cautiously to avoid losing valuable information.

- <strong>Imputation </strong>: Imputation involves filling in the missing values with estimated or predicted values. The choice of imputation method depends on the type of data and the characteristics of the missingness. Some common imputation techniques include:
   - <strong>Mean/Median/Mode Imputation: Fill the missing values with the mean, median, or mode of the respective feature. This method is simple but assumes that the missing values are missing completely at random (MCAR) or missing at random (MAR).

   - <strong>Regression Imputation </strong>: Predict the missing values using a regression model based on other variables in the dataset. This method is useful when there is a relationship between the missing values and other features.

   - <strong>K-Nearest Neighbors (KNN) Imputation </strong>: Estimate missing values by finding the K most similar records based on other variables and using their values to fill in the missing values. This method is suitable when there is no specific pattern in the missingness and the data points can be considered interchangeable.

- <strong>Multiple Imputation </strong>: Generate multiple imputed datasets by creating plausible values for missing data based on observed data and statistical models. Multiple imputation accounts for the uncertainty of imputed values and is often preferred in complex analyses.

- <strong>Indicator/Dummy Variables </strong>: Create an additional binary indicator variable to signify whether a value was missing or not. This approach allows the model to capture any patterns or relationships associated with missingness.

The choice of missing value handling technique depends on the specific dataset, the amount of missing data, and the nature of the analysis or model being used. It's important to consider the potential impact of each approach on the integrity of the data and the validity of the subsequent analysis.


## Some examples of missing data handling


Handling missing data is a crucial step in data preprocessing. Python provides several libraries and methods to handle missing data effectively. Here are some examples of how to handle missing data using popular libraries like pandas and scikit-learn:

1. **Identifying Missing Values**:
   ```python
   import pandas as pd

   # Read the CSV file
   data = pd.read_csv('your_file.csv')

   # Check for missing values in the entire DataFrame
   print(data.isnull().sum())

   # Check for missing values in a specific column
   print(data['column_name'].isnull().sum())
   ```

2. **Dropping Missing Values**:
   ```python
   import pandas as pd

   # Drop rows with any missing value in the DataFrame
   data.dropna(inplace=True)

   # Drop rows with any missing value in a specific column
   data.dropna(subset=['column_name'], inplace=True)
   ```

3. **Imputing Missing Values**:
   ```python
   import pandas as pd
   from sklearn.impute import SimpleImputer

   # Read the CSV file
   data = pd.read_csv('your_file.csv')

   # Create a SimpleImputer object
   imputer = SimpleImputer(strategy='mean')

   # Impute missing values in a specific column
   data['column_name'] = imputer.fit_transform(data[['column_name']])
   ```

4. **Filling Missing Values with a Constant**:
   ```python
   import pandas as pd

   # Fill missing values in a specific column with a constant
   data['column_name'].fillna(value='constant_value', inplace=True)
   ```

5. **Filling Missing Values with Forward or Backward Fill**:
   ```python
   import pandas as pd

   # Fill missing values with the previous valid value (forward fill)
   data['column_name'].fillna(method='ffill', inplace=True)

   # Fill missing values with the next valid value (backward fill)
   data['column_name'].fillna(method='bfill', inplace=True)
   ```


6. **By Mean/Median/Mode values**:
```
# Identify columns with missing values
columns_with_missing_values = data.columns[data.isnull().any()].tolist()

# Impute missing values with mean
for column in columns_with_missing_values:
    data[column].fillna(data[column].mean(), inplace=True)

# Verify the imputed dataset
print(data.head())
print('-----------------------')
#check the new dataset along with the imputed values
print(data)
```
### Note:  Check this medium link : https://medium.com/analytics-vidhya/handling-missing-data-data-pre-processing-8fbab02c8cb4
