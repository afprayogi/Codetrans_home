import gradio as gr
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, GenerationConfig
from config_file import MODEL_NAME, MAX_LENGTH, NUM_BEAMS, BAD_WORDS_IDS

# Fungsi untuk menerjemahkan kode
def translate_code(input_text):
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
    
    # Mengonfigurasi parameter generasi
    generation_config = GenerationConfig.from_pretrained(MODEL_NAME)
    generation_config.max_length = MAX_LENGTH
    generation_config.num_beams = NUM_BEAMS
    generation_config.bad_words_ids = BAD_WORDS_IDS
    
    # Proses input teks
    inputs = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True)
    outputs = model.generate(**inputs, generation_config=generation_config)
    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return translated_text

# Fungsi untuk menerima file dan menerjemahkan isi file
def translate_code_from_file(file):
    input_text = file.read().decode("utf-8")  # Membaca file sebagai teks
    return translate_code(input_text)

# Membuat antarmuka pengguna dengan Gradio
def create_interface():
    iface = gr.Interface(
        fn=translate_code_from_file,  # Fungsi yang akan dipanggil untuk menerjemahkan
        inputs=gr.File(label="Upload Code File"),  # Input file untuk mengunggah kode
        outputs=gr.Textbox(label="Translated Code"),  # Output terjemahan
        title="Code Translation AI",  # Judul aplikasi
        description="Aplikasi untuk menerjemahkan string di dalam kode dari bahasa Inggris ke bahasa Indonesia.",  # Deskripsi aplikasi
    )
    iface.launch()

# Menjalankan aplikasi
if __name__ == "__main__":
    create_interface()
