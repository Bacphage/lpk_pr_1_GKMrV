import streamlit as st
import re

st.set_page_config(
    page_title="Generator Massa Molekul Relatif (Mr)",
    page_icon="🧪"
)

st.page_link("Main.py", label="Main Menu", icon="⚒️")
st.page_link("pages/3_Generator Valensi Asam dan Basa (α).py", label="Generator Valensi Asam dan Basa (α)", icon="⚗️")
st.page_link("pages/4_Kalkulator Berat Ekuivalen (BE).py", label="Kalkulator Berat Ekuivalen (BE)", icon="🧮")

# Dictionary yang berisi massa atom relatif (Ar) dari semua unsur dalam tabel periodik
atomic_weights = { 'H': 1.008,   'He': 4.0026,  'Li': 6.94,    'Be': 9.0122,   'B': 10.81,
    'C': 12.011,  'N': 14.007,   'O': 15.999,   'F': 18.998,    'Ne': 20.180,
    'Na': 22.9898,'Mg': 24.305,  'Al': 26.982,  'Si': 28.085,   'P': 30.974,
    'S': 32.06,   'Cl': 35.453,  'Ar': 39.948, 'K': 39.0983,   'Ca': 40.078,
    'Sc': 44.956, 'Ti': 47.867,  'V': 50.942,   'Cr': 51.996,   'Mn': 54.938,
    'Fe': 55.845, 'Co': 58.933,  'Ni': 58.693,  'Cu': 63.546,   'Zn': 65.38,
    'Ga': 69.723, 'Ge': 72.63,   'As': 74.922,  'Se': 78.971,   'Br': 79.904,
    'Kr': 83.798, 'Rb': 85.468,  'Sr': 87.62,   'Y': 88.906,    'Zr': 91.224,
    'Nb': 92.906, 'Mo': 95.95,   'Tc': 98,      'Ru': 101.07,   'Rh': 102.91,
    'Pd': 106.42, 'Ag': 107.87,  'Cd': 112.41,  'In': 114.82,   'Sn': 118.71,
    'Sb': 121.76, 'Te': 127.6,   'I': 126.9,    'Xe': 131.29,   'Cs': 132.91,
    'Ba': 137.33, 'La': 138.91,  'Ce': 140.12,  'Pr': 140.91,   'Nd': 144.24,
    'Pm': 145,    'Sm': 150.36,  'Eu': 151.96,  'Gd': 157.25,   'Tb': 158.93,
    'Dy': 162.5,  'Ho': 164.93,  'Er': 167.26,  'Tm': 168.93,   'Yb': 173.05,
    'Lu': 174.97, 'Hf': 178.49,  'Ta': 180.95,  'W': 183.84,    'Re': 186.21,
    'Os': 190.23, 'Ir': 192.22,  'Pt': 195.08,  'Au': 196.97,   'Hg': 200.59,
    'Tl': 204.38, 'Pb': 207.2,   'Bi': 208.98,  'Po': 209,      'At': 210,
    'Rn': 222,    'Fr': 223,     'Ra': 226,    'Ac': 227,      'Th': 232.04,
    'Pa': 231.04, 'U': 238.03,   'Np': 237,    'Pu': 244,      'Am': 243,
    'Cm': 247,    'Bk': 247,     'Cf': 251,    'Es': 252,      'Fm': 257,
    'Md': 258,    'No': 259,     'Lr': 266,    'Rf': 267,     'Db': 270,
    'Sg': 271,    'Bh': 270,     'Hs': 270,    'Mt': 278,      'Ds': 281,
    'Rg': 281,    'Cn': 285,     'Nh': 286,    'Fl': 289,     'Mc': 289,
    'Lv': 293,    'Ts': 294,     'Og': 294,
    
}

# Fungsi untuk menghitung massa molekul relatif (Mr) dari sebuah senyawa
def calculate_molar_mass(formula, atomic_weights):
    # Fungsi bantuan untuk menghitung massa molar relatif (Mr) dari unsur dalam sebuah senyawa
    def calculate_molar_mass_helper(parsed_formula):
        molar_mass = 0
        # Looping melalui setiap unsur dalam rumus
        for element, count_str in parsed_formula:
            # Mengambil jumlah atom unsur
            count = int(count_str) if count_str else 1
            # Menambahkan massa molar unsur ke total massa molar
            if element in atomic_weights:
                molar_mass += atomic_weights[element] * count
            else:
                st.error(f"Massa atom relatif untuk unsur {element} tidak ditemukan.")
                return None
        return molar_mass

    # Menggunakan regex untuk memisahkan unsur dan gugus fungsional dalam rumus
    parsed_formula = re.findall(r'([A-Z][a-z]*)(\d*)|\(([^)]+)\)(\d*)', formula)
    molar_mass = 0

    # Looping melalui setiap unsur atau gugus fungsional dalam rumus
    for match in parsed_formula:
        if match[0]:
            # Jika ditemukan unsur dalam rumus, hitung massa molarnya
            count = int(match[1]) if match[1] else 1
            if match[0] in atomic_weights:
                molar_mass += atomic_weights[match[0]] * count
            else:
                st.error(f"Massa atom relatif untuk unsur {match[0]} tidak ditemukan.")
                return None
        elif match[2]:
            # Jika ditemukan gugus fungsional dalam rumus, hitung massa molarnya
            molar_mass += calculate_molar_mass_helper(re.findall(r'([A-Z][a-z]*)(\d*)', match[2])) * int(match[3])

    return molar_mass

# Membuat antarmuka pengguna menggunakan Streamlit
st.title("Generator Massa Molekul Relatif (Mr)")
st.markdown("Generator untuk memunculkan Mr dari suatu senyawa")
formula = st.text_input("Masukkan rumus senyawa kimia (contoh: HCl)",)

# Tombol untuk menghitung massa molar relatif (Mr) ketika ditekan
if st.button("Munculkan Mr"):
    molar_mass = calculate_molar_mass(formula, atomic_weights)
    # Menampilkan hasil penghitungan
    if molar_mass is not None:
        st.success(f"Massa molekul relatif (Mr) dari {formula} adalah {molar_mass:.2f} g/mol")
