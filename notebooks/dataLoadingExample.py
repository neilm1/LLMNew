from transformers import pipeline

# Defining main function
def main():


    # Load the language model pipeline
    model = "gpt2"  # Example model name, you can choose any model available on Hugging Face
    lm_pipeline = pipeline("text-generation", model=model)

    # Generate text using the language model
    prompt = "Once upon a time"
    generated_text = lm_pipeline(prompt, max_length=50, num_return_sequences=1)

    # Print the generated text
    print(generated_text[0]["generated_text"])


# Using the special variable
# __name__
if __name__=="__main__":
    main()