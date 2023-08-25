import streamlit as st
import openai


openai.api_key = "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"


# Streamlit app UI
def main():
    st.title("Localized Script Generator")

    user_input = st.text_area("Enter the demo script in English:", "")
    user_selected_language = st.selectbox("Select target language:", ["french", "spanish", "russian"])
    user_selected_country = st.text_input("Enter country for names:", "")

    if st.button("Generate Localized Script"):
        translated_script = translate_with_llm(user_input, user_selected_language)
        localized_script = replace_names(translated_script, user_selected_country)
        st.text("Localized Script:")
        st.text(localized_script)
def replace_names(script,country):
    localized_script = script
    return localized_script



def translate_with_llm(text, target_language):
    prompt = f"Translate the following English text to {target_language}: '{text}'"
    try:
        response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        max_tokens=50
        )
        translated_text = response.choices[0].text.strip()
        return translated_text
    except openai.error.RateLimitError as e:
        st.error(f"An error occurred: {e}")
        return ""





if __name__ == "__main__":
    main()
