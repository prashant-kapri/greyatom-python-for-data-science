# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank=pd.read_csv(path)
categorical_var=bank.select_dtypes(include='object')
print(categorical_var)
numerical_var=bank.select_dtypes(include='number')
print(numerical_var)





# code ends here


# --------------
# code starts here
bank.drop('Loan_ID',axis=1,inplace=True)
banks=pd.DataFrame(data=bank)
print(banks.isnull().sum())
bank_mode=banks.mode()
print(bank_mode)
banks.Gender.fillna(banks.Gender.value_counts().index[0],inplace=True)
banks.Married.fillna(banks.Married.value_counts().index[0],inplace=True)
banks.Dependents.fillna(banks.Dependents.value_counts().index[0],inplace=True)
banks.Self_Employed.fillna(banks.Self_Employed.value_counts().index[0],inplace=True)
banks.LoanAmount.fillna(banks.LoanAmount.value_counts().index[0],inplace=True)
banks.Loan_Amount_Term.fillna(banks.Loan_Amount_Term.value_counts().index[0],inplace=True)
banks.Credit_History.fillna(banks.Credit_History.value_counts().index[0],inplace=True)
print(banks.isnull().sum())
#code ends here


# --------------
# Code starts here
avg_loan_amount=pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values=['LoanAmount'],aggfunc='mean')



# code ends here



# --------------
# code starts here
loan_approved=banks[(banks.Self_Employed=='Yes') & (banks.Loan_Status=='Y')]
print(loan_approved.head(5))
loan_approved_se=loan_approved.count()
print(loan_approved_se)
loan_approved_nse=banks[(banks.Self_Employed=='No')&(banks.Loan_Status=='Y')].count()
print(loan_approved_nse.head(5))
print(loan_approved_nse)
percentage_se=(56*100/614)
print(percentage_se)
percentage_nse=(366*100/614)
print(percentage_nse)

# code ends here


# --------------
# code starts here
loan_term=banks.Loan_Amount_Term.apply(lambda x: x/12)
print(loan_term)
print(loan_term.count())
x=[]
count=0;
for i in loan_term: 
    if (i>=25):
        x.append(i)
        count+=1

print(count)
big_loan_term=count
# code ends here


# --------------
# code starts here
loan_groupby=banks.groupby('Loan_Status')['ApplicantIncome','Credit_History']
mean_values=loan_groupby.mean()




# code ends here


