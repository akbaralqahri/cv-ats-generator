import streamlit as st
from session_state import init_session_state
from utils import manage_count
from latex_generator import generate_full_latex

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="LaTeX Resume Generator",
    page_icon="📄",
    layout="wide"
)

def main():
    init_session_state()

    # Sidebar: Instruksi
    with st.sidebar:
        st.header("📌 Cara Penggunaan")
        st.info("""
        1. **Isi Form**: Lengkapi data di tab sebelah kanan. Kolom bertanda (*) wajib diisi.
        2. **Generate**: Jika semua data wajib terisi, kode LaTeX akan muncul di bagian bawah.
        3. **Copy Code**: Salin kode yang dihasilkan.
        4. **Buka Overleaf**: Pergi ke [Overleaf.com](https://www.overleaf.com).
        5. **New Project**: Buat 'Blank Project'.
        6. **Paste & Compile**: Tempel kode di editor Overleaf dan klik 'Recompile'.
        7. **Download PDF**: Unduh hasil resume PDF Anda.
        """)
        st.warning("⚠️ Fitur: Maksimal 5 item untuk Pendidikan, Pengalaman, dan Project agar muat di 1 halaman.")
        st.markdown("---")
        st.markdown("© 2025 @akbaralqahri | Developed for research and educational purposes.")


    st.title("📄 LaTeX Resume Generator")
    st.markdown("Buat resume profesional standar ATS (Applicant Tracking System) tanpa perlu coding LaTeX manual.")

    # --- FORM INPUT ---
    with st.form("resume_form"):
        st.subheader("1. Informasi Dasar (Wajib *)")
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Nama Lengkap *", placeholder="Contoh: Budi Santoso")
            title = st.text_input("Judul/Posisi yang Dilamar", placeholder="Contoh: Data Analyst")
            email = st.text_input("Email *", placeholder="email@contoh.com")
        with col2:
            phone = st.text_input("Nomor Telepon *", placeholder="0812-3456-7890")
            linkedin = st.text_input("Link LinkedIn *", placeholder="https://linkedin.com/in/budisantoso")
            portfolio = st.text_input("Link Portfolio *", placeholder="https://budisantoso.com")
        
        st.subheader("2. Professional Summary")
        summary = st.text_area("Ringkasan Diri", placeholder="Jelaskan secara singkat pengalaman dan keahlian Anda...", height=100)

        # --- EDUCATION (Dynamic) ---
        st.markdown("---")
        st.subheader("3. Pendidikan (Max 5)")
        education_data = []
        for i in range(st.session_state.edu_count):
            st.markdown(f"**Pendidikan #{i+1}**")
            c1, c2, c3, c4 = st.columns(4)
            deg = c1.text_input(f"Gelar #{i+1}", placeholder="B.Sc Computer Science")
            inst = c2.text_input(f"Institusi #{i+1}", placeholder="Universitas Indonesia")
            loc = c3.text_input(f"Kota #{i+1}", placeholder="Depok, Indonesia")
            per = c4.text_input(f"Periode #{i+1}", placeholder="2020 -- 2024")
            if deg and inst:
                education_data.append({'degree': deg, 'institution': inst, 'location': loc, 'period': per})
        
        ce1, ce2 = st.columns([1, 5])
        with ce1:
            add_edu = st.form_submit_button("➕ Tambah Pendidikan")
        if add_edu:
            manage_count('edu_count', 'add')
            st.rerun()

        # --- EXPERIENCE (Dynamic) ---
        st.markdown("---")
        st.subheader("4. Pengalaman Kerja (Max 5)")
        experience_data = []
        for i in range(st.session_state.exp_count):
            st.markdown(f"**Pengalaman #{i+1}**")
            c1, c2 = st.columns(2)
            role = c1.text_input(f"Posisi #{i+1}", placeholder="Junior Developer")
            comp = c2.text_input(f"Perusahaan #{i+1}", placeholder="Tokopedia")
            c3, c4 = st.columns(2)
            loc = c3.text_input(f"Lokasi Kerja #{i+1}", placeholder="Jakarta")
            per = c4.text_input(f"Periode Kerja #{i+1}", placeholder="Jan 2023 -- Sekarang")
            resp = st.text_area(f"Tanggung Jawab #{i+1} (Satu poin per baris)", placeholder="- Membuat fitur baru\n- Optimasi database", height=100)
            
            if role and comp:
                experience_data.append({'position': role, 'company': comp, 'location': loc, 'period': per, 'responsibilities': resp})

        cx1, cx2 = st.columns([1, 5])
        with cx1:
            add_exp = st.form_submit_button("➕ Tambah Pengalaman")
        if add_exp:
            manage_count('exp_count', 'add')
            st.rerun()

        # --- PROJECTS (Dynamic) ---
        st.markdown("---")
        st.subheader("5. Proyek (Max 5)")
        project_data = []
        for i in range(st.session_state.proj_count):
            st.markdown(f"**Proyek #{i+1}**")
            c1, c2 = st.columns([3, 1])
            title_proj = c1.text_input(f"Nama Proyek #{i+1}", placeholder="Sistem Prediksi Harga Rumah")
            year_proj = c2.text_input(f"Tahun #{i+1}", placeholder="2024")
            tech_proj = st.text_input(f"Teknologi #{i+1}", placeholder="Python, Scikit-Learn, Streamlit")
            desc_proj = st.text_area(f"Deskripsi Proyek #{i+1} (Satu poin per baris)", placeholder="- Mengembangkan model ML dengan akurasi 95%", height=80)
            
            if title_proj:
                project_data.append({'title': title_proj, 'year': year_proj, 'tech': tech_proj, 'description': desc_proj})

        cp1, cp2 = st.columns([1, 5])
        with cp1:
            add_proj = st.form_submit_button("➕ Tambah Proyek")
        if add_proj:
            manage_count('proj_count', 'add')
            st.rerun()

        # --- SKILLS ---
        st.markdown("---")
        st.subheader("6. Keahlian (Skills)")
        sk1, sk2 = st.columns(2)
        s_data = sk1.text_input("Data Analysis Skills", placeholder="Python (Pandas), SQL, Excel")
        s_ml = sk2.text_input("Machine Learning Skills", placeholder="Scikit-Learn, TensorFlow")
        s_ai = sk1.text_input("AI & Automation", placeholder="LLM, Selenium, Zapier")
        s_biz = sk2.text_input("Business Skills", placeholder="Communication, Project Management")
        
        skills_data = {
            'data_analysis': s_data, 'ml': s_ml, 'ai': s_ai, 'business': s_biz
        }

        # --- CERTIFICATIONS & LANGUAGES ---
        st.markdown("---")
        col_c, col_l = st.columns(2)
        
        with col_c:
            st.subheader("7. Sertifikasi")
            cert_list = []
            for i in range(st.session_state.cert_count):
                cert = st.text_input(f"Sertifikat #{i+1}", key=f"cert_{i}")
                cert_list.append(cert)
            if st.form_submit_button("➕ Sertifikat"):
                manage_count('cert_count', 'add')
                st.rerun()

        with col_l:
            st.subheader("8. Bahasa")
            lang_list = []
            for i in range(st.session_state.lang_count):
                lang = st.text_input(f"Bahasa #{i+1}", key=f"lang_{i}")
                lang_list.append(lang)
            if st.form_submit_button("➕ Bahasa"):
                manage_count('lang_count', 'add')
                st.rerun()

        # --- FINAL SUBMIT ---
        st.markdown("---")
        submitted = st.form_submit_button("🚀 GENERATE LATEX CODE", type="primary")

    # --- OUTPUT LOGIC ---
    if submitted:
        # Validasi Input Wajib
        if not (name and email and linkedin and portfolio and phone):
            st.error("❌ Mohon lengkapi semua data wajib di bagian Informasi Dasar!")
        else:
            # Susun Data
            full_data = {
                'name': name,
                'title': title,
                'email': email,
                'linkedin': linkedin,
                'portfolio': portfolio,
                'phone': phone,
                'summary': summary,
                'education': education_data,
                'experience': experience_data,
                'projects': project_data,
                'skills': skills_data,
                'certifications': cert_list,
                'languages': lang_list
            }

            # Generate Code
            latex_code = generate_full_latex(full_data)
            
            # Tampilkan Hasil
            st.success("✅ Kode berhasil dibuat! Silakan salin kode di bawah ini:")
            st.code(latex_code, language='latex')
            
            # Download Button
            st.download_button(
                label="📥 Download File .tex",
                data=latex_code,
                file_name="resume.tex",
                mime="text/x-tex"
            )

if __name__ == "__main__":
    main()