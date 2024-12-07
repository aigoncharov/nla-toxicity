from transformers import pipeline

classifier = pipeline(
    "text-classification", model="j-hartmann/emotion-english-distilroberta-base"
)
