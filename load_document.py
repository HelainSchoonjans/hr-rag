import os
from langchain_community.document_loaders import PyPDFLoader

# define the datasource and load data
data_loader = PyPDFLoader('https://www.upl-ltd.com/images/people/downloads/Leave-Policy-India.pdf')
data_test=data_loader.load_and_split()
print(len(data_test))
print(data_test[0])