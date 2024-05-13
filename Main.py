import streamlit as st 

st.set_page_config(
    page_title="Generator & Kalkulator Massa Molekul Relatif & Valensi",
    page_icon="⚒️"
)
st.markdown("<h1 style='text-align: center; color: white;'>Generator & Kalkulator Massa Molekul Relatif & Valensi</h1>", unsafe_allow_html=True)
st.header("")
st.markdown("")
st.markdown("Silahkan pilih opsi menu dibawah ini")

st.page_link("Main.py", label="Main Menu", icon="⚒️")
st.page_link("pages/1_Pengertian dan Informasi.py", label="Pengertian dan Informasi", icon="📖")
st.page_link("pages/2_Generator Massa Molekul Relatif (Mr).py", label="Generator Massa Molekul Relatif (Mr)", icon="🧪")
st.page_link("pages/3_Generator Valensi Asam dan Basa (α).py", label="Generator Valensi Asam dan Basa (α)", icon="⚗️")
st.page_link("pages/4_Kalkulator Berat Ekuivalen (BE).py", label="Kalkulator Berat Ekuivalen (BE)", icon="🧮")