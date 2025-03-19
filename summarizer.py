from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize the client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def summarize_text(text):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes text."},
                {"role": "user", "content": f"Please summarize this text in 2-3 sentences: {text}"}
            ],
            max_tokens=150,
            temperature=0.5
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Example text - a passage about climate change
sample_text = """
The events surrounding Cambyses's death and Bardiya's succession are greatly debated as there are many conflicting accounts.[60] According to Herodotus, as Bardiya's assassination had been committed in secret, the majority of Persians still believed him to be alive. This allowed two Magi to rise up against Cambyses, with one of them sitting on the throne able to impersonate Bardiya because of their remarkable physical resemblance and shared name (Smerdis in Herodotus's accounts[d]).[76] Ctesias writes that when Cambyses had Bardiya killed he immediately put the magus Sphendadates in his place as satrap of Bactria due to a remarkable physical resemblance.[77] Two of Cambyses' confidants then conspired to usurp Cambyses and put Sphendadates on the throne under the guise of Bardiya.[78] According to the Behistun Inscription, written by the following king Darius the Great, a magus named Gaumata impersonated Bardiya and incited a revolution in Persia.[59] Whatever the exact circumstances of the revolt, Cambyses heard news of it in the summer of 522 BC and began to return from Egypt, but he was wounded in the thigh in Syria and died of gangrene, so Bardiya's impersonator became king.[79][e] The account of Darius is the earliest, and although the later historians all agree on the key details of the story, that a magus impersonated Bardiya and took the throne, this may have been a story created by Darius to justify his own usurpation.[81] Iranologist Pierre Briant hypothesises that Bardiya was not killed by Cambyses, but waited until his death in the summer of 522 BC to claim his legitimate right to the throne as he was then the only male descendant of the royal family. Briant says that although the hypothesis of a deception by Darius is generally accepted today, "nothing has been established with certainty at the present time, given the available evidence".[82]
"""

# Run the summarizer
if __name__ == "__main__":
    print("Original text:\n", sample_text)
    print("\nGenerating summary...")
    summary = summarize_text(sample_text)
    print("\nSummary:", summary)