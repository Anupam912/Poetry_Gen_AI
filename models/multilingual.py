from transformers import MBartForConditionalGeneration, MBartTokenizer

# Load multilingual model
tokenizer = MBartTokenizer.from_pretrained("facebook/mbart-large-cc25")
model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-cc25")

# Function to generate a poem in a specific language
def generate_poem_in_language(prompt, target_language="fr"):
    inputs = tokenizer(prompt, return_tensors="pt")
    translated = model.generate(inputs["input_ids"], forced_bos_token_id=tokenizer.lang_code_to_id[target_language])
    return tokenizer.decode(translated[0], skip_special_tokens=True)
