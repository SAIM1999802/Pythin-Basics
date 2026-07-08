from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

client = genai.Client(
    api_key="AQ.Ab8RN6J4l2TrZlHJ8Khl-O8avjorRD7KyP6b6U0UkuLjJP84Lg"
)

def generate(ingredients, cuisine, diet):
    prompt = f'''
    Generate one food recipe using these ingredients: {','.join(ingredients)}
    Recipe should not be more than 100 words.
    Cuisine: {cuisine}
    Diet: {diet}
    '''
try:
    # CORRECT METHOD: Use generate_content
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    
    # CORRECT ACCESS: Use response.text
    print(response.text)
except Exception as e:
   print(f"madmnfskf")
# Test the function
generate(["Tomatoes", "Lentils", "onion", "jeera", "salt"], "indian", "vegan")


generate(["Corn", "black beans","Avocado"], "Mexican", "vegan")

