import streamlit as st
import pandas as pd
import numpy as np

# 1. Títol i descripció de la web
st.title("🚇 Calculadora de Rutes: Metro de Barcelona")
st.write("Calcula la distància més curta entre dues estacions utilitzant matrius d'adjacència.")

# 2. Carregar les dades (utilitzem cache perquè la matriu no es calculi cada cop que toquem un botó)
@st.cache_data
def prepara_matriu():
    estacions_df = pd.read_csv('estacions.csv')
    trams_df = pd.read_csv('trams_linia_metro.csv')
    
    noms_estacions = estacions_df['NOM_ESTACIO'].str.strip().unique()
    estacio_a_id = {nom: i for i, nom in enumerate(noms_estacions)}
    
    N = len(noms_estacions)
    A = np.zeros((N, N), dtype=int)
    
    for index, row in trams_df.iterrows():
        origen = str(row['NOM_ESTACIO_INI']).strip()
        desti = str(row['NOM_ESTACIO_FI']).strip()
        if origen != "Inici" and desti != "Final":
            if origen in estacio_a_id and desti in estacio_a_id:
                i = estacio_a_id[origen]
                j = estacio_a_id[desti]
                A[i, j] = 1
                A[j, i] = 1
                
    return estacio_a_id, noms_estacions, A

estacio_a_id, noms_estacions, A = prepara_matriu()

# 3. La teva funció matemàtica
def troba_recorregut_mes_curt(origen_nom, desti_nom, matriu_A, diccionari):
    i = diccionari[origen_nom]
    j = diccionari[desti_nom]
    if i == j: return 0, 1
        
    M = matriu_A.copy()
    k = 1
    N_nodes = matriu_A.shape[0]
    
    while M[i, j] == 0 and k < N_nodes:
        k += 1
        M = M @ matriu_A
        
    if M[i, j] > 0:
        return k, M[i, j]
    else:
        return -1, 0

# 4. Interfície d'usuari (Desplegables i botons)
origen = st.selectbox("📍 Selecciona l'estació d'origen:", noms_estacions)
desti = st.selectbox("🏁 Selecciona l'estació de destí:", noms_estacions)

if st.button("Calcula el recorregut"):
    k_min, num_recorreguts = troba_recorregut_mes_curt(origen, desti, A, estacio_a_id)
    
    if k_min == -1:
        st.error("❌ No s'ha trobat cap connexió entre aquestes estacions.")
    elif k_min == 0:
        st.info("Ja ets a l'estació de destí!")
    else:
        st.success(f"✅ El recorregut més curt té **{k_min} parades**.")
        st.write(f"S'han detectat **{num_recorreguts}** rutes diferents amb aquesta mateixa llargada.")