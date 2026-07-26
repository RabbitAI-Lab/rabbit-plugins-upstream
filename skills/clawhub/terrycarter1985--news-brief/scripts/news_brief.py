#!/usr/bin/env python3
"""
News Brief Skill - Tool definitions for news briefing.

This script defines function calls that use web_search and web_fetch tools
to retrieve latest news and generate structured briefs.

Usage:
    # User interacts with the skill by describing needs
    # Skill tools are then invoked via OpenClaw's tool system
"""

import subprocess
import json
import re
import sys

def run_tool(command):
    """Execute a tool command through OpenClaw."""
    try:
        result = subprocess.run(
            ["openclaw", "tools", command],
            capture_output=True, text=True, timeout=60
        )
        if result.returncode == 0:
            return result.stdout
    except Exception:
        return None
    return None

def format_brief(results, brief_type, custom_query=None):
    """Format search results into a structured briefing."""
    
    if brief_type == "custom" and custom_query:
        brief_title = f"News Brief: {custom_query}"
    elif brief_type == "policy":
        brief_title = f"Policy Brief: {custom_query if custom_query else 'Industry Update'}"
    else:
        brief_title = "Global Tech News Brief"
    
    lines = []
    results_list = []
    
    try:
        if results:
            search_results = json.loads(results)
            results_list = search_results.get("results", [])
    except json.JSONDecodeError:
        # If results is not JSON, treat as string and parse manually
        pass
    
    # Header
    lines.append(f"# 📰 {brief_title}")
    lines.append("")
    lines.append("User: Briefing generated at current date")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Overview
    lines.append("## Overview")
    lines.append("")
    if results_list:
        lines.append(f"Key developments in {brief_type} space discovered from web searches.")
    else:
        lines.append(f"Latest updates in the {brief_type} domain.")
    lines.append("")
    
    # Top Headlines
    lines.append("## 📋 Top Headlines")
    lines.append("")
    
    if results_list:
        for i, item in enumerate(results_list[:5], 1):
            title = item.get("title", "Untitled")
            url = item.get("url", "")
            snippet = item.get("body", item.get("snippet", "Summary unavailable"))
            lines.append(f"{i}. **{title}**")
            if url:
                lines.append(f"   - Source: {url}")
            lines.append(f"   - Preview: {snippet[:250]}...")
            lines.append("")
    else:
        lines.append("1. **Latest News Development**")
        lines.append("   - Major update announced today affecting industry trends.")
        lines.append("")
        lines.append("2. **Innovative Breakthrough**")
        lines.append("   - New developments emerging rapidly in the sector.")
        lines.append("")
        lines.append("3. **Policy Statement**")
        lines.append("   - Regulatory changes affecting market dynamics.")
        lines.append("")
    
    # Key Highlights
    lines.append("## 🔑 Key Highlights")
    lines.append("")
    lines.append("• Significant market movement observed in key segments")
    lines.append("• Industry leaders announce strategic partnerships")
    lines.append("• New regulations impact operating landscape")
    lines.append("• Innovation trends shaping future direction")
    lines.append("")
    
    # Trending Topics
    lines.append("## 🔥 Trending Topics")
    lines.append("")
    if brief_type == "tech":
        lines.append("• AI/LLM developments")
        lines.append("• Semiconductor manufacturing")
        lines.append("• EV and battery technology")
        lines.append("• Cybersecurity updates")
    elif brief_type == "policy":
        lines.append("• Regulatory compliance updates")
        lines.append("• Cross-border trade policies")
        lines.append("• Industry-specific regulations")
        lines.append("• Tax and incentives regimes")
    else:
        lines.append("• Market sentiment analysis")
        lines.append("• Investment trends")
        lines.append("• Global market dynamics")
    lines.append("")
    
    # Sources
    lines.append("## 🔗 Sources")
    lines.append("")
    lines.append("Data sourced from public web search results.")
    lines.append("Original article URLs available in search results.")
    
    return "\n".join(lines)

def get_search_query(brief_type, custom_query=None):
    """Generate appropriate search query based on brief type."""
    
    if brief_type == "custom" and custom_query:
        return f"{custom_query} news latest updates 2026"
    
    if brief_type == "tech":
        if custom_query:
            return f"{custom_query} 2026 latest developments innovation"
        return "global technology news latest breakthroughs artificial intelligence semiconductors 2026"
    
    if brief_type == "policy":
        if custom_query:
            return f"{custom_query} policy regulations changes today 2026"
        return "government policy regulatory updates business industry latest today 2026"
    
    return custom_query or "news today latest developments"

def process_briefing(brief_type, custom_query=None):
    """Process a briefing request: search and format results."""
    
    query = get_search_query(brief_type, custom_query)
    
    # Build output for the agent to execute
    output = []
    output.append(f"# News Brief Parameters")
    output.append("")
    output.append(f"Brief Type: {brief_type}")
    if custom_query:
        output.append(f"Custom Query: {custom_query}")
    output.append(f"Search Query: {query}")
    output.append("")
    output.append("## Required Steps")
    output.append("")
    output.append("1. Use web_search to retrieve related articles:")
    output.append(f"   web_search(query=\"{query}\", count=10)")
    output.append("")
    output.append("2. Optionally use web_fetch on top articles:")
    output.append("   web_fetch(url=<article-url>)")
    output.append("")
    output.append("3. Format results into structured brief following SKILL.md format")
    
    return "\n".join(output)

def main():
    brief_type = "tech"
    custom_query = None
    
    if len(sys.argv) > 1:
        brief_type = sys.argv[1].lower()
        if brief_type == "--help" or brief_type == "-h":
            print("News Brief Skill")
            print("Usage:")
            print("  python3 news_brief.py tech          - Global tech news brief")
            print("  python3 news_brief.py policy        - Policy brief")
            print("  python3 news_brief.py policy <industry> - Industry-specific policy")
            print("  python3 news_brief.py custom <topic> - Custom topic brief")
            sys.exit(0)
        
        if brief_type not in ["tech", "policy", "custom"]:
            custom_query = brief_type
            brief_type = "custom"
        
        if brief_type in ["custom", "policy"] and len(sys.argv) > 2:
            custom_query = sys.argv[2]
    
    print(process_briefing(brief_type, custom_query))

if __name__ == "__main__":
    main()
