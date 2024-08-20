##Importing the Libraries
import streamlit as st
import pickle
import pandas as pd
##-----------

## Loading the ML Model 
movies_list = pickle.load(open('movies_project.pkl','rb'))
movies_list = pd.DataFrame(movies_list)
similarity = pickle.load(open('similarity.pkl','rb'))
##-----------

##Function to recommend movies
def recommend(movie):
    index = movies_list[movies_list['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    
    recommended_movies = []
    for i in distances[1:11]:
        recommended_movies.append(movies_list.iloc[i[0]].title)

    return recommended_movies
##-----------

##Streamlit website Code
st.header("Movie Recommender Website!")
option = st.selectbox(
   "Select any movie from given Select Box",
   movies_list['title'].values,
   index=None,
   placeholder="Movies List",
)

st.write('You selected:', option)

if st.button('Recommend Me'):
    recommendations = recommend(option)
    for i in recommendations:
        st.write(i)    
    
##------------