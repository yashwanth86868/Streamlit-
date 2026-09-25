
# import streamlit as st
# import numpy as np
# import pandas as pd

# st.title('My First Streamlit App created by YASHWANTH BALIJ')
# st.write('This is my first Streamlit app. I am learning how to use Streamlit to create interactive web applications with Python.')


# st.sidebar.header('User Input Parameters')

# user_name = st.sidebar.text_input('Enter your name:')
# user_age = st.sidebar.slider('Select your age:', 0, 100, 25)

# favarite_color = st.sidebar.selectbox('Select your favorite color:', ['Red', 'Green', 'Blue', 'Yellow', 'Purple'])

# # Main Page Content
# st.header(f'Welcome, {user_name}!')
# st.write(f'You are {user_age} years old and your favorite color is {favarite_color}.')

# #Displaying Data

# st.subheader('Sample DataFrame')

# #Create a sample Dataframe 

# data = pd.DataFrame(
#     np.random.randn(10, 5),
#     columns=['A', 'B', 'C', 'D', 'E']
#     # colomns=('col %d' %i for i in range(5))
    
    
# )                            
# st.dataframe(data)

# #checkbox to show/hide data
# if st.checkbox('Show Data Summary'):
#     st.subheader('Data Summary')
#     st.write(data)
    
# if st.button('Say hello'):
#     st.write('Hello there!')
# else:
#     st.write('Goodbye!')