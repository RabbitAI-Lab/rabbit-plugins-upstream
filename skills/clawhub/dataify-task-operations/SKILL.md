---
name: dataify-task-operations
description: Continue a Dataify Builder job after submission by checking status, explaining failures, retrieving available results, or reporting a safe handoff. Use when the user provides a Dataify task ID, asks whether a collection finished, or wants the result of an asynchronous Dataify scraper task.
---

# Dataify Task Operations

Complete the asynchronous task lifecycle instead of stopping at task creation.

## Contract

Treat task states as `submitted`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`. Preserve an unknown provider state verbatim and map it only when the meaning is unambiguous.

## Workflow

1. Require a task ID. Reuse one returned earlier in the conversation when unambiguous.
2. Read `DATAIFY_API_TOKEN` from the environment. Never accept or print it as a command-line argument.
3. Use an installed Dataify task-status/result tool when available. Do not invent an endpoint that is not documented in the repository or exposed by a connected tool.
4. If status is queued or running, report the current state and continue monitoring only when the user asked to wait or monitor.
5. If succeeded, return the available result or download link. Summarize by default and preserve access to raw data.
6. If failed, return the provider error, likely corrective action, and whether retrying is safe.
7. If no status/result capability is installed, report the task ID and dashboard URL as an explicit handoff. State that automated retrieval is unavailable; do not claim completion.

## Safety

- Do not retry paid or high-volume tasks without confirmation.
- Do not expose tokens, cookies, signed URLs, or private result contents in logs.
- Do not infer success from the presence of a task ID.

