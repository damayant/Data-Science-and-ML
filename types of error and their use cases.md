Classification error, mean squared error (MSE), and cross-entropy (also known as log loss or binary/multiclass log loss) are three common evaluation metrics used in machine learning, and they are suited for different types of tasks. Here's when to use each one:

1. **Classification Error (Misclassification Error)**:
   - **Use Case**: Classification error is primarily used for binary or multiclass classification problems where the goal is to categorize data points into one of several predefined classes or labels.
   - **Metric Description**: It measures the percentage of misclassified instances in your dataset.
   - **When to Use**: Use classification error when you want a simple and interpretable metric to understand the accuracy of your classifier. However, it doesn't provide fine-grained information about how confident the model's predictions are.

2. **Mean Squared Error (MSE)**:
   - **Use Case**: MSE is commonly used for regression problems where the goal is to predict a continuous numeric value.
   - **Metric Description**: It calculates the average of the squared differences between the predicted values and the true values.
   - **When to Use**: Use MSE when dealing with regression problems, especially when you want to penalize large prediction errors more heavily. It's sensitive to outliers.

3. **Cross-Entropy (Log Loss)**:
   - **Use Case**: Cross-entropy is typically used for binary or multiclass classification problems, especially in cases where you need to model probabilities and assess how well your model's predictions align with the true labels.
   - **Metric Description**: Cross-entropy measures the dissimilarity between predicted class probabilities and actual class probabilities.
   - **When to Use**: Use cross-entropy when you want a metric that penalizes models for being both overconfident and underconfident. It's particularly useful in scenarios where you need well-calibrated probabilities and when dealing with imbalanced datasets.

In summary:

- Use **classification error** for simple binary or multiclass classification tasks when you want to know the percentage of misclassified instances.
- Use **mean squared error (MSE)** for regression problems to measure the average squared difference between predicted and actual values.
- Use **cross-entropy** (log loss) for classification tasks when you need to assess the quality of class probabilities and want to penalize models for misclassifications, especially in situations where you want to calibrate probability estimates.

Remember that the choice of evaluation metric should align with the specific goals and characteristics of your machine learning task. It's also common to use additional metrics or custom metrics depending on the domain and problem at hand.
