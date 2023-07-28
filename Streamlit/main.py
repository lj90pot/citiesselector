import streamlit as st
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

#[theme]
#primaryColor="#f9bef5"
#backgroundColor="#FFFFFF"
#secondaryBackgroundColor="#a0cae2"
#textColor="#000000"
#font="sans serif"

# Function to load and preprocess the data
def load_data():
    data_df = pd.read_csv(r'C:\Users\luisj\Desktop\Ironhack\Archivos Ejercicios\09_Final project\citiesselector\Data\cities_clean_model.csv')
    numeric_df = data_df.select_dtypes(include=[float, int])

    #Transform data
    scalerss = StandardScaler()
    scaler_result=scalerss.fit(numeric_df)
    scalerss_numeric_df=scaler_result.transform(numeric_df)
    
    # Model
    kmeans = KMeans(n_clusters=3,n_init='auto', random_state=20)
    kmeans.fit(scalerss_numeric_df)
    clusters = kmeans.predict(scalerss_numeric_df)
    
    df=data_df
    df['clusters'] = clusters

    # Perform PCA
    #pca = PCA(2)
    #df = pca.fit_transform(scalerss_numeric_df)
    #df = pd.DataFrame(df, columns=['PCA1', 'PCA2'])
    #df['clusters'] = clusters

    return df, numeric_df.columns.tolist(), numeric_df,data_df, kmeans, scaler_result

def main():
    # Corrected: Unpack the returned value into four variables
    data, feature_columns,numeric_df, original_df, kmeans, scaler_result = load_data()

    # Set the title and description of the app
    st.title('Your Dreamed City')
    st.write('This app shows you the city within Europe that suits you the best according to the chosen features below')

    # Create a two-column layout using beta_columns
    col1, col2 = st.columns((0.5,0.5),gap="medium")

    # Add sliders for user input on the left side
    with st.sidebar:
        st.header('User Input')
        st.write('Please input your data for the following features:')
        user_input = {}
        for feature in feature_columns:
            min_value = original_df[feature].min()
            max_value = original_df[feature].max()
            default_value = (min_value + max_value) / 2
            user_input[feature] = st.slider(f'{feature}', min_value=min_value, max_value=max_value, value=default_value)

    # Button to calculate result
    if st.button('Get city suggestions'):
        # Convert user input to DataFrame
        user_input_df = pd.DataFrame([user_input])
        
        #applying transformation to user input
        #scalerss = StandardScaler()
        user_input_transformed = scaler_result.transform(user_input_df)

        # Apply the pre-trained KMeans model on user input PCA
        user_cluster = kmeans.predict(user_input_transformed)
        
        #Get only cities in the same cluster 
        user_cluster_df = original_df.loc[data['clusters'] == user_cluster[0]]
        numeric_filtered_df = numeric_df.loc[data['clusters'] == user_cluster[0]]

        #Show results on column 2
        with col1:
            # Calculate Euclidean distance between the user input point and all points in numeric_df
            distances = np.linalg.norm(numeric_filtered_df - user_input_df.values, axis=1)
            # Find the indices of the three closest points
            closest_indices = np.argsort(distances)[:3]  
            closest_records = user_cluster_df.iloc[closest_indices]
            closest_records=closest_records['cities_name'].tolist()
            # Get the three closest records from the user's input cluster with the user's input values
            st.write('Your data belongs to cluster:', user_cluster[0])
            st.subheader('Three better results: ')
            st.write('These are the 3 cities that are closer to your inputs')
            for city_name in closest_records:
                st.subheader(f"{city_name} :")
        
                # Display Google Map
                st.markdown(f'<iframe width="300" height="400" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://maps.google.com/maps?q={city_name}&output=embed"></iframe>',unsafe_allow_html=True)
        
                # Display Wikipedia link
                wikipedia_link = f"https://en.wikipedia.org/wiki/{city_name}"
                st.write(f"Link to Wikipedia page for {city_name}: [Wikipedia]({wikipedia_link})")
                st.divider()

      
        # Show result on the column 3
        with col2:

            # Get random records from the user's input cluster
            user_cluster_random_records = user_cluster_df['cities_name'].sample(3)
            user_cluster_random_records=user_cluster_random_records.tolist()
            
            st.write(' ')
            st.subheader('Three random cities: ')
            st.write('These are 3 random cities that also match with your preferences')
            for city_name in user_cluster_random_records:
                st.subheader(f"{city_name} :")
        
                # Display Google Map
                st.markdown(f'<iframe width="300" height="400" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://maps.google.com/maps?q={city_name}&output=embed"></iframe>',unsafe_allow_html=True)
        
                # Display Wikipedia link
                wikipedia_link = f"https://en.wikipedia.org/wiki/{city_name}"
                st.write(f"Link to Wikipedia page for {city_name}: [Wikipedia]({wikipedia_link})")
                st.divider()


if __name__ == '__main__':
    main()
