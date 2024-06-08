# Industrial-copper-modelling
The Industrial Copper Modeling project focuses on predicting the selling price and status (won or lost) in the industrial copper market using machine learning regression and classification algorithms. By exploring the dataset, performing data cleaning and preprocessing, and applying various machine learning techniques, we aim to develop models that can accurately predict the selling price and status in the copper market.Enhance data analysis and machine learning skills in the 'Industrial Copper Modeling' project. 

# Data Understanding: 

1.Identify the types of variables (continuous, categorical) and their distributions. Some rubbish values are present 		in ‘Material_Reference’ which starts with ‘00000’ value which should be converted into null. Treat reference columns 		as categorical variables. INDEX may not be useful.


# Data Preprocessing: 
1.Handle missing values with mean/median/mode.

2.Treat Outliers using IQR or Isolation Forest from sklearn library.

3.Identify Skewness in the dataset and treat skewness with appropriate data transformations, such as log 					transformation(which is best suited to transform target variable-train, predict and then reverse 							transform it back to original scale eg:dollars), boxcox transformation, or other techniques, to 							handle high skewness in continuous variables.

4.Encode categorical variables using suitable techniques, such as one-hot encoding, label encoding, or 						ordinal encoding, based on their nature and relationship with the target variable.


# EDA:
1.Try visualizing outliers and skewness(before and after treating skewness) using Seaborn’s boxplot, distplot, 				violinplot.

2.Feature Engineering: Engineer new features if applicable, such as aggregating or transforming existing features to create more informative representations of the data. And drop highly correlated columns using SNS HEATMAP.

3.Model Building and Evaluation:

4.Split the dataset into training and testing/validation sets.

5.Train and evaluate different classification models, such as ExtraTreesClassifier, XGBClassifier, or Logistic Regression, using appropriate evaluation metrics such as accuracy, precision, recall, F1 score, and AUC curve. 

6.Optimize model hyperparameters using techniques such as cross-validation and grid search to find the best-performing model.

7.Interpret the model results and assess its performance based on the defined problem statement.

Same steps for Regression modelling

8.Use pickle module to dump and load models such as encoder(onehot/ label/ str.cat.codes /etc), scaling models(standard scaler), ML models. First fit and then transform in separate line and use transform only for unseen data 
Eg: scaler = StandardScaler()
scaler.fit(X_train)
scaler.transform(X_train)
scaler.transform(X_test_new) #unseen data

# STREAMLIT PART:
Using streamlit module, create interactive page with

   (1) task input( Regression or Classification) and 
   
   (2) create an input field where you can enter each column value except ‘Selling_Price’ for regression 							model and  except ‘Status’ for classification model. 
   
   (3) perform the same feature engineering, scaling factors, log/any transformation steps which you used 							for training ml model and predict this new data from streamlit and display the output.
# RESULTS:

Classification: Achieved 97.9% accuracy with ExtraTreesClassifier.

Regression: Achieved 93.05% accuracy with RANDOMForestRegressor.
