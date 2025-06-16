def convert_vtt_to_text(vtt_content: str) -> str:
    """Convert VTT content to plain text."""
    lines = vtt_content.split('\n')
    text_lines = []
    
    for line in lines:
        # Skip WebVTT header, timestamps and empty lines
        if (not line.strip() or 
            line.startswith('WEBVTT') or 
            '-->' in line or 
            line[0].isdigit()):
            continue
        text_lines.append(line.strip())
    
    return ' '.join(text_lines)
