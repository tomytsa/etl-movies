def transform_data(df):
    columns_to_drop = ['Poster_Link', 'Certificate', 'Meta_score', 'Gross']
    clean_df = df.drop(columns_to_drop, axis = 1)
    return clean_df