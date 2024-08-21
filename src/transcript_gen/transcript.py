from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter

def extract_video_id(url: str) -> str:
    """
    Extracts the video ID from a given YouTube URL.
    Supports various YouTube URL formats.
    """
    import re
    # Regex patterns for different YouTube URL formats
    patterns = [
        r"youtu\.be/([a-zA-Z0-9_-]+)",
        r"youtube\.com/watch\?v=([a-zA-Z0-9_-]+)",
        r"youtube\.com/embed/([a-zA-Z0-9_-]+)",
        r"youtube\.com/v/([a-zA-Z0-9_-]+)"
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

def get_transcript(url):
    print(url)
    video_id = ""
    try:
        # Extract video ID from URL
        video_id = extract_video_id(url)
        if not video_id:
            raise Exception("Invalid YouTube URL")
        
        # Fetch the transcript
        # transcript = YouTubeTranscriptApi.get_transcript(video_id)
        # 45.127.248.127:5128:qoluvhjw:xf9em39t6bn5
        transcript = YouTubeTranscriptApi.get_transcript(video_id, proxies={"https": "http://qoluvhjw:xf9em39t6bn5@45.127.248.127:5128"})
        transcription = " ".join(row['text'] for row in transcript)
        # Format transcript as JSON
        # formatter = JSONFormatter()
        # formatted_transcript = formatter.format_transcript(transcript)
        
        return {"transcript": transcription}
    except Exception as e:
        raise Exception(str(e) + video_id)


if __name__ == "__main__":
    url = "https://youtu.be/67_aMPDk2zw?si=45Ok41iYPQOatTB-"
    transcript = get_transcript(url)
    print(transcript)