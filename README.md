# Home Loan Approval Predictor

Welcome to the **Home Loan Approval Predictor**! This project uses machine learning to predict whether a home loan application will be approved or rejected based on applicant details. Built with Python and Streamlit, it provides an easy-to-use web interface for users to input their information and get instant predictions.

## 🌐 Try the App

You can use the Home Loan Approval Predictor directly online! Visit the deployed app here:  
👉 [**Home Loan Approval Predictor App**](https://loan-approval-prediction-klgdpjsksaktokquvhttpn.streamlit.app/)

## 📖 Project Overview

The Home Loan Approval Predictor is designed to help users understand their eligibility for a home loan. It uses a pre-trained machine learning model (saved as `pipeline.pkl`) to analyze factors like income, credit history, education, and property area. The model was trained on the [Loan Prediction Problem Dataset from Kaggle](https://www.kaggle.com/datasets/altruist/delhi-house-price-prediction).

### Key Features
- **User-Friendly Interface**: A clean Streamlit app for entering personal and financial details.
- **Accurate Predictions**: Powered by a robust machine learning pipeline with preprocessing, SMOTE, and a classifier.
- **Input Validation**: Uses Pydantic to ensure all inputs are valid and within acceptable ranges.
- **Instant Results**: Get a clear "Eligible" or "Not Eligible" verdict with a visually appealing output.

## 🚀 Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites
- Python 3.8 or higher
- Git (optional, for cloning the repository)
- A code editor like VS Code

### Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/home-loan-approval-predictor.git
   cd home-loan-approval-predictor
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure the Model File**:
   - Make sure the `pipeline.pkl` file is in the `models` folder. This file contains the pre-trained machine learning model.

5. **Run the Streamlit App**:
   ```bash
   streamlit run app.py
   ```
   - Open your browser and go to `http://localhost:8501` to use the app.

### Dependencies
The project relies on the following Python libraries:
- `streamlit`: For the web interface
- `pandas`: For data manipulation
- `pydantic`: For input validation
- `pickle`: For loading the pre-trained model
- `scikit-learn`: For the machine learning pipeline
- `imblearn`: For SMOTE (handling imbalanced data)

Install them using:
```bash
pip install streamlit pandas pydantic scikit-learn imblearn
```

## 🖥️ How to Use

1. **Launch the App**: Use the [online app](https://loan-approval-prediction-klgdpjsksaktokquvhttpn.streamlit.app/) or run `streamlit run app.py` locally and open the provided URL in your browser.
2. **Enter Personal Information**:
   - Select your gender, marital status, number of dependents, education level, employment status, and property area.
3. **Enter Financial Information**:
   - Input your income, co-applicant’s income (if any), loan amount, loan term, credit history, income category, and loan amount category.
4. **Predict**:
   - Click the "Predict" button to see if your loan application is "Eligible" or "Not Eligible".
5. **Reset Options**:
   - Use "Reset All" to clear all fields or "Reset Financial" to clear only financial inputs.

## 📊 Model Details

The machine learning model is a pipeline that includes:
- **Preprocessing**: StandardScaler for numerical features and OneHotEncoder for categorical features.
- **SMOTE**: To handle imbalanced data by oversampling the minority class.
- **Classifier**: A logistic regression model (or other classifiers like RandomForest, XGBoost, etc., depending on the pipeline configuration).
- **Evaluation**: The model was evaluated using metrics like F1 Score, ROC AUC, and accuracy, with top models compared using LazyPredict.

The dataset used for training includes 13 features, such as:
- Applicant Income
- Coapplicant Income
- Loan Amount
- Credit History
- Property Area
- Education, and more

For detailed model performance, refer to the [Jupyter Notebook](LOAN_APPROVED_WORK.ipynb) in the repository.

## 📂 Project Structure
```
home-loan-approval-predictor/
├── app.py                   # Main Streamlit application
├── models/
│   └── pipeline.pkl         # Pre-trained machine learning model
├── requirements.txt         # Python dependencies
├── LOAN_APPROVED_WORK.html  # Jupyter Notebook with model training details
└── README.md                # This file
```

## 🛠️ Troubleshooting

- **Model File Missing**: Ensure `pipeline.pkl` is in the `models` folder. If you need to retrain the model, refer to the Jupyter Notebook (`LOAN_APPROVED_WORK.html`).
- **Dependency Issues**: Verify that all dependencies are installed correctly. Use `pip install -r requirements.txt`.
- **Streamlit Errors**: Make sure you’re running the app with `streamlit run app.py` and that the port `8501` is free.
- **Input Errors**: The app uses Pydantic to validate inputs. If you see an error, check that your inputs match the expected ranges and formats.

## 🤝 Contributing

Contributions are welcome! If you’d like to improve the project, please:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙌 Acknowledgments

- [Kaggle](https://www.kaggle.com) for providing the Loan Prediction Problem Dataset.
- [Streamlit](https://streamlit.io) for the amazing web app framework.
- [Scikit-learn](https://scikit-learn.org) and [Imbalanced-learn](https://imbalanced-learn.org) for machine learning tools.

## 📬 Contact

Have questions or suggestions? Reach out to me at:
- Email: tongjohn9@gmail.com
- GitHub: [link](https://github.com/JohnTong12)

Happy predicting! 🎉
