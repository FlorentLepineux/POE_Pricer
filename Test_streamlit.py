{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "67def892-2ac4-446c-b0e9-f431bc329891",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-08-24 12:13:43.192 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\ProgramData\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "\n",
    "# Charger le DataFrame\n",
    "df = pd.read_csv('Clean_Items_Prices.csv')\n",
    "\n",
    "# Titre de l'application\n",
    "st.title('Analyse des Objets de Path of Exile')\n",
    "\n",
    "# Afficher les premières lignes du DataFrame\n",
    "st.subheader('Aperçu des Données')\n",
    "st.write(df.head())\n",
    "\n",
    "# Sélecteur pour afficher différentes colonnes\n",
    "column = st.selectbox('Choisir une colonne à afficher', df.columns)\n",
    "\n",
    "# Afficher les données de la colonne sélectionnée\n",
    "st.subheader(f'Données de la colonne {column}')\n",
    "st.write(df[column])\n",
    "\n",
    "# Filtrer les données par type d'objet\n",
    "object_type = st.selectbox('Filtrer par type d\\'objet', df['type'].unique())\n",
    "filtered_df = df[df['type'] == object_type]\n",
    "st.subheader(f'Données filtrées pour le type d\\'objet: {object_type}')\n",
    "st.write(filtered_df)\n",
    "\n",
    "# Afficher des statistiques descriptives\n",
    "st.subheader('Statistiques Descriptives')\n",
    "st.write(df.describe())\n",
    "\n",
    "# Graphique de distribution des valeurs de 'chaosValue'\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "if 'chaosValue' in df.columns:\n",
    "    st.subheader('Distribution des valeurs de chaosValue')\n",
    "    plt.figure(figsize=(10, 5))\n",
    "    plt.hist(df['chaosValue'].dropna(), bins=30, edgecolor='black')\n",
    "    plt.xlabel('chaosValue')\n",
    "    plt.ylabel('Fréquence')\n",
    "    plt.title('Distribution des valeurs de chaosValue')\n",
    "    st.pyplot(plt)\n",
    "else:\n",
    "    st.warning('La colonne \"chaosValue\" est absente des données.')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
