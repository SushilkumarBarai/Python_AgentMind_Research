from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import (
    search_tool, 
    wiki_tool, 
    save_tool, 
    calculator_tool, 
    web_scraper_tool,
    data_analysis_tool,
    datetime_tool,
    file_reader_tool
)

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]
    key_findings: list[str]
    
llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that helps generate comprehensive research papers.
            
            Available tools:
            - search: Search the web for current information
            - wikipedia: Get encyclopedic knowledge
            - calculator: Perform mathematical calculations
            - web_scraper: Extract content from specific URLs
            - data_analysis: Analyze CSV/JSON data
            - datetime: Get current date/time information
            - file_reader: Read local text files
            - save_text_to_file: Save research output
            
            Instructions:
            1. Analyze the user's query carefully
            2. Select appropriate tools to gather information
            3. Synthesize findings into a coherent summary
            4. List all sources used
            5. Provide key findings as bullet points
            
            Wrap the output in this format and provide no other text:
            {format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

tools = [
    search_tool, 
    wiki_tool, 
    save_tool, 
    calculator_tool, 
    web_scraper_tool,
    data_analysis_tool,
    datetime_tool,
    file_reader_tool
]

agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)

agent_executor = AgentExecutor(
    agent=agent, 
    tools=tools, 
    verbose=True,
    max_iterations=10,
    handle_parsing_errors=True
)

def main():
    print("=" * 60)
    print("🔬 AI Research Assistant")
    print("=" * 60)
    print("\nAvailable capabilities:")
    print("  • Web search for current information")
    print("  • Wikipedia knowledge lookup")
    print("  • Mathematical calculations")
    print("  • Web page content extraction")
    print("  • Data analysis (CSV/JSON)")
    print("  • File reading and saving")
    print("  • Date/time information")
    print("\n" + "=" * 60)
    
    query = input("\n💡 What can I help you research? ")
    
    if not query.strip():
        print("❌ Please provide a valid query.")
        return
    
    print(f"\n🔍 Researching: {query}")
    print("⏳ Please wait...\n")
    
    try:
        raw_response = agent_executor.invoke({"query": query})
        
        # Try to parse structured response
        try:
            output_text = raw_response.get("output")
            structured_response = parser.parse(output_text)
            
            print("\n" + "=" * 60)
            print("📊 RESEARCH RESULTS")
            print("=" * 60)
            print(f"\n📌 Topic: {structured_response.topic}")
            print(f"\n📝 Summary:\n{structured_response.summary}")
            print(f"\n🔑 Key Findings:")
            for i, finding in enumerate(structured_response.key_findings, 1):
                print(f"  {i}. {finding}")
            print(f"\n🔗 Sources:")
            for i, source in enumerate(structured_response.sources, 1):
                print(f"  {i}. {source}")
            print(f"\n🛠️  Tools Used: {', '.join(structured_response.tools_used)}")
            print("=" * 60)
            
            # Ask if user wants to save
            save = input("\n💾 Save this research? (y/n): ")
            if save.lower() == 'y':
                save_data = f"""
TOPIC: {structured_response.topic}

SUMMARY:
{structured_response.summary}

KEY FINDINGS:
{chr(10).join(f"  • {finding}" for finding in structured_response.key_findings)}

SOURCES:
{chr(10).join(f"  • {source}" for source in structured_response.sources)}

TOOLS USED: {', '.join(structured_response.tools_used)}
"""
                save_tool.func(save_data)
                print("✅ Research saved successfully!")
            
        except Exception as e:
            print("\n⚠️  Could not parse structured response.")
            print(f"Error: {e}")
            print(f"\n📄 Raw Response:\n{raw_response.get('output')}")
            
    except Exception as e:
        print(f"\n❌ Error during research: {e}")

if __name__ == "__main__":
    main()
