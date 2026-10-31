---
name: agent-orchestrator
description: Run multiple agents in parallel and merge results with intelligent error handling and resource management.
version: 1.0.0
author: Z-Hussein
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [orchestration, parallel, delegate, multi-agent, workflow, automation]
    homepage: https://docs.openclaw.ai/
    related_skills: []
    inputs:
      goals:
        type: array
        items:
          type: string
        description: "List of goal descriptions (strings) – one per subagent to run in parallel"
        required: true
      max_parallel:
        type: integer
        description: "Maximum number of agents to run concurrently (default: system-dependent)"
        required: false
        default: 4
      timeout_seconds:
        type: integer
        description: "Timeout in seconds for each subagent (default: 300)"
        required: false
        default: 300
      retry_failed:
        type: boolean
        description: "Whether to automatically retry failed subagents (default: false)"
        required: false
        default: false
    outputs:
      report:
        type: object
        description: "Merged report containing execution results from all subagents"
        properties:
          successful:
            type: array
            items:
              type: object
              description: "Successfully completed subagents"
            description: "List of successful subagent executions"
          failed:
            type: array
            items:
              type: object
              description: "Failed subagents"
            description: "List of failed subagent executions"
          total_execution_time:
            type: number
            description: "Total wall-clock time for the orchestration"
          timestamp:
            type: string
            description: "ISO timestamp of when the orchestration completed"
    examples:
      - description: "Run three research tasks in parallel"
        invocation: |
          agent-orchestrator run --goals '["Research renewable energy trends", "Compare electric vehicle models", "Analyze climate impact reports"]'
      - description: "Orchestrate with custom parallelism and timeout"
        invocation: |
          agent-orchestrator run --goals '[\"Task 1\", \"Task 2\"]' --max-parallel 2 --timeout-seconds 60
      - description: "Retry failed subagents automatically"
        invocation: |
          agent-orchestrator run --goals '[\"Flaky task A\", \"Stable task B\"]' --retry-failed true
---

# Agent Orchestrator Skill

## When to use
Use when a task can be divided into independent sub‑jobs that benefit from concurrent execution by multiple agents (or agent instances).

Ideal scenarios:
- Research tasks requiring multiple perspectives or data sources
- Code generation or refactoring across multiple files/modules
- Data processing pipelines with parallelizable stages
- Testing scenarios requiring multiple test suites to run concurrently
- Any workload where sub‑tasks don't have strict sequential dependencies

## What it does
- Provides a robust wrapper around the agent’s delegation/spawning mechanism (e.g., `delegate_task`, `fork`, or `spawn`).
- Automatically collects stdout/stderr from each subagent and merges them into a single comprehensive report.
- Handles retries, timeouts, and graceful cancellation of stray subagents.
- Offers a shared scratch directory (configurable via `$ORCH_SCRATCH` or similar) for intermediate data.
- Emits a summary JSON file containing each subagent’s exit code, output size, and execution timing.
- Implements intelligent resource management to prevent system overload.
- Provides detailed failure diagnostics for troubleshooting.

## Typical workflow
1. Prepare a list of goal descriptions (strings) – one per subagent.
2. Invoke the orchestrator with those goals, specifying any desired options (parallelism, timeout, retry behavior).
3. Examine the merged report to see successes, failures, and performance metrics.
4. If needed, re‑run only the failed subagents using the retry functionality.
5. Use the shared scratch directory for intermediate data that needs to be exchanged between subagents.

## Configuration
- `$ORCH_SCRATCH`: Optional path to shared scratch directory for intermediate data
- Default scratch directory: system temp directory with agent-orchestrator prefix

## References
- Delegation patterns in agent frameworks: look for `delegate_task`, `spawn`, or `fork` in your agent’s documentation.
- Parallel computing patterns and best practices for distributed systems.
- Error handling and fault tolerance in concurrent systems.

## Triggers
This skill activates when the user mentions:
- "run agents in parallel"
- "orchestrate multiple agents"
- "run tasks concurrently"
- "parallel agent execution"
- "multi-agent workflow"
- "delegate and merge results"
- "run multiple goals at once"