LaTeX Resume Generator with Streamlit
Aplikasi berbasis web sederhana menggunakan Python (Streamlit) untuk membuat kode resume LaTeX yang teroptimasi untuk ATS (Applicant Tracking System).
Fitur
Input Dinamis: Tambah/kurang kolom untuk Pendidikan, Pengalaman, Project, dll.
ATS Optimized: Menggunakan template LaTeX yang bersih dan mudah dibaca mesin.
Live Generation: Menghasilkan kode .tex yang siap disalin ke Overleaf.
Struktur Project
app.py: Entry point aplikasi (UI Utama).
latex_generator.py: Berisi template dan logika penggabungan string LaTeX.
utils.py: Fungsi bantuan (helper functions).
session_state.py: Manajemen state sesi pengguna.
Cara Menjalankan
Clone repository ini (atau download file-filenya).
Buat Virtual Environment (Opsional tapi disarankan):
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate


Install Dependencies:
pip install -r requirements.txt


Jalankan Aplikasi:
streamlit run app.py


Cara Menggunakan
Isi form yang tersedia di sebelah kanan.
Klik tombol GENERATE LATEX CODE.
Copy kode yang dihasilkan.
Paste di Overleaf (Buat Blank Project).
Compile dan Download PDF.
