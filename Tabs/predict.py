import streamlit as st

from web_functions import predict


def app(df, x, y):
    st.title("Halaman Prediksi")

    col1, col2, col3 = st.columns(3)

    with col1:
        bp = st.text_input("Masukkan Blood Pressure (mmHg)")
        sg = st.text_input("Masukkan Specific Gravity")
        al = st.text_input("Masukkan Albumin (0-5)")
        su = st.text_input("Masukkan kadar gula (0-5)")
        rbc = st.text_input("Masukkan Red Blood Cells")
        pc = st.text_input("Masukkan Pus Cell")
        pcc = st.text_input("Masukkan Pus Cell Clumps")
        ba = st.text_input("Masukkan Bacteria")
    with col2:
        bgr = st.text_input("Masukkan Blood Glucose Random (mg/dL)")
        bu = st.text_input("Masukkan Blood Urea (mg/dL)")
        sc = st.text_input("Masukkan Serum Creatinine (mg/dL)")
        sod = st.text_input("Masukkan Sodium (mg/dL)")
        pot = st.text_input("Masukkan Potassium (mg/dL)")
        hemo = st.text_input("Masukkan Hemoglobin (mg/dL)")
        pcv = st.text_input("Masukkan Packed Cell Volume")
        wc = st.text_input("Masukkan White Blood Cell Count")
    with col3:
        rc = st.text_input("Masukkan Red Blood Cell Count")
        htn = st.text_input("Masukkan Hypertension")
        dm = st.text_input("Masukkan Diabetes Melitius")
        cad = st.text_input("Masukkan Coronary Artery Disease")
        appet = st.text_input("Masukkan Appetite")
        pe = st.text_input("Masukkan Pedal Edema")
        ane = st.text_input("Masukkan Anemia")

    features = [bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc, sod, pot, hemo, pcv, wc, rc, htn, dm, cad, appet, pe, ane
                ]

    # tombol prediksi
    if st.button("Prediksi"):
        prediction, score = predict(x, y, features)
        score = score
        st.info("Prediksi Sukses")

        if (prediction == 1):
            st.warning(
                "Pasien memiliki risiko tinggi untuk mengalami penyakit ginjal")
        else:
            st.success("Pasien relatif aman dari penyakit ginjal")

        st.write("Model yang digunakan memiliki tingkat akurasi ",
                 (score*100), "%")
