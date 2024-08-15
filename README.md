# VideoQ

#### Quick Answers, Skip Clickbait
- Skip the endless scrolling. VideoQ provides instant video insights.
- Ask Questions to YouTube video and Save Time

VideoQ is an AI-powered web application that processes YouTube video content using Gradio and LangChain, enhanced by Cohere embeddings for language understanding. This app allows users to input Youtube video link and receive processed results based on advanced language models.

![Project Demo](demo_capture.gif)

### Features

- YouTube Video Processing: Automatically load and process video content. Currently support only English video whose transcripts are available.
- Cohere Embeddings: Use advanced embeddings to understand and process text data.
- Gradio Interface: An easy-to-use web interface for interaction.


### Installation
Follow these steps to set up and run the project on your local machine.

Prerequisites
Ensure you have the following installed:

1. Python 3.X
2. pip (Python package installer)
3. Clone the Repository
```bash
git clone https://github.com/yourusername/projectname.git
cd projectname
```

#### Install Dependencies
Install the required Python packages using the requirements.txt file:
```bash
pip install -r requirements.txt
```

Set Up Environment Variables
The application uses API keys that need to be set as environment variables. Ensure you have the necessary API keys (like the Cohere API key) and set them in your environment.

For Linux/macOS:
```bash
export COHERE_API_KEY=your_cohere_api_key
```

For Windows:
```bash
set COHERE_API_KEY=your_cohere_api_key
```

Running the Application
Once everything is set up, you can start the application by running:

```python
python app.py
```

This will launch the Gradio app, and you can access it via your web browser at http://localhost:7860.

### Usage
This tool is perfect for quickly getting insights from videos with clickbait titles or thumbnails—just ask your question instead of wasting time.

1. Input a YouTube Video URL: Enter the URL of the YouTube video you want to process.
2. Click "Load Document": Load the video content into the tool.
3. Start Chatting: Ask questions or discuss the video in the chat interface below.

The processed output will be displayed directly in the Gradio interface.



<!-- Contributing
If you'd like to contribute to this project, please fork the repository and use a feature branch. Pull requests are warmly welcome. -->

<!-- ### License
This project is licensed under the MIT License - see the LICENSE file for details. -->

### Acknowledgments
Special thanks ❤️ to the Gradio, LangChain, and Cohere teams for their amazing tools and support. This project wouldn't have been possible without their contributions to user-friendly interfaces, seamless language model integration, and powerful NLP capabilities.