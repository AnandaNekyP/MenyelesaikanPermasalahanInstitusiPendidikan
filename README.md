# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Perusahaan Edutech ini menghadapi masalah dropout siswa yang dapat berdampak pada reputasi perusahaan, retensi pengguna, dan keberlanjutan bisnis. Tingginya tingkat dropout juga memengaruhi tujuan sosial perusahaan untuk menyediakan pendidikan yang inklusif dan merata. Oleh karena itu, diperlukan analisis mendalam untuk memahami penyebab utama dropout dan pengembangan sistem berbasis teknologi yang dapat membantu perusahaan mengambil langkah-langkah preventif.

### Permasalahan Bisnis

- Identifikasi Penyebab Dropout: Apa saja faktor yang paling signifikan dalam menentukan apakah seorang siswa akan dropout?
- Mencari Insight Data: Bagaimana data yang tersedia dapat memberikan informasi kepada manajemen untuk membuat keputusan strategis?
- Prediksi Dropout: Bagaimana cara memprediksi risiko dropout siswa sehingga langkah pencegahan dapat dilakukan lebih dini?

### Cakupan Proyek

- Data Understanding & Preprocessing:
    - Menganalisis pola dropout siswa berdasarkan demografi, performa akademik, dan kondisi sosial-ekonomi.
    - Membersihkan dan memproses data untuk menghilangkan inkonsistensi.
- Pembuatan Dashboard:
    - Membuat dashboard interaktif untuk menyajikan data dropout siswa secara visual dan membantu pengambilan keputusan.
- Pengembangan Model Machine Learning:
    - Mengembangkan sistem prediksi berbasis machine learning untuk mengidentifikasi siswa berisiko tinggi.
- Implementasi & Rekomendasi:
    - Memberikan rekomendasi berbasis data untuk menyelesaikan permasalahan dropout.

### Persiapan

Sumber data: [Source](https://doi.org/10.24432/C5MC89.)

Setup environment:

```bash
pip install -r requirements.txt
```

## Business Dashboard

Deskripsi Dashboard:
Dashboard interaktif ini memberikan gambaran lengkap tentang penyebab dropout siswa.

Data visualisasi meliputi:

- Distribusi Status Siswa Berdasarkan Jenis Kelamin:
  - Laki-laki:
    - Dropout: 45.1%
    - Graduate: 35.2%
    - Enrolled: 19.7%
  - Perempuan:
    - Dropout: 25.1%
    - Graduate: 57.9%
    - Enrolled: 17.0%

Insight: Laki-laki lebih cenderung dropout dibandingkan perempuan. Program mentoring tambahan dapat difokuskan pada siswa laki-laki.

Faktor Kualifikasi Orang Tua:
Dropout lebih tinggi terjadi pada siswa dengan orang tua yang memiliki tingkat pendidikan rendah, khususnya pada kualifikasi pendidikan dasar.

Mode Aplikasi Pendaftaran:
Beberapa mode aplikasi tertentu menunjukkan tingkat dropout yang signifikan lebih tinggi dibandingkan yang lain. Hal ini perlu ditinjau kembali.

Usia Siswa Saat Pendaftaran:
Siswa yang dropout memiliki rata-rata usia 26 tahun, lebih tua dibandingkan siswa yang graduate (21.78 tahun) dan enrolled (22.37 tahun).

Kebutuhan Khusus (Special Needs):
Dari total siswa yang dropout, mayoritas tidak memiliki kebutuhan khusus. Namun, siswa dengan kebutuhan khusus juga menunjukkan dropout kecil (17 kasus).

Status Hutang:
78% siswa yang dropout tidak memiliki hutang, sementara 22% memiliki status hutang. Hal ini menunjukkan faktor sosial-ekonomi perlu dianalisis lebih dalam.

## Menjalankan Sistem Machine Learning

Jelaskan cara menjalankan protoype sistem machine learning yang telah dibuat. Selain itu, sertakan juga link untuk mengakses prototype tersebut.

``` bash
streamlit run app.py
```

link streamlit : [Streamlit](https://anandanekyp-menyelesaikanpermasalahaninstitusipendid-app-zu5akm.streamlit.app/)

## Conclusion

Tingkat dropout siswa dipengaruhi oleh:
- Jenis kelamin (laki-laki lebih cenderung dropout).
- Usia saat pendaftaran (usia lebih tua lebih cenderung dropout).
- Kualifikasi pendidikan orang tua.
- Mode aplikasi saat pendaftaran.
- Kondisi sosial-ekonomi seperti tingkat inflasi dan pengangguran turut memengaruhi dropout siswa.

### Rekomendasi Action Items
- Fokus pada Kelompok Risiko Tinggi:
Memberikan dukungan tambahan untuk siswa laki-laki, terutama mereka yang memiliki orang tua dengan pendidikan rendah.
- Optimasi Proses Pendaftaran:
Mengevaluasi mode aplikasi dengan dropout tinggi dan memperbaiki pengalaman pengguna pada proses tersebut.
- Program Khusus untuk Siswa Tua:
Menyediakan mentoring atau program tambahan untuk siswa berusia lebih tua (di atas 25 tahun).
- Kolaborasi dengan Orang Tua:
Mengadakan workshop atau seminar untuk meningkatkan keterlibatan orang tua dalam pendidikan siswa.

