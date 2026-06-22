# Homework 1: Building an Agentic RAG System from Scratch

Project ini adalah implementasi sistem **Retrieval-Augmented Generation (RAG)** yang dikembangkan secara bertahap dari sistem pencarian statis hingga menjadi **Agentic RAG** yang dinamis berbasis LLM Gemini (menggunakan OpenAI-compatible client).

## 🚀 Ringkasan Pengerjaan

Dataset yang digunakan dalam eksperimen ini adalah seluruh halaman modul materi pelajaran (*lesson pages* dalam format Markdown) yang ditarik langsung dari repositori kursus GitHub `DataTalksClub/llm-zoomcamp` pada commit spesifik `8c1834d`.

Berikut adalah tahapan eksperimen yang dilakukan di dalam `homework_1.ipynb`:

### 1. Data Preparation & Exploration (Q1)
* Mengunduh materi pelajaran dari GitHub menggunakan `gitsource.GithubRepositoryDataReader`.
* Mem-parsing dokumen teks mentah menjadi basis pengetahuan (*knowledge base*).
* **Hasil:** Berhasil mengumpulkan **72** halaman dokumen pelajaran.

### 2. Basic Indexing & Information Retrieval (Q2)
* Membangun mesin pencari lokal berbasis memori menggunakan `minsearch`.
* Melakukan indeks pada kolom `content` (sebagai text field) dan `filename` (sebagai keyword field).
* Menguji pencarian dengan query: *"How does the agentic loop keep calling the model until it stops?"*
* **Hasil:** Dokumen paling relevan yang ditemukan berada pada file `01-agentic-rag/lessons/14-agentic-loop.md`.

### 3. Plain RAG Implementation & Token Metrics (Q3)
* Membangun *pipeline* RAG dasar dengan menggabungkan dokumen utuh hasil pencarian ke dalam prompt instruksi.
* Mengirim prompt tersebut ke model `gemini-2.5-flash` menggunakan OpenAI Client wrapper.
* **Hasil:** Sistem berhasil menjawab dengan konteks penuh, menghabiskan sekitar **11.461 input tokens** (berada pada skala terdekat opsi **7.000** di lembar soal).

### 4. Text Chunking Optimization (Q4 & Q5)
* Mengoptimalkan presisi pencarian dan efisiensi biaya dengan memotong dokumen panjang menggunakan teknik *sliding window* (`size=2000` karakter, `step=1000` karakter overlap).
* **Hasil Q4:** Dokumen berhasil dipecah menjadi **295 chunks**.
* **Hasil Q5:** Pengujian RAG ulang menggunakan indeks beralih ke basis *chunks* berhasil menurunkan konsumsi *prompt tokens* secara drastis menjadi **5.339 tokens** (Lebih hemat ~2x lipat, atau memilih opsi terdekat **3× fewer** pada soal).

### 5. Transition to Agentic RAG (Q6)
* Mengubah sistem RAG statis menjadi Agen Mandiri (*Agentic Loop*).
* Memberikan hak akses kepada Gemini untuk memanggil fungsi pencarian teks (`search_course_material`) sebagai sebuah *Tool* secara dinamis.
* Memberikan instruksi sistem agar LLM mengeksplorasi materi dengan berbagai kata kunci sebelum memberikan konklusi akhir.
* **Hasil:** Agen secara cerdas memutuskan untuk melakukan **2 kali pemanggilan alat** (menggunakan kata kunci `'agentic loop'` dan `'RAG pipeline'`) sebelum berhasil menyusun jawaban komprehensif (opsi terdekat pada lembar soal adalah **4**).

## 🛠️ Tech Stack & Environment
* **Language:** Python 3.12 (Managed via `uv` package manager)
* **Environment:** GitHub Codespaces (Ubuntu Linux cloud container)
* **LLM Provider:** Google Gemini API (`gemini-2.5-flash`) via `openai` client library
* **Libraries:** `gitsource`, `minsearch`, `python-dotenv`, `ipykernel`

---
*Project ini diselesaikan sebagai bagian dari pemenuhan tugas Module 1 - Agentic RAG pada LLM Zoomcamp.*
