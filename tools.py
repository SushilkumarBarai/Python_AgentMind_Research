from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import json
import os

# ============================================================================
# 1. SAVE TOOL - Save research to files
# ============================================================================
def save_to_txt(data: str, filename: str = "research_output.txt"):
    """
    Saves research data to a text file with timestamp.
    
    Args:
        data: The content to save
        filename: Output filename (default: research_output.txt)
    
    Returns:
        Success message with filename
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"\n{'='*60}\n📅 Research Output\n⏰ Timestamp: {timestamp}\n{'='*60}\n\n{data}\n\n"
    
    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(formatted_text)
        return f"✅ Data successfully saved to {filename}"
    except Exception as e:
        return f"❌ Error saving file: {str(e)}"

save_tool = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description="Saves structured research data to a text file with timestamp. Use this to preserve research findings.",
)

# ============================================================================
# 2. SEARCH TOOL - Web search using DuckDuckGo
# ============================================================================
search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="search",
    func=search.run,
    description="Search the web for current information, news, and real-time data. Use this for recent events, current statistics, or when you need up-to-date information.",
)

# ============================================================================
# 3. WIKIPEDIA TOOL - Encyclopedia lookup
# ============================================================================
api_wrapper = WikipediaAPIWrapper(top_k_results=2, doc_content_chars_max=500)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)
wiki_tool.description = "Search Wikipedia for encyclopedic knowledge, historical information, scientific concepts, and factual data. Use this for well-established facts and definitions."

# ============================================================================
# 4. CALCULATOR TOOL - Mathematical computations
# ============================================================================
def calculator(expression: str) -> str:
    """
    Evaluates mathematical expressions safely.
    
    Args:
        expression: Mathematical expression to evaluate (e.g., "2 + 2", "15% of 100")
    
    Returns:
        Result of the calculation or error message
    """
    try:
        # Handle percentage calculations
        if "%" in expression:
            # Convert "15% of 100" to "0.15 * 100"
            if "of" in expression.lower():
                parts = expression.lower().replace("%", "").split("of")
                percentage = float(parts[0].strip()) / 100
                number = float(parts[1].strip())
                result = percentage * number
                return f"Result: {result}"
        
        # Remove common words
        expression = expression.lower().replace("what is", "").replace("calculate", "").strip()
        
        # Safe evaluation using eval with restricted globals
        allowed_names = {"__builtins__": None}
        allowed_functions = {
            "abs": abs, "round": round, "min": min, "max": max,
            "sum": sum, "pow": pow, "len": len
        }
        
        result = eval(expression, allowed_names, allowed_functions)
        return f"Result: {result}"
    
    except Exception as e:
        return f"❌ Calculation error: {str(e)}. Please provide a valid mathematical expression."

calculator_tool = Tool(
    name="calculator",
    func=calculator,
    description="Performs mathematical calculations including basic arithmetic, percentages, and expressions. Examples: '2+2', '15% of 850', 'pow(2,8)'",
)

# ============================================================================
# 5. WEB SCRAPER TOOL - Extract content from URLs
# ============================================================================
def scrape_webpage(url: str) -> str:
    """
    Scrapes and extracts text content from a webpage.
    
    Args:
        url: The URL to scrape
    
    Returns:
        Extracted text content or error message
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style", "nav", "footer", "header"]):
            script.decompose()
        
        # Get text
        text = soup.get_text(separator='\n', strip=True)
        
        # Clean up text
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        text = '\n'.join(lines)
        
        # Limit length
        if len(text) > 2000:
            text = text[:2000] + "...(truncated)"
        
        return f"📄 Content from {url}:\n\n{text}"
    
    except Exception as e:
        return f"❌ Error scraping webpage: {str(e)}"

web_scraper_tool = Tool(
    name="web_scraper",
    func=scrape_webpage,
    description="Extracts text content from a specific webpage URL. Use this when you have a specific URL to analyze or when you need content from a particular website.",
)

# ============================================================================
# 6. DATA ANALYSIS TOOL - Analyze CSV/JSON data
# ============================================================================
def analyze_data(file_path: str) -> str:
    """
    Analyzes CSV or JSON data files and provides summary statistics.
    
    Args:
        file_path: Path to the data file (CSV or JSON)
    
    Returns:
        Analysis summary or error message
    """
    try:
        import pandas as pd
        
        if not os.path.exists(file_path):
            return f"❌ File not found: {file_path}"
        
        # Load data
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith('.json'):
            df = pd.read_json(file_path)
        else:
            return "❌ Unsupported file format. Use CSV or JSON."
        
        # Generate summary
        summary = f"""
📊 Data Analysis Summary for {os.path.basename(file_path)}

📏 Dimensions: {df.shape[0]} rows × {df.shape[1]} columns

📋 Columns: {', '.join(df.columns.tolist())}

🔢 Numeric Summary:
{df.describe().to_string()}

❓ Missing Values:
{df.isnull().sum().to_string()}

📌 First 3 Rows:
{df.head(3).to_string()}
"""
        return summary
    
    except ImportError:
        return "❌ pandas library not installed. Run: pip install pandas"
    except Exception as e:
        return f"❌ Error analyzing data: {str(e)}"

data_analysis_tool = Tool(
    name="data_analysis",
    func=analyze_data,
    description="Analyzes CSV or JSON data files and provides statistics, missing values, and data preview. Provide the file path to analyze.",
)

# ============================================================================
# 7. DATETIME TOOL - Current date and time information
# ============================================================================
def get_datetime_info(query: str = "") -> str:
    """
    Provides current date, time, and related information.
    
    Args:
        query: Optional query like 'date', 'time', 'datetime', 'day', 'year'
    
    Returns:
        Formatted datetime information
    """
    now = datetime.now()
    
    info = f"""
📅 Current Date & Time Information:

📆 Date: {now.strftime('%Y-%m-%d')} ({now.strftime('%A, %B %d, %Y')})
⏰ Time: {now.strftime('%H:%M:%S')} ({now.strftime('%I:%M:%S %p')})
🌍 Day of Week: {now.strftime('%A')}
📊 Week Number: {now.strftime('%U')}
📈 Day of Year: {now.strftime('%j')}
"""
    return info

datetime_tool = Tool(
    name="datetime",
    func=get_datetime_info,
    description="Gets current date, time, day of week, and related temporal information. Use this when you need to know what day it is or current time.",
)

# ============================================================================
# 8. FILE READER TOOL - Read local text files
# ============================================================================
def read_file(file_path: str) -> str:
    """
    Reads and returns the content of a text file.
    
    Args:
        file_path: Path to the text file
    
    Returns:
        File content or error message
    """
    try:
        if not os.path.exists(file_path):
            return f"❌ File not found: {file_path}"
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Limit length
        if len(content) > 2000:
            content = content[:2000] + "\n...(truncated)"
        
        return f"📄 Content of {os.path.basename(file_path)}:\n\n{content}"
    
    except Exception as e:
        return f"❌ Error reading file: {str(e)}"

file_reader_tool = Tool(
    name="file_reader",
    func=read_file,
    description="Reads and returns the content of local text files. Provide the file path to read. Useful for analyzing existing documents or notes.",
)
