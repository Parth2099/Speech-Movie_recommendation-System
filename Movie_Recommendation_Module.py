import numpy as np
import pandas as pd

def movieRecomFun(movieStr):
    # --- Get the Data ---
    column_names = ['user_id', 'item_id', 'rating', 'timestamp']
    df = pd.read_csv('data_file.data', sep='\t', names=column_names)
    movie_titles = pd.read_csv("movies_data_record")
    df = pd.merge(df,movie_titles,on='item_id')

    # --- Visualization Imports ---
    ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
    ratings['Number_Of_Ratings'] = pd.DataFrame(df.groupby('title')['rating'].count())

    # --- Recommending Similar Movies ---
    moviemat = df.pivot_table(index='user_id',columns='title',values='rating')
    
    ## --- RuntimeWarning: Degrees of freedom <= 0 for slice --- ##
    moviemat = moviemat[moviemat.get(movieStr).notnull()]
    moviemat = moviemat.dropna(axis='columns', thresh=2)
    ## --- --- ##

    input_user_ratings = moviemat[movieStr]

    similar_to_input = moviemat.corrwith(input_user_ratings)

    corr_input = pd.DataFrame(similar_to_input,columns=['Correlation'])
    corr_input.dropna(inplace=True)

    corr_input = corr_input.join(ratings['Number_Of_Ratings'])

    # --- Printing Solution ---
    rMovies = corr_input[corr_input['Number_Of_Ratings']>100].sort_values('Correlation',ascending=False).head()
    #rMovies = pd.DataFrame(rMovies, columns = ['title', 'Correlation', 'num of ratings'])
    print(rMovies)


