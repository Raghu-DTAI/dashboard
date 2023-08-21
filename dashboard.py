import pymongo
import os
from pymongo import MongoClient
import urllib
import streamlit as st
#from pymongo.server_api import ServerApi

uri = os.environ['MONGO_URI']
user = os.environ['MONGO_USER']
password = os.environ['MONGO_PASSWORD']

uri = uri.format( urllib.parse.quote_plus(user), urllib.parse.quote_plus(password))

# Create a new client and connect to the server
client = MongoClient(uri)

default_db = os.environ['MONGO_DB']
db = client[default_db]

resources=db.resources
with st.expander('The number of resources overall is'):
    st.write(f" There are {resources.count_documents({})} number of reosurces overall")

resource_data=db.resource_data
with st.expander('The number of resources completed_documenting is'):
    st.write(f" There are {resource_data.count_documents({})} number of reosurces that have completed documenting")

terminologies=db.terminologies
with st.expander('The number of terminologies extracted is'):
    st.write(f" There are {terminologies.count_documents({})} number of terminologies extracted")



