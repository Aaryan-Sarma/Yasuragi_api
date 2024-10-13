import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

# Load the dataset
df = pd.read_csv('user_profiles_with_schedules.csv')

# Sample the dataset (optional)
df_sampled = df.sample(frac=0.1, random_state=42)  # Use 10% of the data for training

# Display the first few rows of the dataset
print(df_sampled.head())

# Assuming 'generated_schedule' is the target variable we want to predict
X = df_sampled.drop(columns=['generated_schedule'])  # Features
y = df_sampled['generated_schedule']  # Target

# Create a Pipeline with OneHotEncoder and RandomForestClassifier
pipeline = Pipeline(steps=[
    ('encoder', OneHotEncoder(sparse_output=False, handle_unknown='ignore')),  # Handle unknown categories
    ('classifier', RandomForestClassifier(n_estimators=10, random_state=42))
])

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
pipeline.fit(X_train, y_train)

# Make predictions on the test set
y_pred = pipeline.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)

# Plotting the confusion matrix
plt.figure(figsize=(10, 7))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=pipeline.classes_, yticklabels=pipeline.classes_)
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.title('Confusion Matrix')
plt.show()

# Save the model
joblib.dump(pipeline, 'schedule_model.pkl')  # Save the model
