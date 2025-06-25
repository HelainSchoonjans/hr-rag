import os
from langchain_community.document_loaders import PyPDFLoader

# define the datasource and load data
data_loader = PyPDFLoader('https://www.upl-ltd.com/images/people/downloads/Leave-Policy-India.pdf')
data_test=data_loader.load_and_split()
print(len(data_test))
print(data_test[0])
# split the text on character
# create embeddings
#5a create vector DB
#5b create index for hr report
# wrap within a function
#6a write a function to connect to bedrock foundation
#6b write a function wich searches the user promptS