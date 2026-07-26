"""
AI Agent tool registration and execution subsystem.

Provides:
  - tools_list:  Return all available tool declarations (OpenAI Function Calling format)
  - tools_call:  Execute AI-selected tool calls
  - screen_context: Screen state snapshot (text summary for AI decision-making)
  - goal_run:    Natural language goal → plan → execute

This enables AI agents (via OpenClaw or directly via MCP) to
"look at the screen, make decisions, and execute operations".
"""
