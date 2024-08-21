import os
from mistralai import Mistral
from functools import lru_cache
api_key = os.environ.get("MISTRAL_API_KEY", "XXXXXXXXXXXXXXXXXX")
model = "mistral-large-latest"

client = Mistral(api_key=api_key)
def generate_summary_prompt(transcript_text, summary_length="brief", focus_points="main ideas", 
                            tone="neutral", audience="general public", additional_instructions="", 
                            output_format="paragraphs"):
    """
    Generate a summary prompt using the given template.
    
    :param transcript_text: The full transcript of the video.
    :param summary_length: Desired length of the summary (e.g., "brief," "detailed," "200 words").
    :param focus_points: Aspects of the video to emphasize in the summary (e.g., "main ideas," "key takeaways").
    :param tone: The tone of the summary (e.g., "formal," "informal," "neutral").
    :param audience: The target audience for the summary (e.g., "general public," "students").
    :param additional_instructions: Any special instructions for the summary.
    :param output_format: Preferred format for the summary (e.g., "paragraphs," "bullet points").
    
    :return: A formatted prompt string.
    """
    
    template = f"""
    Summarize the following transcript of a video. In not more than 250 words. 
    The summary should be concise and capture the key points discussed in the video. 
    
    **Transcript:**
    {transcript_text}

    **Summary Requirements:**
    1. Length: {summary_length}
    2. Focus on: {focus_points}
    3. Tone: {tone}
    4. Audience: {audience}
    5. Additional Instructions: {additional_instructions}

    Provide the summary in {output_format}.
    """ 
    
    return template.strip()

@lru_cache()
def summarize(transcript):
    try:
        chat_response = client.chat.complete(
                                                model = model,
                                                messages = [
                                                    {
                                                        "role": "user",
                                                        "content": generate_summary_prompt(transcript),
                                                    },
                                                ]
                                            )
        response = chat_response.choices[0].message.content
        return {"summary": response}
    except Exception as e:
        print(f"Error when requesting llms : {e}")
        return {}