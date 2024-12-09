import requests
import json
import gradio as gr

url = "http://localhost:11434/api/generate"

headers = {
    "Content-Type": "application/json",
}

# data = {
#    "model": "mistral",
#   "stream": False,
#    "prompt": "Why is the sky blue?",
# }


def generate_response(prompt):
    data = {
        "model": "mistral",
        "stream": False,
        "prompt": prompt,
    }

    response = requests.post(url, data=json.dumps(data), headers=headers)

    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data["response"]
        return actual_response
    else:
        print("Request failed with status code:", response.status_code, response.text)
        return None


iface = gr.Interface(
    fn=generate_response,
    inputs=gr.inputs.Textbox(lines=2, placeholder="Enter your prompt here..."),
    outputs="text",
)

iface.launch()
