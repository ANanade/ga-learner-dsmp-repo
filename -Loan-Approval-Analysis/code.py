# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
# code starts here
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include='object')
print(categorical_var)
numerical_var = bank.select_dtypes(include='number')
print(numerical_var)





# code ends here


# --------------
# code starts here

banks = bank.drop(['Loan_ID'], axis = 1)
null_values = banks.isnull().sum()
print(null_values)

bank_mode =  banks.mode()
print(bank_mode)
banks = banks.fillna(value = 'bank_mode')
print(banks)
banks.isnull().any()
#code ends here


# --------------
# Code starts here






avg_loan_amount = banks.pivot_table(values=["LoanAmount"], index=["Gender","Married","Self_Employed"], aggfunc=np.mean)
print(avg_loan_amount)

# code ends here



# --------------
# code starts here




loan_approved_se = len(banks[(banks['Self_Employed'] == 'Yes') &  (banks['Loan_Status'] == 'Y') ])
#loan_S =  banks[banks['Loan_Status'] == 'Y'].set()
#loan_approved_se =  self_E + loan_S

loan_approved_nse = len(banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')])
#loan_S =  banks[banks['Loan_Status'] == 'Y'].set()
print(loan_approved_nse)
#loan_approved_nse = self_N + loan_S

Loan_Status = 614

percentage_se = ((loan_approved_se / 614) * 100)
percentage_nse =  (( loan_approved_nse / 614) * 100)

print(percentage_nse)
print(percentage_se)
# code ends here


# --------------
# code starts here


loan_term =  banks['Loan_Amount_Term'].apply(lambda x: int(x)/12 )
#df['year'] = pd.DatetimeIndex(df['birth_date']).year
#big_loan_term = 

print(loan_term)
big_loan_term = len(loan_term[loan_term >= 25])

print(big_loan_term)


# code ends here


# --------------
# code starts here




loan_groupby = banks.groupby('Loan_Status')
print(loan_groupby)

loan_groupby = loan_groupby['ApplicantIncome', 'Credit_History']
mean_values = loan_groupby.mean()
# code ends here


