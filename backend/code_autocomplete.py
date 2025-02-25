from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "bigcode/starcoder"  # Free & Open-source model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)


def get_suggestions(code_snippet):
    inputs = tokenizer(code_snippet, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=50)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
