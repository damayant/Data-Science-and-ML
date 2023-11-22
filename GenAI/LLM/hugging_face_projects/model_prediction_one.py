from transformers import pipeline

model = pipeline("text-generation")


def predict(prompt):
    completion = model(prompt)[0]["generated_text"]
    print(completion)
    return completion

predict("My favorite food is")