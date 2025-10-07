# 🔬 ResearchAgent Pro

### *Your AI Agent for Intelligent Research*

---

## 📖 Table of Contents
- [What is ResearchAgent Pro?](#what-is-researchagent-pro)
- [What Can It Do?](#what-can-it-do)
- [How Does It Work?](#how-does-it-work)
- [Prerequisites](#prerequisites)
- [Installation Guide](#installation-guide)
- [How to Use](#how-to-use)
- [Understanding the Tools](#understanding-the-tools)
- [Example Usage](#example-usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## 🤔 What is ResearchAgent Pro?

ResearchAgent Pro is an **AI-powered research assistant** that helps you gather, analyze, and organize information automatically. Think of it as your personal research helper that can:
- Search the internet
- Read Wikipedia
- Do calculations
- Extract content from websites
- Analyze data files
- Save your research findings

**Perfect for:** Students, researchers, writers, analysts, or anyone who needs to gather information quickly!

---

## ✨ What Can It Do?

### 8 Powerful Tools at Your Fingertips:

| Tool | What It Does | Example Use |
|------|--------------|-------------|
| 🔍 **Web Search** | Searches the internet for current information | "What are the latest AI trends?" |
| 📚 **Wikipedia** | Gets factual information from Wikipedia | "Tell me about photosynthesis" |
| 🧮 **Calculator** | Performs math calculations | "What is 15% of 850?" |
| 🌐 **Web Scraper** | Extracts text from specific websites | "Get info from example.com" |
| 📊 **Data Analysis** | Analyzes CSV/JSON files | "Analyze sales_data.csv" |
| 📅 **DateTime** | Gets current date and time | "What day is it today?" |
| 📄 **File Reader** | Reads local text files | "Read notes.txt" |
| 💾 **Save Tool** | Saves research to a file | Automatically used when saving |

---

## 🔄 How Does It Work?

```
You Ask a Question
        ↓
AI Agent Analyzes Your Question
        ↓
Agent Selects the Right Tool(s)
        ↓
Tools Gather Information
        ↓
AI Organizes Everything
        ↓
You Get a Structured Answer
        ↓
Optional: Save to File
```

**The Magic:** The AI agent automatically decides which tools to use based on your question!

---

## 📋 Prerequisites

Before you start, make sure you have:

### 1. **Python Installed**
- Version: Python 3.8 or higher
- Check if installed: Open terminal/command prompt and type:
  ```bash
  python --version
  ```
- If not installed: Download from [python.org](https://www.python.org/downloads/)

### 2. **Anthropic API Key**
- You need an API key from Anthropic (the company that makes Claude AI)
- Get it here: [console.anthropic.com](https://console.anthropic.com/)
- Free tier available for testing!

### 3. **Basic Terminal/Command Prompt Knowledge**
- Know how to open terminal (Mac/Linux) or command prompt (Windows)
- Know how to navigate folders using `cd` command

---

## 🚀 Installation Guide

### Step 1: Download the Project

**Option A: Using Git (Recommended)**
```bash
git clone https://github.com/yourusername/researchagent-pro.git
cd researchagent-pro
```

**Option B: Download ZIP**
1. Click the green "Code" button on GitHub
2. Click "Download ZIP"
3. Extract the ZIP file
4. Open terminal/command prompt in that folder

### Step 2: Create a Virtual Environment (Recommended)

**Why?** Keeps your project dependencies separate and organized.

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You'll see `(venv)` appear in your terminal - that means it's active!

### Step 3: Install Required Packages

```bash
pip install -r requirements.txt
```

This installs all the necessary libraries. It might take 2-3 minutes.

### Step 4: Set Up Your API Key

1. Create a file named `.env` in the project folder
2. Open it with any text editor (Notepad, VS Code, etc.)
3. Add this line:
   ```
   ANTHROPIC_API_KEY=your_actual_api_key_here
   ```
4. Replace `your_actual_api_key_here` with your real API key
5. Save the file

**Important:** Never share your `.env` file or commit it to GitHub!

---

## 🎮 How to Use

### Running the Program

1. Make sure your virtual environment is activated (you see `(venv)`)
2. Run:
   ```bash
   python main.py
   ```

3. You'll see a welcome screen:
   ```
   ============================================================
   🔬 AI Research Assistant
   ============================================================
   
   Available capabilities:
     • Web search for current information
     • Wikipedia knowledge lookup
     • Mathematical calculations
     • Web page content extraction
     • Data analysis (CSV/JSON)
     • File reading and saving
     • Date/time information
   
   ============================================================
   
   💡 What can I help you research?
   ```

4. Type your question and press Enter!

### Example Questions to Try:

**General Research:**
```
Tell me about renewable energy sources
```

**Math Problems:**
```
What is 25% of 1200 plus 350?
```

**Current Information:**
```
What are the latest developments in artificial intelligence?
```

**Data Analysis:**
```
Analyze the file data.csv
```

**Web Content:**
```
Extract information from https://example.com/article
```

**Date/Time:**
```
What is today's date?
```

---

## 🛠️ Understanding the Tools

### When Does the Agent Use Each Tool?

The AI agent is smart and picks tools automatically based on your question:

| Your Question Contains... | Agent Will Use... |
|---------------------------|-------------------|
| Numbers, percentages, "calculate" | 🧮 Calculator |
| "Current", "latest", "news", "today" | 🔍 Web Search |
| "What is", "who is", historical facts | 📚 Wikipedia |
| "analyze", "data", file name | 📊 Data Analysis |
| A URL (https://...) | 🌐 Web Scraper |
| "what day", "what time" | 📅 DateTime |
| "read file", specific filename | 📄 File Reader |

**The agent can use multiple tools** in one research session!

---

## 💡 Example Usage

### Example 1: Simple Research

**You Ask:**
```
Tell me about the solar system
```

**Agent Does:**
1. Uses Wikipedia tool to get information
2. Organizes it into a summary
3. Provides key findings and sources

**Output:**
```
📊 RESEARCH RESULTS
============================================================

📌 Topic: The Solar System

📝 Summary:
The Solar System consists of the Sun and all objects bound to it by gravity...

🔑 Key Findings:
  1. Contains 8 planets
  2. Formed 4.6 billion years ago
  3. Sun contains 99.86% of system's mass

🔗 Sources:
  1. Wikipedia: Solar System

🛠️ Tools Used: wikipedia

💾 Save this research? (y/n):
```

### Example 2: Complex Research with Multiple Tools

**You Ask:**
```
Research electric cars and calculate if I save money by buying one. 
Annual gas cost is $2400, electricity would be $800
```

**Agent Does:**
1. Uses Web Search to research electric cars
2. Uses Wikipedia for technical details
3. Uses Calculator to compute savings: $2400 - $800
4. Combines everything into a report

---

## 📁 Project Structure

```
researchagent-pro/
│
├── main.py                    # Main program (runs the agent)
├── tools.py                   # All 8 tools are defined here
├── requirements.txt           # List of required packages
├── .env                       # Your API key (you create this)
├── .gitignore                 # Tells Git what to ignore
├── README.md                  # This file!
│
└── research_output.txt        # Auto-created when you save research
```

### File Explanations:

**main.py** - The Brain
- Creates the AI agent
- Handles user input
- Displays results
- Manages saving

**tools.py** - The Toolbox
- Defines all 8 tools
- Each tool is a Python function
- Tools return information to the agent

**requirements.txt** - The Shopping List
- Lists all Python packages needed
- Used by `pip install -r requirements.txt`

**.env** - The Secret Keeper
- Stores your API key securely
- Never commit this to GitHub!

---

## ⚙️ Configuration

### Changing the AI Model

In `main.py`, find this line:
```python
llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")
```

You can change to:
- `claude-3-5-sonnet-20241022` - Balanced (default)
- `claude-3-opus-20240229` - Most powerful
- `claude-3-haiku-20240307` - Fastest and cheapest

### Adjusting Tool Settings

In `tools.py`, you can customize:

**Wikipedia Results:**
```python
api_wrapper = WikipediaAPIWrapper(
    top_k_results=2,        # Number of Wikipedia articles
    doc_content_chars_max=500  # Max characters to retrieve
)
```

**Save File Location:**
```python
def save_to_txt(data: str, filename: str = "my_custom_name.txt"):
    # Change the default filename
```

**Max Agent Iterations:**
In `main.py`:
```python
agent_executor = AgentExecutor(
    agent=agent, 
    tools=tools, 
    verbose=True,
    max_iterations=10,  # Change this number
)
```

---

## 🐛 Troubleshooting

### Problem: "ModuleNotFoundError"

**Solution:**
```bash
pip install -r requirements.txt
```
Make sure your virtual environment is activated!

### Problem: "API Key Not Found"

**Solution:**
1. Check if `.env` file exists in project folder
2. Make sure it contains: `ANTHROPIC_API_KEY=your_key`
3. No spaces around the `=` sign
4. API key should have no quotes

### Problem: "Rate Limit Error"

**Solution:**
- You've exceeded your API usage limit
- Wait a few minutes or check your Anthropic account
- Consider upgrading your plan

### Problem: "Tool Not Working"

**Solution:**
1. Check your internet connection (for search/wiki/scraper)
2. Make sure file exists (for file reader/data analysis)
3. Check file format (CSV/JSON for data analysis)

### Problem: Agent Takes Too Long

**Solution:**
- The agent is thinking and using tools
- Wait for completion (usually 10-30 seconds)
- If stuck, press `Ctrl+C` to cancel

### Problem: "Parsing Error"

**Don't worry!** The agent will show you the raw response instead. You can still read the information.

---

## 🙏 Acknowledgments

Built with:
- [LangChain](https://www.langchain.com/) - Agent framework
- [Anthropic Claude](https://www.anthropic.com/) - AI model
- [DuckDuckGo](https://duckduckgo.com/) - Web search
- [Wikipedia](https://www.wikipedia.org/) - Knowledge base

---

## 🚀 What's Next?

### Roadmap:

- [ ] Add more tools (email, image analysis, translation)
- [ ] Web interface (Flask/Streamlit)
- [ ] Multiple file format support
- [ ] Conversation history
- [ ] Export to PDF/Word
- [ ] Multi-language support
- [ ] Voice input/output

### Stay Updated:

- ⭐ Star this repository
- 👁️ Watch for updates
- 🔔 Follow for announcements

---

## 💬 Feedback

Love ResearchAgent Pro? Found it helpful? 

- ⭐ Give us a star on GitHub
- 🐦 Share on social media
- 📝 Write a blog post about it
- 🗣️ Tell your friends!

---

**Made with ❤️ by [Sushilkumar Barai]**

*Happy Researching! 🔬✨*
