from typing import Optional, NamedTuple, List, Dict
import os
import pandas as pd
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

class MeetingAnalysis(NamedTuple):
    summary: str
    action_items: list[str]

def parse_result(response: str) -> MeetingAnalysis:
    """Parse the AI response into summary and action items."""
    summary = ""
    action_items = []
    
    current_section = None
    for line in response.split('\n'):
        if '📝 Summary:' in line:
            current_section = 'summary'
        elif '✅ Action Items:' in line:
            current_section = 'action_items'
        elif line.strip() and current_section:
            if current_section == 'summary':
                summary += line.strip() + '\n'
            elif current_section == 'action_items' and line.startswith('-'):
                action_items.append(line.strip())
    
    return MeetingAnalysis(summary.strip(), action_items)

def analyze_meeting_transcript(client: genai.Client, transcript: str) -> Optional[MeetingAnalysis]:
    """
    Analyze meeting transcript using Gemini AI.
    
    Args:
        client: Gemini AI client
        transcript: Meeting transcript text
    
    Returns:
        MeetingAnalysis object or None if failed
    """
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            config=types.GenerateContentConfig(
                temperature=0,
                system_instruction=SYSTEM_INSTRUCTION),
            contents=transcript
        )
        return parse_result(response.text)
    except Exception as e:
        print(f"Error analyzing transcript: {e}")
        return None

def parse_action_items_for_csv(action_items: List[str]) -> List[Dict]:
    """Parse action items into structured format for CSV."""
    parsed_items = []
    for item in action_items:
        # Remove the leading dash if present
        item = item.lstrip('- ')
        # Split by — (em dash) or - (hyphen)
        parts = [p.strip() for p in item.replace('—', '-').split('-')]
        
        task = parts[0] if len(parts) > 0 else ""
        person = parts[1] if len(parts) > 1 else ""
        deadline = parts[2] if len(parts) > 2 else ""
        
        parsed_items.append({
            "Task": task,
            "Responsible Person": person,
            "Deadline": deadline
        })
    return parsed_items

def export_to_csv(analysis: MeetingAnalysis, filename: str = "meeting_actions.csv"):
    """Export action items to CSV file."""
    parsed_items = parse_action_items_for_csv(analysis.action_items)
    df = pd.DataFrame(parsed_items)
    df.to_csv(filename, index=False)
    return filename