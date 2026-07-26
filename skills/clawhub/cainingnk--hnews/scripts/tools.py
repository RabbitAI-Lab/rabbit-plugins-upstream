from __future__ import annotations

from typing import Optional

from scripts.call_api import call_api
from scripts.config import settings

def get_stories(
    story_type: Optional[str] = None,
    num_stories: Optional[int] = None
) -> Dict[str, Any]:
    """
    Get stories from Hacker News. The options are `top`, `new`, `ask_hn`, `show_hn` for types of stories. This doesn't include the comments. Use `get_story_info` to get the comments.
    
    Args:
        story_type: Type of stories to get, one of: `top`, `new`, `ask_hn`, `show_hn`
        num_stories: Number of stories to get
    
    Returns:
        
    """
    arguments = {
        "story_type": story_type,
        "num_stories": num_stories
    }
    
    return call_api("1777419073035267", "get_stories", arguments)

def get_user_info(
    user_name: str,
    num_stories: Optional[int] = None
) -> Dict[str, Any]:
    """
    Get user info from Hacker News, including the stories they've submitted
    
    Args:
        user_name: Username of the user
        num_stories: Number of stories to get, defaults to 10
    
    Returns:
        
    """
    arguments = {
        "user_name": user_name,
        "num_stories": num_stories
    }
    
    return call_api("1777419073035267", "get_user_info", arguments)

def search_stories(
    query: str,
    search_by_date: Optional[bool] = None,
    num_results: Optional[int] = None
) -> Dict[str, Any]:
    """
    Search stories from Hacker News. It is generally recommended to use simpler queries to get a broader set of results (less than 5 words). Very targetted queries may not return any results.
    
    Args:
        query: Search query
        search_by_date: Search by date, defaults to False. If this is False, then we search by relevance, then points, then number of comments.
        num_results: Number of results to get, defaults to 10
    
    Returns:
        
    """
    arguments = {
        "query": query,
        "search_by_date": search_by_date,
        "num_results": num_results
    }
    
    return call_api("1777419073035267", "search_stories", arguments)

def get_story_info(
    story_id: Optional[int] = None
) -> Dict[str, Any]:
    """
    Get detailed story info from Hacker News, including the comments
    
    Args:
        story_id: Story ID
    
    Returns:
        
    """
    arguments = {
        "story_id": story_id
    }
    
    return call_api("1777419073035267", "get_story_info", arguments)

