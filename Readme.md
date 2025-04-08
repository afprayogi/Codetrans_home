# DeepLearning Translate

Proyek ini bertujuan untuk menerjemahkan string/text yang terdapat dalam file kode (seperti Python, JavaScript, HTML, dsb) dari bahasa Inggris ke bahasa Indonesia, tanpa mengubah struktur kode.

## Fitur Utama
- Mengekstrak semua teks di dalam tanda kutip dari berbagai file kode
- Menerjemahkan teks menggunakan model dari Hugging Face
- Menyimpan hasil terjemahan dengan struktur kode yang tetap
- Mendeteksi string yang tidak berubah (misalnya hasil translate sama dengan teks aslinya) sebagai calon data latih tambahan
- Mendukung fine-tuning model untuk meningkatkan akurasi terjemahan berdasarkan dataset pribadi

## Struktur Folder
```
project/
├── input/               # File kode sumber
├── output/              # Hasil terjemahan
├── dataset/             # Dataset pasangan string
├── model/               # Model yang telah dilatih
├── config_file.py       # Konfigurasi program
├── extract_text.py      # Ekstraksi string dari file
├── translate.py         # Proses penerjemahan
├── train.py             # Fine-tuning model
├── utils.py             # Fungsi bantu
├── main.py              # Program utama
└── requirements.txt     # Daftar pustaka Python
```

## Model Hugging Face
Proyek ini menggunakan model dari Hugging Face:

**Model**: [`Helsinki-NLP/opus-mt-en-id`](https://huggingface.co/Helsinki-NLP/opus-mt-en-id)  
**Pemilik**: [Helsinki-NLP](https://huggingface.co/Helsinki-NLP)

Model ini adalah bagian dari OPUS-MT, yang merupakan kumpulan model terjemahan berbasis MarianMT untuk berbagai pasangan bahasa. 

Digunakan melalui library `transformers` dari Hugging Face:
```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-id")
tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-id")
```

## Instalasi
```bash
pip install -r requirements.txt
```

## Menjalankan Proyek
```bash
python main.py
```

## Lisensi
Proyek ini menggunakan lisensi MIT. Bebas digunakan, dimodifikasi, dan didistribusikan dengan tetap mencantumkan kredit pembuat.

---

> Dibuat dengan semangat pembelajaran dan eksplorasi oleh afprayogi.
> 
> Telah dibantu dengan ChatGPT agar tidak mengurangi rasa hormat kepada semua kontributor dan teknologi yang mendukung proyek ini.

