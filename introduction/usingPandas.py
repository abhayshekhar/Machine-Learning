import pandas as pd
from IPython.display import display

print('---creating a simple dataset of people---')
data={'Name':['John','Abhay','Tanuj'],
      'Location':['New York','Jharkhand','Shillong'],
      'Age':['45','22','22']  }

data_pandas=pd.DataFrame(data)
display(data_pandas)
print('--People above age 40--')
display(data_pandas[data_pandas.Age>'40'])