---
name: project-onboarding
description: Prepare a role-specific onboarding brief for a Flow Relay project by checking existing onboarding insights first and answering targeted follow-up questions with citations.
---

# Project onboarding

Explicit user instructions always take priority over these defaults.

## Input
- Role of the person joining (for example `backend engineer` or `product manager`) and optional focus area (repository, service or feature). If the role is missing, ask before generating.

## Workflow
1. Ensure the target project is active using `get_workspace_context` and `list_projects`.
2. Call `list_insights` first to check if a recent onboarding or architecture insight already covers the requested role and focus area.
3. If an existing insight fits, present it without triggering a new generation.
4. If no existing insight fits and the user wants a tailored brief, call `generate_onboarding_brief` with `new_member_role` and optional `focus_area`.
5. For specific follow-up questions about decisions, architecture or recent changes, call `ask_project` and include the returned source citations.
6. End with up to three concrete next things to read or inspect first based strictly on the retrieved brief and citations.

## Guardrails
- Do not call `generate_onboarding_brief` if `mcp:ai` is not granted; fall back to `list_insights`, `list_handoffs` and `list_events` or inform the user about the required scope.
- Never invent repositories, file paths, owners or architectural claims not present in tool outputs.
