import streamlit as st

def escape_latex(text):
    """
    Melakukan escaping pada karakter spesial LaTeX agar tidak error saat dicompile.
    """
    if not text:
        return ""
    
    # Mapping karakter spesial LaTeX
    replacements = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\textasciicircum{}',
        '\\': r'\textbackslash{}'
    }
    
    # Lakukan replace karakter
    escaped_text = "".join(replacements.get(char, char) for char in text)
    return escaped_text

def manage_count(key, operation, max_val=5):
    """Mengatur penambahan/pengurangan item dalam session state"""
    if operation == 'add' and st.session_state[key] < max_val:
        st.session_state[key] += 1
    elif operation == 'remove' and st.session_state[key] > 0:
        st.session_state[key] -= 1