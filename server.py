from fastmcp import FastMCP
import requests
import os
from dotenv import load_dotenv

load_dotenv()

mcp = FastMCP("SimpleAPI")

@mcp.tool
def fetch_news_headlines(topic: str) -> dict:
    """
    Fetch news articles related to a specific topic from the API.
    
    Args:
        topic (str): The topic to search for in news articles.
    
    Returns:
        dict: The JSON response from the API containing news articles.
    """
    try:
        url = f"https://amd1.mooo.com/api/duck/news?topic={topic}"
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {os.getenv('BEARER_TOKEN')}"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch news: {str(e)}")

@mcp.resource("info://api_version")
def get_api_version():
    """Return the version of the SimpleAPI server."""
    return "1.0.0"

@mcp.tool
def fetch_url(url: str) -> dict:
    """
    Fetch content from a given URL using the w3m API.
    
    Args:
        url (str): The URL to fetch content from.
    
    Returns:
        dict: The JSON response from the API containing the fetched content.
    """
    try:
        api_url = f"https://amd1.mooo.com/api/w3m?url={url}"
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {os.getenv('BEARER_TOKEN')}"
        }
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch URL: {str(e)}")

@mcp.tool
def fetch_google_search(query: str, num_results: int = 10, domain: str = "at") -> dict:
    """
    Fetch Google search results using the w3m API.
    
    Args:
        query (str): The search query. eg "Elon Musk"
        num_results (int): The number of search results to return. eg 10.
        domain (str): The domain to search in. eg at, de, com.
    
    Returns:
        dict: The JSON response from the API containing the search results.
    """
    try:
        api_url = f"https://amd1.mooo.com/api/w3m_google?query={query}&num_results={num_results}&domain={domain}"
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {os.getenv('BEARER_TOKEN')}"
        }
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch Google search results: {str(e)}")

if __name__ == "__main__":
    mcp.run()
