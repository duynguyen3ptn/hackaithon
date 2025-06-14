from typing import Optional
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import SYSTEM_INSTRUCTION, SCRIPT1, SCRIPT2

# Load environment variables
load_dotenv()

# Configuration
API_KEY = os.getenv('GEMINI_API_KEY')
MODEL_NAME = "gemini-2.0-flash"

def init_client() -> genai.Client:
    """Initialize the Gemini AI client."""
    return genai.Client(api_key=API_KEY)

def analyze_meeting_transcript(client: genai.Client, transcript: str) -> Optional[str]:
    """
    Analyze meeting transcript using Gemini AI.
    
    Args:
        client: Gemini AI client
        transcript: Meeting transcript text
    
    Returns:
        Analysis result or None if failed
    """
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION),
            contents=transcript
        )
        return response.text
    except Exception as e:
        print(f"Error analyzing transcript: {e}")
        return None

def main():
    client = init_client()
    
    # Analyze transcripts
    result = analyze_meeting_transcript(client, SCRIPT2)
    if result:
        print(result)

if __name__ == "__main__":
    main()