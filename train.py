# train.py
from datasets import load_dataset
from transformers import AutoModelForSeq2SeqLM, Trainer, TrainingArguments

def train_model():
    """Melatih model menggunakan dataset yang ada"""
    dataset = load_dataset("json", data_files={"train": "dataset/dataset.json"})
    
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
    training_args = TrainingArguments(
        output_dir="./model",
        evaluation_strategy="epoch",
        per_device_train_batch_size=4,
        num_train_epochs=3,
        logging_dir="./logs",
    )
    
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset["train"],
    )
    
    trainer.train()
    model.save_pretrained("./model")
