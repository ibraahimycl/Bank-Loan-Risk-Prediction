# Bank Loan Risk Prediction

A comprehensive machine learning project for predicting credit risk in loan applications. This project helps banks identify high-risk customers before loan approval, reducing potential financial losses.

## 📋 Project Overview

This project implements a credit risk prediction model using the Home Credit Default Risk dataset. The model analyzes various customer features to predict whether a loan applicant is likely to default on their loan.

## 🎯 Features

- **Data Exploration & Analysis**: Comprehensive analysis of loan application data
- **Feature Engineering**: Advanced feature creation and selection techniques
- **Machine Learning Model**: LightGBM-based binary classification model
- **Hyperparameter Optimization**: Automated parameter tuning using Optuna
- **Model Evaluation**: ROC-AUC scoring and cross-validation
- **Production Ready**: Trained model saved for deployment

## 📊 Dataset

The project uses the Home Credit Default Risk dataset, which includes:

- **Application Data**: Main loan application information
- **Bureau Data**: Credit bureau information
- **Previous Applications**: Historical loan applications
- **Installment Payments**: Payment history
- **Credit Card Balance**: Credit card usage data
- **POS Cash Balance**: Point of sale transactions

## 🛠️ Technologies Used

- **Python 3.x**
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Scikit-learn**: Machine learning utilities
- **LightGBM**: Gradient boosting framework
- **Optuna**: Hyperparameter optimization
- **Matplotlib & Seaborn**: Data visualization
- **Jupyter Notebooks**: Interactive development

## 📁 Project Structure

```
BANKA_PROJE1/
├── README.md                           # Project documentation
├── data_exploration.ipynb             # Data exploration and analysis
├── feature_eng.ipynb                  # Feature engineering notebook
├── model_set_up.ipynb                 # Model training and optimization
├── final_model.pkl                    # Trained model file
├── final_model.txt                    # Model parameters
├── best_params.json                   # Optimized hyperparameters
├── submission.csv                     # Model predictions
├── app_train_fe.csv                   # Feature-engineered training data
├── app_test_fe.csv                    # Feature-engineered test data
└── home-credit-default-risk/          # Original dataset
    ├── application_train.csv
    ├── application_test.csv
    ├── bureau.csv
    ├── bureau_balance.csv
    ├── previous_application.csv
    ├── installments_payments.csv
    ├── credit_card_balance.csv
    ├── POS_CASH_balance.csv
    ├── sample_submission.csv
    └── HomeCredit_columns_description.csv
```

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.x installed on your system.

### Installation

1. Clone the repository:
```bash
git clone https://github.com/ibraahimycl/Bank-Loan-Risk-Prediction.git
cd Bank-Loan-Risk-Prediction
```

2. Install required packages:
```bash
pip install pandas numpy matplotlib seaborn lightgbm scikit-learn optuna joblib
```

3. For Jupyter notebooks:
```bash
pip install jupyter
```

### Usage

1. **Data Exploration**: Open `data_exploration.ipynb` to explore the dataset
2. **Feature Engineering**: Run `feature_eng.ipynb` to create features
3. **Model Training**: Execute `model_set_up.ipynb` to train the model
4. **Predictions**: Use the trained model (`final_model.pkl`) for new predictions

## 📈 Model Performance

The model achieves competitive performance on the Home Credit Default Risk challenge:

- **Algorithm**: LightGBM (Gradient Boosting)
- **Evaluation Metric**: ROC-AUC Score
- **Cross-Validation**: Stratified K-Fold
- **Hyperparameter Optimization**: Optuna framework

## 🔧 Model Configuration

The model uses the following optimized parameters:
- Learning Rate: 0.022
- Number of Leaves: 95
- Max Depth: 5
- Feature Fraction: 0.842
- Bagging Fraction: 0.863
- Regularization: L1=1.4, L2=2.91

## 📝 Key Features

### Feature Engineering
- Missing value imputation
- Categorical encoding
- Feature scaling and normalization
- Domain-specific feature creation
- Aggregation features from related tables

### Model Training
- Stratified cross-validation
- Hyperparameter optimization
- Feature importance analysis
- Model interpretability

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**İbrahim Yücel**
- GitHub: [@ibraahimycl](https://github.com/ibraahimycl)

## 🙏 Acknowledgments

- Home Credit Group for providing the dataset
- Kaggle community for the competition platform
- Open-source contributors for the libraries used

## 📞 Contact

If you have any questions or suggestions, please feel free to reach out:
- GitHub Issues: [Create an issue](https://github.com/ibraahimycl/Bank-Loan-Risk-Prediction/issues)

---

⭐ If you find this project helpful, please give it a star!
