# QnA-ChatBot-LangChain

Acknowledgements
---
I would like to extend my sincere thanks to [Krish Naik](https://github.com/krishnaik06) for his invaluable content and guidance, which helped me build this project. This project wouldn't have been possible without his educational resources.

<br>

About the Project
---
[LangChain](https://www.langchain.com/) is a framework for building applications with large language models (LLMs), enabling features like memory, APIs, and tool integrations. Integrating [OpenAI](https://platform.openai.com/docs/overview) with LangChain allows developers to leverage powerful LLMs like [GPT-3.5-Turbo](https://platform.openai.com/docs/models#gpt-3-5-turbo) and [GPT-4](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4) for tasks such as dynamic prompting, conversational agents, and workflow automation.<br>
This project demonstrates the [Basic Functionalities of LangChain](https://github.com/SoubhikSinha/QnA-ChatBot-LangChain/blob/main/langchain.ipynb) and its integration with OpenAI models. It concludes with a simple Q-n-A chatbot deployed locally using Streamlit.

<br>

How to Run the Project ?
---
### **1. Clone the Repository**
Clone the repository to your local machine :
```bash
git clone https://github.com/SoubhikSinha/QnA-ChatBot-LangChain.git
```
<br>

### **2. Create a Virtual Environment**
Navigate to the repository's root directory and create a Conda virtual environment :
```bash
conda create --prefix ./venv python=3.11 -y
```
<br>

### **3. Activate the Conda Environment**
Activate the newly created environment :
```bash
conda activate venv/
```
<br>

### **4. Install Required Libraries**
Install all the necessary dependencies :
```bash
pip install -r requirements.txt
```
<br>


### **5. OpenAI API Secret Key Creation**
To access OpenAI models, follow these steps to create your own API secret key :
1.  Go to the webpage: [OpenAI API Keys](https://platform.openai.com/settings/organization/api-keys)
2.  Click on `Create new secret key`.
3.  Give the key a name.
4.  Copy the generated `Secret Key` and paste it in the `.env` file as well as in `langchain.ipynb` next to `OPENAI_API_KEY` (if you want to explore the basic functionalities of LangChain).

<br>

### **6. HuggingFace Access Token Creation**
To create a HuggingFace access token, follow these steps :
1.  Visit [HuggingFace](https://huggingface.co/).
2.  Click on your `profile picture` in the top right.
3.  Select `Access Tokens` from the dropdown menu.
4.  Click on `Create New Token`.
5.  Name your token and create it.
6.  Copy the value of the token and paste it in `langchain.ipynb` wherever `HUGGINGFACEHUB_API_TOKEN` is mentioned.

<br>

### **7. Running the Streamlit Application**
To start the Streamlit application, run the following command in your terminal:
```bash
streamlit run app.py`
```
Once you execute the above command in your CLI/Terminal, an IP address (`Local URL`) will be provided (in some cases, a window may automatically pop up with the Streamlit application running in a new tab). You can now access and use the application.
