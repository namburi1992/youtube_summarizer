import gradio as gr
import requests
# Step 1: Define a function that takes a URL as input and returns some text.
def process_url(url):
    # For demonstration purposes, let's assume it returns the URL reversed.
    host = 'http://13.88.43.229:8080/transcript'
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    data = {
        'url': url
    }

    response = requests.post(host, headers=headers, json=data)

    print(response.status_code)
    response_json = response.json()  # if the response is in JSON format
    return response_json.get('transcript')

# Step 2: Define another function that takes the text from the first function and returns another text.
def further_process_text(text, summary_length, focus_points, tone, audience, additional_instructions, output_format):
    # For demonstration purposes, let's assume it converts the text to uppercase.
    host = 'http://13.88.43.229:8080/generate'
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    data = {
        'transcript': text,
        "summary_length": summary_length,
        "focus_points": focus_points,
        "tone": tone,
        "audience": audience,
        "additional_instructions": additional_instructions,
        "output_format": output_format,
    }

    response = requests.post(host, headers=headers, json=data)

    print(response.status_code)
    response_json = response.json()  # if the response is in JSON format
    return response_json.get('summary')



# Gradio Interface
with gr.Blocks() as demo:
    # First step: Input URL and process it
    url_input = gr.Textbox(label="Enter Youtube URL")
    processed_text = gr.Textbox(label="Transcipt", lines=5)
    process_button = gr.Button("Get Transcript")
    
    process_button.click(process_url, inputs=url_input, outputs=processed_text)
    # Adding parameters for the second function
    summary_length = gr.Textbox(label="Summary Length", value="brief")
    focus_points = gr.Textbox(label="Focus Points", value="main ideas")
    tone = gr.Textbox(label="Tone", value="neutral")
    audience = gr.Textbox(label="Audience", value="general public")
    additional_instructions = gr.Textbox(label="Additional Instructions", value="")
    output_format = gr.Textbox(label="Output Format", value="paragraphs")
    # Second step: Process the text from the first step further
    further_processed_text = gr.Textbox(label="Summary", lines=5)
    further_process_button = gr.Button("Summarize")
    
    further_process_button.click(further_process_text, inputs=[processed_text, summary_length, focus_points, tone, audience, 
                                         additional_instructions, output_format], outputs=further_processed_text)

# Launch the Gradio interface
demo.launch(share=True)
