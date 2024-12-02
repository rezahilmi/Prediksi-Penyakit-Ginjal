import warnings
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn.metrics import confusion_matrix
from sklearn import tree
import streamlit as st

from web_functions import train_model


def app(df, x, y):
    warnings.filterwarnings('ignore')
    # st.set_option('deprecation.showPyplotGlobalUse', False)

    st.title("Visualisasi Prediksi Batu Ginjal")

    if st.checkbox("Plot Confusion Matrix"):
        model, score = train_model(x, y)
        y_pred = model.predict(x)
        cm = confusion_matrix(y, y_pred)

        fig, ax = plt.subplots(figsize=(10, 6))
        sn.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=[
            'CKD', 'No CKD'], yticklabels=['CKD', 'No CKD'], ax=ax)
        st.pyplot(fig)

    if st.checkbox("Plot Decision Tree"):
        model, score = train_model(x, y)
        dot_data = tree.export_graphviz(
            decision_tree=model, max_depth=3, out_file=None, filled=True, rounded=True, feature_names=x.columns, class_names=['nockd', 'ckd']
        )

        st.graphviz_chart(dot_data)
