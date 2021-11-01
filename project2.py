import pandas as pd
import numpy as np
import streamlit as st
import pickle as p

p_in = open("F:/ExcelR workings/model.pkl", "rb")
model = p.load(p_in)

def welcome():
    return "Welcome All"
def user_input_features():
    st.sidebar.header('User Input Features')
    number = st.sidebar.text_input('Number', )
    resolved_by = st.sidebar.text_input('Resolved_by', )
    assigned_to = st.sidebar.text_input('Assigned_to', )
    assignment_group = st.sidebar.text_input('Assignment_group',)
    u_symptom = st.sidebar.text_input('U_symptom', )
    subcategory = st.sidebar.text_input('Subcategory',)
    category = st.sidebar.text_input('Category', )
    location = st.sidebar.text_input('Location', )
    resolved_at = st.sidebar.text_input('Resolved_at', )
    sys_updated_by = st.sidebar.text_input('Sys_updated_by', )
    closed_at = st.sidebar.text_input('Closed_at', )
    opened_by = st.sidebar.text_input('opened_by', )
    sys_mod_count = st.sidebar.text_input('Sys_mod_count', )
    Data = {'Number': number, 'Resolved_by': resolved_by,
	    'Assigned_to': assigned_to, 'Assignment_group': assignment_group,
	    'U_symptom': u_symptom, 'Subcategory': subcategory,
	    'Category': category, 'Location': location,
	    'Resolved_at': resolved_at, 'Sys_updated_by': sys_updated_by,
	    'Closed_at': closed_at, 'Opened_by': opened_by,
	    'Sys_mod_count': sys_mod_count}
    features = pd.DataFrame(Data,index=[0])
    return features


def main():
    st.title("**Team-2**")
    st.title("Impact of Incidents")
    st.write("**This app predicts the impact of incidents**")
    html_temp = """
    <div style="background-color:Teal;padding:10px">
    <h2 style="color:white;text-align:center">Streamlit Incidents Impact ML App </h2>
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html=True)
    df = user_input_features()
    st.subheader('User Input parameters')
    st.write(df)
    result = ""
    if st.button("Predict"):
        result = model.predict(df)
    st.success('The output is {}'.format(result))
    st.subheader('Prediction')
    st.write(""" 1: **HIGH**
		 2: **MEDIUM**
		 3: **LOW**
	""")
    st.subheader("Created by:-")
    st.write("***Harsha***",",","***Gangadhar***")
    st.write("***Suresh***",",","***Sagar***")

if __name__=='__main__':
    main()