import gradio as gr
from langchain_community.document_loaders import YoutubeLoader


from langchain_cohere import ChatCohere
import bs4
from langchain import hub
from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_cohere import CohereEmbeddings

llm = ChatCohere(model="command-r")
prompt = hub.pull("rlm/rag-prompt")

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


# Function to load YouTube details
def get_youtube_details(video_url):
    print(video_url)
    loader = YoutubeLoader.from_youtube_url(str(video_url), add_video_info=False)
    docs = loader.load()
    print("Video transcripts loaded in DB")
    return docs, loader

# Function to handle user messages and update the history
def user_message(message, history):
    return "", history + [[message, None]]

# Function to clear the vector store (optional, not used in this example)
def clear_vectorstore(vectorstore):
    vectorstore.delete_all()
    return "Vector store cleared."

# Function to clear the text box and reset the state
def clear_textbox():
    return "", None, None

# Function to handle bot responses
def bot_message(history, docs):
    if docs is None:
        return history
    
    user_question = history[-1][0]
    splits = text_splitter.split_documents(docs)
    vectorstore = Chroma.from_documents(documents=splits, embedding=CohereEmbeddings())
    retriever = vectorstore.as_retriever()

    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    response = rag_chain.invoke(user_question)
    history[-1][1] = response
    return history

title=(
"""
<center> 

<h1> VideoQ: Quick Answers, Skip Clickbait </h1>
<b> text  📧<b>

</center>
"""
)

with gr.Blocks(theme=gr.themes.Monochrome()) as demo:
    # gr.Markdown("#              VideoQ: Quick Answers, Skip Clickbait")
    with gr.Row():
          gr.HTML(title,label=" ")  

    gr.Markdown("""
    ### Skip the endless scrolling. VideoQ provides instant video insights.
    ### Ask Questions to YouTube video and Save Time 
    """,label="Description")

    text_box = gr.Textbox(lines=2, placeholder="Enter link of the YouTube video",label="Youtube valid link")
    with gr.Row():
        load_button = gr.Button("Load Document")
        clear_button = gr.Button("Clear Document")

    docs_box = gr.State()
    loader_box = gr.State()

    load_button.click(fn=get_youtube_details, inputs=[text_box], outputs=[docs_box, loader_box])
    clear_button.click(fn=clear_textbox, inputs=[], outputs=[text_box, docs_box, loader_box])

    chatbot_interface = gr.Chatbot(show_copy_button=True,label=" ")
    msg = gr.Textbox(label="Message")

    with gr.Row():
        submit_btn = gr.Button("Submit")
        clear_btn = gr.Button("Clear")

    submit_btn.click(user_message, [msg, chatbot_interface], [msg, chatbot_interface], queue=False).then(
        bot_message, [chatbot_interface, docs_box], chatbot_interface)
    
    msg.submit(user_message, [msg, chatbot_interface], [msg, chatbot_interface], queue=False).then(
        bot_message, [chatbot_interface, docs_box], chatbot_interface)

    clear_btn.click(lambda: None, None, chatbot_interface, queue=False)

demo.launch()
