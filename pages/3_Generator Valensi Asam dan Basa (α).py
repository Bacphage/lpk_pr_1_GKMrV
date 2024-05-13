import streamlit as st
import re

st.set_page_config(
    page_title="Generator Valensi Asam dan Basa (α) ",
    page_icon="⚗️"
)

st.page_link("Main.py", label="Main Menu", icon="⚒️")
st.page_link("pages/2_Generator Massa Molekul Relatif (Mr).py", label="Generator Massa Molekul Relatif (Mr)", icon="🧪")
st.page_link("pages/4_Kalkulator Berat Ekuivalen (BE).py", label="Kalkulator Berat Ekuivalen (BE)", icon="🧮")

def check_valency(compound):
    # Menghapus spasi yang mungkin ada
    compound = compound.replace(" ", "")
    
    # Pengecualian untuk NH4OH dan CH3COOH
    if compound == "NH4OH" or compound == "CH3COOH":
        return f"{compound} adalah asam dengan valensi 1"
    
    # Mencocokkan pola regex untuk menemukan angka setelah H
    match_h = re.match(r'^H(\d*)', compound)
    if match_h:
        # Jika ditemukan, ambil angka setelah H
        valency = int(match_h.group(1)) if match_h.group(1) else 1
        return f"{compound} adalah asam dengan valensi {valency}"
    
    # Mencocokkan pola regex untuk menemukan OH dan angka di sebelahnya
    match_oh = re.match(r'[^\(]OH(\d*)', compound)
    if match_oh:
        # Jika ditemukan, ambil angka setelah OH
        valency = int(match_oh.group(1)) if match_oh.group(1) else 1
        return f"{compound} adalah basa dengan valensi {valency}"
    
    # Mencocokkan pola regex untuk menemukan (OH) dan angka di sebelahnya
    match_oh_in_bracket = re.match(r'\(OH\)(\d*)', compound)
    if match_oh_in_bracket:
        # Jika ditemukan, ambil angka setelah (OH)
        valency = int(match_oh_in_bracket.group(1)) if match_oh_in_bracket.group(1) else 1
        return f"{compound} adalah basa dengan valensi {valency}"
    
    # Mencocokkan pola regex untuk senyawa yang tidak mengandung H, OH, atau (OH)
    match_other = re.match(r'^[A-Za-z]+\(*[A-Za-z]*\)*(\d*)', compound)
    if match_other:
        # Jika ditemukan, ambil angka setelah senyawa
        valency = int(match_other.group(1)) if match_other.group(1) else 1
        return f"{compound} adalah senyawa dengan valensi {valency}"
    
    # Jika tidak memenuhi syarat asam maupun basa
    return "Senyawa tidak termasuk asam maupun basa"

def main():
    st.title("Generator Valensi Asam dan Basa")

    compound = st.text_input("Masukkan rumus senyawa:        (Contoh HCl")
    if st.button("Munculkan"):
        result = check_valency(compound)
        st.write(result)

if __name__ == "__main__":
    main()
