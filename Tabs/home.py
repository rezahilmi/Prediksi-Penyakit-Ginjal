import streamlit as st


def app():
    # judul aplikasi
    st.title("Aplikasi Prediksi Penyakit Batu Ginjal")
    col1, col2 = st.columns(2)

    with col1:
        st.header("")
        st.title(''':blue[Early Detection, Better Protection]''')
        st.text("")
        st.text("Kelompok 9 - Data Mining 2024")

    with col2:
        st.image("Tabs/gambar_ginjal.png")

    st.title("")
    st.markdown(
        "Aplikasi ini dikembangkan menggunakan **Streamlit** untuk memprediksi risiko penyakit batu ginjal berdasarkan data medis pasien. Dengan memanfaatkan algoritma :blue-background[Decision Tree], aplikasi ini memberikan hasil prediksi secara interaktif dan menampilkan visualisasi performa model.")
