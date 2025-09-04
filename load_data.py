#!/usr/bin/env python3
"""
Data Loading Script for Bank Loan Risk Prediction Project

This script demonstrates how to load and prepare the Home Credit Default Risk dataset
for the machine learning model.
"""

import pandas as pd
import numpy as np
import os
from pathlib import Path

def load_application_data():
    """
    Load the main application data files.
    
    Returns:
        tuple: (train_data, test_data) - Training and test application data
    """
    data_dir = Path("home-credit-default-risk")
    
    # Load application data
    train_data = pd.read_csv(data_dir / "application_train.csv")
    test_data = pd.read_csv(data_dir / "application_test.csv")
    
    print(f"✅ Loaded training data: {train_data.shape}")
    print(f"✅ Loaded test data: {test_data.shape}")
    
    return train_data, test_data

def load_bureau_data():
    """
    Load bureau and bureau balance data.
    
    Returns:
        tuple: (bureau_data, bureau_balance_data) - Bureau related data
    """
    data_dir = Path("home-credit-default-risk")
    
    # Load bureau data
    bureau_data = pd.read_csv(data_dir / "bureau.csv")
    bureau_balance_data = pd.read_csv(data_dir / "bureau_balance.csv")
    
    print(f"✅ Loaded bureau data: {bureau_data.shape}")
    print(f"✅ Loaded bureau balance data: {bureau_balance_data.shape}")
    
    return bureau_data, bureau_balance_data

def load_previous_applications():
    """
    Load previous application data.
    
    Returns:
        pandas.DataFrame: Previous application data
    """
    data_dir = Path("home-credit-default-risk")
    
    # Load previous applications
    prev_app = pd.read_csv(data_dir / "previous_application.csv")
    
    print(f"✅ Loaded previous applications: {prev_app.shape}")
    
    return prev_app

def load_installments_payments():
    """
    Load installments payments data.
    
    Returns:
        pandas.DataFrame: Installments payments data
    """
    data_dir = Path("home-credit-default-risk")
    
    # Load installments payments
    installments = pd.read_csv(data_dir / "installments_payments.csv")
    
    print(f"✅ Loaded installments payments: {installments.shape}")
    
    return installments

def load_credit_card_balance():
    """
    Load credit card balance data.
    
    Returns:
        pandas.DataFrame: Credit card balance data
    """
    data_dir = Path("home-credit-default-risk")
    
    # Load credit card balance
    cc_balance = pd.read_csv(data_dir / "credit_card_balance.csv")
    
    print(f"✅ Loaded credit card balance: {cc_balance.shape}")
    
    return cc_balance

def load_pos_cash_balance():
    """
    Load POS cash balance data.
    
    Returns:
        pandas.DataFrame: POS cash balance data
    """
    data_dir = Path("home-credit-default-risk")
    
    # Load POS cash balance
    pos_cash = pd.read_csv(data_dir / "POS_CASH_balance.csv")
    
    print(f"✅ Loaded POS cash balance: {pos_cash.shape}")
    
    return pos_cash

def get_column_descriptions():
    """
    Load column descriptions for understanding the data.
    
    Returns:
        pandas.DataFrame: Column descriptions
    """
    data_dir = Path("home-credit-default-risk")
    
    # Load column descriptions
    descriptions = pd.read_csv(data_dir / "HomeCredit_columns_description.csv")
    
    print(f"✅ Loaded column descriptions: {descriptions.shape}")
    
    return descriptions

def main():
    """
    Main function to demonstrate data loading.
    """
    print("🚀 Loading Home Credit Default Risk Dataset...")
    print("=" * 50)
    
    try:
        # Load all data
        train_data, test_data = load_application_data()
        bureau_data, bureau_balance_data = load_bureau_data()
        prev_app = load_previous_applications()
        installments = load_installments_payments()
        cc_balance = load_credit_card_balance()
        pos_cash = load_pos_cash_balance()
        descriptions = get_column_descriptions()
        
        print("\n📊 Dataset Summary:")
        print(f"   • Training samples: {len(train_data):,}")
        print(f"   • Test samples: {len(test_data):,}")
        print(f"   • Target distribution: {train_data['TARGET'].value_counts().to_dict()}")
        
        print("\n✅ All data loaded successfully!")
        print("\n💡 Next steps:")
        print("   1. Run data_exploration.ipynb for detailed analysis")
        print("   2. Run feature_eng.ipynb for feature engineering")
        print("   3. Run model_set_up.ipynb for model training")
        
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        print("Please make sure the dataset files are in the 'home-credit-default-risk' directory.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main() 