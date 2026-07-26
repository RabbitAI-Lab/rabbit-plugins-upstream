"""
Natural language script generation for desktop-control.

Provides:
  - LLM-based script generation from natural language prompts
  - JSON Schema validation of generated scripts
  - Script template library (common tasks without LLM)
  - Integration with the async script execution engine

This module is a **pluggable** add-on. All LLM dependencies are lazy-loaded.
The module functions without LLM configuration (templates still work).
"""
