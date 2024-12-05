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

        rbc = st.selectbox("Masukkan Red Blood Cells", ["normal", "abnormal"])
        rbc = 1 if rbc == "normal" else 0

        pc = st.selectbox("Masukkan Pus Cell", ["normal", "abnormal"])
        pc = 1 if pc == "normal" else 0

        pcc = st.selectbox("Masukkan Pus Cell Clumps",
                           ["present", "not present"])
        pcc = 1 if pcc == "present" else 0

        ba = st.selectbox("Masukkan Bacteria", ["present", "not present"])
        ba = 1 if ba == "present" else 0
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

        htn = st.selectbox("Masukkan Hypertension", ["yes", "no"])
        htn = 1 if htn == "yes" else 0

        dm = st.selectbox("Masukkan Diabetes Melitus", ["yes", "no"])
        dm = 4 if dm == "yes" else 3

        cad = st.selectbox("Masukkan Coronary Artery Disease", ["yes", "no"])
        cad = 1 if cad == "no" else 2

        appet = st.selectbox("Masukkan Appetite", ["good", "poor"])
        appet = 1 if appet == "poor" else 0

        pe = st.selectbox("Masukkan Pedal Edema", ["yes", "no"])
        pe = 1 if pe == "yes" else 0

        ane = st.selectbox("Masukkan Anemia", ["yes", "no"])
        ane = 1 if ane == "yes" else 0

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
