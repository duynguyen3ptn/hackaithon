from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from main import init_client, analyze_meeting_transcript, parse_action_items_for_csv
from utils import convert_vtt_to_text
import pandas as pd

app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze_transcript():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    vtt_content = file.read().decode('utf-8')
    
    # Convert VTT to plain text
    transcript = convert_vtt_to_text(vtt_content)
    
    client = init_client()
    result = analyze_meeting_transcript(client, transcript)
    
    if result:
        return jsonify({
            'summary': result.summary,
            'action_items': result.action_items
        })
    return jsonify({'error': 'Analysis failed'}), 500

@app.route('/download-csv', methods=['POST'])
def download_csv():
    try:
        data = request.get_json()
        action_items = data.get('action_items', [])
        
        parsed_items = parse_action_items_for_csv(action_items)
        df = pd.DataFrame(parsed_items)
        
        # Convert DataFrame to CSV string
        csv_data = df.to_csv(index=False)
        
        return Response(
            csv_data,
            mimetype="text/csv",
            headers={"Content-disposition": "attachment; filename=action_items.csv"}
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
