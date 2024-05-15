import streamlit as st


st.set_page_config(
    page_title="Pengertian dan Informasi",
    page_icon="📖"
)
st.page_link("Main.py", label="Main Menu", icon="🗜️")

st.title("Pengertian dan Informasi")
st.markdown("Berikut adalah :orange[pengertian] dan :violet[informasi] seputar website ini.")
st.header(":orange[Pengertian]", divider="gray")


st.subheader(":red[Berat Ekuivalen (BE)]")
st.markdown('''
:red[Berat ekuivalen] adalah jumlah gram zat yang diperlukan untuk mereaksikan atau bergabung dengan satu mol elektron atau satu mol ion hidrogen. :red[Berat ekuivalen] terutama penting dalam kimia untuk menentukan jumlah relatif berbagai zat yang terlibat dalam suatu reaksi kimia. Contohnya, dalam analisis kimia, :red[berat ekuivalen] digunakan untuk menghitung jumlah substansi dalam larutan berdasarkan reaksi kimia yang terjadi. Ini juga berguna dalam titrasi, di mana :red[berat ekuivalen] digunakan untuk menghitung konsentrasi larutan yang tidak diketahui. Dalam praktiknya, :red[berat ekuivalen] dapat dihitung dengan rumus yang melibatkan berat atom atau berat molekul zat yang terlibat dalam reaksi.
''')


st.subheader(":green[Massa Molekul Relatif (Mr)]")
st.markdown('''
:green[Massa molekul relatif (Mr)], juga dikenal sebagai :green[bobot molekul (BM)], adalah jumlah massa dari satu molekul suatu zat dalam satuan massa atom relatif (u) atau dalam gram per mol (g/mol). :green[Bobot molekul] diperoleh dengan menjumlahkan berat atom atau berat isotop masing-masing atom yang membentuk molekul tersebut. Ini adalah konsep penting dalam kimia karena membantu dalam menghitung jumlah partikel dalam suatu zat dan dalam menghubungkan berat zat dengan volume gas dalam hukum gas ideal. :green[Bobot molekul] juga digunakan dalam perhitungan stoikiometri untuk menentukan perbandingan antara jumlah zat yang terlibat dalam suatu reaksi kimia. Misalnya, dalam reaksi kimia, perbandingan berat-mol dapat digunakan untuk menentukan jumlah relatif reagen yang diperlukan untuk menghasilkan produk yang diinginkan.            
''')

st.subheader(":blue[Valensi (α)]")
st.markdown('''
:blue[Valensi (α)] suatu senyawa adalah jumlah atom hidrogen atau kelebihan dari satu molekul dari senyawa tersebut yang dapat bergabung dengan atau digantikan oleh atom-atom dari unsur lain. Ini mencerminkan kemampuan senyawa untuk membentuk ikatan kimia dengan unsur-unsur lain. :blue[Valensi] senyawa memberikan informasi tentang bagaimana senyawa tersebut akan bereaksi dengan unsur lain untuk membentuk senyawa baru. Misalnya, dalam air (H2O), oksigen memiliki :blue[valensi] dua karena dapat membentuk ikatan dengan dua atom hidrogen. Dalam senyawa seperti amonia (NH3), nitrogen memiliki :blue[valensi] tiga karena dapat membentuk tiga ikatan dengan atom hidrogen. Pengetahuan tentang :blue[valensi] senyawa penting dalam kimia karena membantu memahami sifat-sifat reaktif senyawa, membantu dalam meramalkan struktur molekul, dan memungkinkan pengembangan reaksi kimia yang spesifik dan efisien.
''')


st.header(":violet[Informasi]", divider="grey")


st.subheader("Rumus-Rumus")
st.markdown("Berikut merupakan rumus-rumus yang dipakai")



st.subheader("Berat Ekuivalen (BE)")
rumus = r"\text{BE} = \frac{Mr}{\alpha}"
st.latex(rumus)

st.markdown('''
Mr  = Massa molekul relatif / bobot molekul (BM)                     
α   = Valensi (alpha)
''')




st.subheader("Massa Molekul relatif (Mr)")
st.markdown("contoh HCl")
contoh_perhitungan = r"""
\begin{align*}
\text{Mr} &= \text{jumlah massa atom dalam molekul} \\
          &= \text{massa atom H} + \text{massa atom Cl} \\
          &= (1 \times 1.008) + (1 \times 35.45) \\
          &= 1.008 + 35.45 \\
          &= 36.458 \, \text{g/mol}
\end{align*}
"""

st.latex(contoh_perhitungan)



st.subheader("Valensi (α)")
st.markdown("contoh HCl")
rumus = r"\text{HCl terdiri dari satu atom H, α dari HCl adalah 1}"
st.latex(rumus)
