import streamlit as st

def init_session_state():
    """Menginisialisasi state untuk jumlah item dinamis (max 5)"""
    defaults = {
        'edu_count': 1,
        'exp_count': 1,
        'proj_count': 1,
        'ach_count': 1,  # Tambahan baru untuk Achievements
        'skill_count': 1,
        'cert_count': 1,
        'lang_count': 1
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value