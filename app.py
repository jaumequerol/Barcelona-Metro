import streamlit as st
import pandas as pd
import numpy as np

st.title("Route Calculator: Barcelona Metro")
st.write("Calculate the shortest distance between two stations using adjacency matrices.")

@st.cache_data
def prepare_matrix():
    stations_df = pd.read_csv('stations.csv')
    sections_df = pd.read_csv('metro_line.csv')
    
    station_names = stations_df['NOM_ESTACIO'].str.strip().unique()
    station_to_id = {name: i for i, name in enumerate(station_names)}
    
    N = len(station_names)
    A = np.zeros((N, N), dtype=int)
    
    for index, row in sections_df.iterrows():
        origin = str(row['NOM_ESTACIO_INI']).strip()
        destination = str(row['NOM_ESTACIO_FI']).strip()
        if origin != "Inici" and destination != "Final":
            if origin in station_to_id and destination in station_to_id:
                i = station_to_id[origin]
                j = station_to_id[destination]
                A[i, j] = 1
                A[j, i] = 1
                
    return station_to_id, station_names, A

station_to_id, station_names, A = prepare_matrix()

def find_shortest_path(origin_name, destination_name, matrix_A, mapping_dict):
    i = mapping_dict[origin_name]
    j = mapping_dict[destination_name]
    if i == j:
        return 0, 1
        
    M = matrix_A.copy()
    k = 1
    num_nodes = matrix_A.shape[0]
    
    while M[i, j] == 0 and k < num_nodes:
        k += 1
        M = M @ matrix_A
        
    if M[i, j] > 0:
        return k, M[i, j]
    else:
        return -1, 0

origin = st.selectbox("📍 Select the origin station:", station_names)
destination = st.selectbox("🏁 Select the destination station:", station_names)

if st.button("Calculate route"):
    k_min, num_routes = find_shortest_path(origin, destination, A, station_to_id)
    
    if k_min == -1:
        st.error("No connection found between these stations.")
    elif k_min == 0:
        st.info("You are already at the destination station!")
    else:
        st.success(f"The shortest route has **{k_min} stops**.")
        st.write(f"Found **{num_routes}** different routes with this same length.")