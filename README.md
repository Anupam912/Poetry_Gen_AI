# **AI Poetry Generator**

## **Overview**

The **AI Poetry Generator** is an advanced Generative AI project that creates personalized, creative, and context-aware poetry. It leverages state-of-the-art language models and interactive features to deliver a captivating poetry generation experience.

The project offers multiple enhancements, including:

- **Intelligent Prompt Suggestions**: Offers creative prompts to inspire poetry.
- **Adaptive Learning**: Customizes output based on user-uploaded poetry.
- **Emotion and Sentiment-Based Customization**: Tailors poems to the user's mood.
- **Multilingual Poetry Generation**: Supports poetry in multiple languages.

---

## **How It Works**

### **1. Dataset Collection**

The project uses datasets from various sources:

- **Scraped Poems**: Poems collected from subreddits like `r/Poetry` using the Reddit API (`PRAW` library).
- **Public Datasets**: Pre-curated poetry datasets from platforms like Kaggle.
- **User-Uploaded Poetry**: Users can upload their own poetry to personalize the generator.

### **2. Preprocessing**

- Text is cleaned and tokenized using libraries like **Hugging Face Transformers**.
- Special formats (e.g., Haiku or Sonnet) are preprocessed to retain structure and style.

### **3. Model Architecture**

- **GPT-4**: Fine-tuned on poetry datasets to generate creative and coherent poetry.
- **mBART**: Used for multilingual poetry generation, enabling cultural and linguistic diversity.
- **Sentiment Analysis Model**: Detects user emotions to influence the theme and tone of the generated poems.

### **4. Generation Process**

1. Users input a **prompt**, **theme**, and **style**, which is passed to the model.
2. The model generates poems dynamically, incorporating user preferences and contextual information.
3. AI-generated visuals or narration can accompany the output for an enhanced experience.

### **5. Adaptive Learning**

- The system allows users to upload their own poetry.
- Fine-tuning is performed on these uploads using lightweight methods like **PEFT (Parameter-Efficient Fine-Tuning)** or **LoRA (Low-Rank Adaptation)**.

---

## **How to Run the Project**

### **1. Clone the Repository**

```bash
git clone https://github.com/your-repo/poetry-generator.git
cd poetry-generator
```

### **2. Install Dependencies**

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

### **Start the server and access the application**

```bash
python app.py
```
