from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, GenerationConfig
from config_file import MODEL_NAME, MAX_LENGTH, NUM_BEAMS, BAD_WORDS_IDS

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

def translate_strings(strings):
    generation_config = GenerationConfig.from_pretrained(MODEL_NAME)
    generation_config.max_length = MAX_LENGTH
    generation_config.num_beams = NUM_BEAMS
    generation_config.bad_words_ids = BAD_WORDS_IDS

    translations = []
    for text in strings:
        inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        outputs = model.generate(**inputs, generation_config=generation_config)
        translation = tokenizer.decode(outputs[0], skip_special_tokens=True)
        translations.append(translation)
    return translations
