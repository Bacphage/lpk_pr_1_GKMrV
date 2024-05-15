import streamlit as st

st.set_page_config(
    page_title="Kalkulator Massa Molekul Relatif & Valensi",
    page_icon="🧮"
)

st.page_link("Main.py", label="Main Menu", icon="🗜️")
st.page_link("pages/2_Generator Massa Molekul Relatif (Mr).py", label="Generator Massa Molekul Relatif (Mr)", icon="🧪")
st.page_link("pages/3_Generator Valensi Asam dan Basa (α).py", label="Generator Valensi Asam dan Basa (α)", icon="⚗️")

def custom_calculator():
    # Masukkan Mr (angka pertama)
    mr = st.number_input("Masukkan angka pertama (Mr):", format="%.0f")

    # Masukkan Valensi (angka kedua)
    valensi = st.number_input("Masukkan angka kedua (Valensi):",  format="%.0f")

    if st.button("Hitung"):
        # Memastikan Valensi tidak boleh 0 untuk menghindari pembagian dengan nol
        if valensi == 0:
            st.error("Valensi tidak boleh nol!")
        else:
            # Menghitung hasil pembagian Mr / Valensi
            result = int(mr / valensi)
            st.success(f"BE adalah: {result} g/grek")

if __name__ == "__main__":
    st.title("Kalkulator Pembagian Mr / Valensi (BE)")
    st.info("Kalkulator pembagian yang digunakan untuk mencari BE")

    rumus = r"\text{BE} = \frac{Mr}{\alpha}"
    st.latex(rumus)
    custom_calculator()
