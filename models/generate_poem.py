from transformers import GPT2LMHeadModel, GPT2Tokenizer
from transformers_interpret import GPT2Explainer

# Load the fine-tuned model
model = GPT2LMHeadModel.from_pretrained("./personalized_model")
tokenizer = GPT2Tokenizer.from_pretrained("./personalized_model")

# Function to generate a single poem
def generate_poem(prompt, theme="nature", style="haiku", max_length=50):
    styled_prompt = f"Write a {style} poem about {theme}. {prompt}"
    inputs = tokenizer.encode(styled_prompt, return_tensors="pt")
    outputs = model.generate(
        inputs,
        max_length=max_length,
        no_repeat_ngram_size=2,
        temperature=1.0,
        top_p=0.9,
        do_sample=True
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Function to generate multiple poems
def generate_multiple_poems(prompt, theme="nature", style="haiku", num_poems=3, max_length=50):
    styled_prompt = f"Write a {style} poem about {theme}. {prompt}"
    inputs = tokenizer.encode(styled_prompt, return_tensors="pt")
    outputs = model.generate(
        inputs,
        max_length=max_length,
        num_return_sequences=num_poems,
        no_repeat_ngram_size=2,
        temperature=1.5,
        top_p=0.9,
        do_sample=True
    )
    return [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]

# Function to explain poem generation
def explain_poem(poem):
    explainer = GPT2Explainer(model, tokenizer)
    explanation = explainer(poem)
    return explanation.word_attributions
