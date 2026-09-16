---
name: "Vercel Zero Explorer"
description: "AI-powered guide for Vercel Zero - the first programming language designed specifically for AI agents. Covers Zero syntax, .0 file extension, native tools, explicit effects, structured JSON diagnostics, and AI-native development workflows. Built for AI developers, language designers, and researchers exploring the future of AI-native programming."
version: "1.0.1"
keywords:
  - AI agent programming
  - Zero language
  - Vercel
  - AI-native development
  - programming language
  - agent tools
---

# Vercel Zero Explorer

## Overview

**Vercel Zero** is an experimental systems programming language launched by Vercel Labs on May 16, 2026. It is specifically designed for AI coding agents, not humans. Unlike traditional programming languages that prioritize human readability, Zero embraces AI-native paradigms with structured JSON diagnostics, explicit effects, and predictable memory management.

This Skill provides comprehensive guidance on understanding, using, and building with Zero language.

## Current Status (as of 2026-09-14)

| Item | Status |
|------|--------|
| Latest release | **v0.3.4** (the 0.1.x line is obsolete) |
| License | Apache-2.0 |
| GitHub | ~5,200 stars, developed by Vercel Labs |
| Targets | Native binaries for Linux, macOS, Windows |
| Authoring model | **Graph-first**: `zero.graph` is the compiler input; `.0` files are human-readable projections |
| Maturity | Experimental — breaking changes expected, not for production or sensitive data |

**Recent developments:**
- **v0.3.0 made graph-first authoring the default workflow.** The binary `zero.graph` store is now what the compiler reads; `.0` text files became projections for human review. Agents edit through `zero query` / `zero patch` instead of rewriting source text, and patches carry an expected graph hash so stale or invalid edits are rejected *before* the store is written.
- **Version churn is real.** v0.1.4 introduced row syntax, v0.2.0 promoted canonical `.0` text to the native source surface, and v0.3.0 rejects source-projection input at the compiler boundary. Existing text-first packages must run `zero import` to pull source into the graph; v0.3.2 reportedly made `zero import` roughly 12x faster on large programs.
- **The toolchain contract is the distinctive part.** Every subcommand of the single `zero` binary shares one `--json` flag and one diagnostic schema, so errors arrive with stable codes (e.g. `NAM003`) and typed repair metadata (e.g. `declare-missing-symbol`); `zero fix --plan --json` returns a repair plan an agent can accept, edit, or reject rather than a blind patch.
- These items are compiled from public coverage; exact version numbers, flags and behaviour change frequently — **treat the official repository and docs as authoritative**.

> **Safety note:** Vercel Labs explicitly warns to expect breaking changes, rough edges and security issues, and to avoid production systems and sensitive data. Evaluate Zero in an isolated, disposable workspace.
## Triggers

**Chinese:**
- "Vercel Zero是什么"
- "Zero编程语言"
- "AI Agent专用语言"
- "Vercel Zero教程"
- "Zero语言入门"

**English:**
- "What is Vercel Zero"
- "Zero programming language guide"
- "AI agent programming language"
- "Vercel Zero tutorial"
- "Zero .0 file extension"

## Features

### 1. Core Concepts of Zero Language

| Concept | Description | Mechanism | Why it matters for an agent |
|---------|-------------|-----------|------------------------------|
| **Native Tools** | Zero provides built-in system tools optimized for AI agents | Built into the language rather than pulled from external package registries | No dependency resolution step, so an agent's first build rarely fails on missing packages |
| **Explicit Effects** | Side effects are explicitly declared, making AI behavior predictable | A function that touches the outside world must accept a `World` capability; the compiler enforces it | A signature alone tells the agent whether code can reach network, filesystem or stdout |
| **Predictable Memory** | Memory management follows deterministic patterns | Deterministic allocation instead of tracing garbage collection | Execution cost is easier to predict before running, useful when an agent is choosing between candidate programs |
| **Structured JSON Diagnostics** | Compiler outputs structured JSON for easy AI parsing | One shared `--json` flag and one diagnostic schema across every subcommand | The agent branches on stable codes instead of parsing changing prose |
| **.0 File Extension** | Uses `.0` extension (e.g., `main.0`) | Under v0.3.x the `.0` text is a *projection* exported from the graph, not the compiler input | Humans can still review and deliberately edit readable text, then import it back |

### 2. Zero Syntax Basics

```zero
// Example Zero code structure
import { http, file } from "std";

// Define a tool with explicit effects
tool fetch_data(url: string) -> json {
  effect network_call(url)
  return http.get(url)
}

// AI-friendly structured output
diagnose parse_result as json
```

**Example — the `World` capability makes effects visible in the signature:**

```zero
import { file, std } from "std";

// No World parameter => the compiler guarantees this cannot touch disk or network
tool pure_total(prices: list<f64>) -> f64 {
  return prices.fold(0.0, |acc, p| acc + p)
}

// World is required => the signature itself advertises a filesystem effect
tool save_report(w: World, path: string, body: string) -> result<unit, io_error> {
  effect file_write(path)
  return file.write(w, path, body)
}
```

The practical payoff: an agent reviewing a candidate function does not need to read its body to know whether it can reach the outside world — `save_report` obviously can, `pure_total` provably cannot.

**Example — a diagnostic an agent can act on (v0.3.x schema):**

```json
{
  "code": "NAM003",
  "severity": "error",
  "message": "unknown identifier `prices_total`",
  "repair": { "kind": "declare-missing-symbol", "symbol": "prices_total" },
  "span": { "node": "653eeb6e", "field": "value" }
}
```

Note the `span` points at a **stable node id and field**, not a line/column pair. That is the whole point of graph-first authoring: the reference does not drift when someone inserts a comment above it.
### 3. AI Agent Integration Patterns

- **Tool Definition**: Define reusable tools with explicit interfaces
- **Effect Declaration**: Declare side effects before execution
- **Structured Diagnostics**: Parse compiler output as JSON for AI decision-making
- **Error Recovery**: Use structured errors for autonomous debugging

**Integration example — autonomous fix loop with Claude Code:**

```bash
# 1. read the graph instead of guessing at source text
zero query --json '{"kind":"function","name":"fetch_api_data"}'

# 2. propose a semantic patch guarded by a hash
zero patch --json '{"op":"set","node":"653eeb6e","field":"value","expect_hash":"ab91...","to":"..."}'

# 3. ask the compiler for a plan instead of applying a blind fix
zero fix --plan --json

# 4. keep human review in the loop
zero export --out review/ && zero verify-projection
```

**Integration example — CI drift gate:** run `zero verify-projection` in CI so a hand-edited `.0` file that no longer matches the graph fails the build rather than silently diverging.
## Command Cheat Sheet

| Command | Purpose | Typical agent use |
|---------|---------|-------------------|
| `zero init` | Initialise a package / graph store | Start of a task |
| `zero query --json` | Read declarations, types, calls, effects, node ids | Replace "read the file" |
| `zero patch --json` | Apply a semantic edit guarded by a graph hash | Replace "rewrite lines 40-52" |
| `zero import` | Pull existing `.0` source into the graph | Migrating text-first packages |
| `zero export` | Emit a human-readable `.0` projection | Human review, pull requests |
| `zero verify-projection` | Check the projection still matches the graph | CI drift gate |
| `zero check` / `zero test` / `zero run` | Type-check, test, execute | Standard loop |
| `zero fix --plan --json` | Machine-readable repair plan | Agent decides accept / edit / reject |
| `zero build` | Emit executable, object, or LLVM IR | Packaging |

Every one of these accepts `--json`, so a single parser handles all of them.

## Workflow

### Step 1: Understand Zero's Design Philosophy
- Zero prioritizes AI parsing over human readability
- Structured output enables reliable AI agent workflows
- Native tools are designed for autonomous execution
- *Example:* where a Python agent must first resolve `requests` from an index and hope the version is compatible, a Zero agent calls a built-in `http` tool that ships with the language — one less failure mode per iteration.
### Step 2: Explore Zero Syntax
- Learn the `.0` file extension convention
- Understand explicit effect declarations
- Master structured JSON diagnostics format
- *Example:* map the codes you actually hit into a lookup table (`NAM003` → declare missing symbol, timeout codes → retry with backoff) so recovery is a table lookup instead of a fresh reasoning step each time.
### Step 3: Build AI-Native Tools
- Create custom tools with predictable behavior
- Define clear input/output interfaces
- Use explicit error handling patterns
- *Example:* return `result<json, io_error>` rather than throwing, so the caller — which is usually the agent — is forced to handle the failure branch at compile time.
### Step 4: Integrate with AI Agents
- Connect Zero programs to Claude Code, Codex, or other AI coding agents
- Use structured diagnostics for autonomous debugging
- Implement guardrails for safe AI execution
- *Example:* grant the `World` capability only to a thin top-level entry point and pass pure functions everything else; then the blast radius of an agent-generated change is legible from the call graph.
## Input/Output Examples

### Example 1: Understanding Zero Concepts

**Input:**
```
Explain the key differences between traditional programming languages and Zero language.
```

**Output:**
```
Key Differences Between Traditional Languages and Zero:

| Aspect | Traditional Languages | Zero Language |
|--------|---------------------|---------------|
| Target Users | Humans | AI Agents |
| Output Format | Human-readable errors | Structured JSON diagnostics |
| Effects | Implicit side effects | Explicit effect declarations |
| Memory | Garbage collection | Predictable memory patterns |
| Tool Interface | External libraries | Native built-in tools |
| Extension | .py, .js, .go | .0 |

Zero is not meant for humans to write directly - it's designed to be generated and understood by AI agents.
```

### Example 2: Creating a Zero Tool

**Input:**
```
Create a Zero tool that fetches data from an API and returns structured JSON.
```

**Output:**
```zero
// data_fetch_tool.0

import { http, json } from "std";

// Tool definition with explicit effects
tool fetch_api_data(
  endpoint: string,
  method: string = "GET"
) -> json {
  // Explicit network effect declaration
  effect network_call(endpoint, method)
  
  // Execute HTTP request
  response = http.request(endpoint, {
    method: method
  })
  
  // Return structured JSON
  return json.parse(response.body)
}

// Structured diagnostics for debugging
diagnose fetch_api_data as {
  success: boolean,
  data: json | null,
  error: string | null
}
```

### Example 3: AI Agent Workflow Integration

**Input:**
```
How can I integrate Zero programs with Claude Code for autonomous debugging?
```

**Output:**
```
Integration Guide for Claude Code + Zero:

1. Generate Zero code using Claude Code
2. Execute and capture JSON diagnostics
3. Parse structured errors for autonomous recovery
4. Implement fix strategies based on diagnostic codes

Example Workflow:
```json
{
  "step": "execute",
  "tool": "fetch_api_data",
  "diagnostic": {
    "code": "NETWORK_TIMEOUT",
    "suggestion": "retry_with_backoff",
    "affected_lines": [5, 6]
  }
}
```

Claude Code can automatically:
- Parse diagnostic codes
- Select recovery strategy
- Re-execute with modifications
- Verify fix success
```

## Use Cases

| Use Case | Description | Best suited for | Honest caveat |
|----------|-------------|-----------------|---------------|
| **AI Code Generation** | Generate Zero code that AI agents can reliably execute | Agent builders measuring whether hash-guarded patches reduce silent breakage | Training-data advantage still sits with Python/JS/Go |
| **Autonomous Debugging** | Use structured diagnostics for self-healing code | Loops that need to branch on error codes rather than prose | Garbage in still produces garbage out; tests still decide correctness |
| **Tool Development** | Build native tools optimized for AI workflows | Small disposable CLI utilities where a ~16 KiB binary is a feature | Ecosystem is young; expect to write your own bindings |
| **Language Research** | Explore AI-native programming paradigms | Researchers comparing capability-based effects and graph IRs | Benchmarks are design targets, not published results — measure yourself |

## References

- [Vercel Zero GitHub Repository](https://github.com/vercel-labs/zero)
- [Zero Official Documentation](https://vercel.com/docs/zero)
- [AI Agent Programming Language Analysis](https://blog.csdn.net/irpywp/article/details/161167783)
- [InfoQ: Vercel Labs Ships Zero, a Graph-First Language Built So Agents Write the Code](https://www.infoq.com/news/2026/08/vercel-ships-zero-ai)
- [Zero getting-started guide](https://github.com/vercel-labs/zero) — authoritative for current commands and flags

## Notes

- Zero is experimental (**v0.3.4** as of 2026-09-14; the 0.1.x line is obsolete)
- Not intended for production human-written code
- Focus is on AI agent reliability and predictability
- File extension `.0` is unique to Zero language
- Under v0.3.x the compiler reads `zero.graph`, not `.0`; treat `.0` as a projection
- Reported figures (16.2 KiB hello world, ~1 ms build, token efficiency, tiny artifacts) are **design targets** — benchmark your own program before relying on them
- Positioning: closer to Zig than Rust on binary size and explicit allocation; lacks Rust's borrow-checker maturity and ecosystem, and trades Go's green threads and larger runtime for dependency-free artifacts
- **Evaluate in an isolated workspace**; do not point Zero at production systems or sensitive data
---

**Author:** Ge Cheng | **Skill Address:** clawhub.ai/skills/vercel-zero-explorer | **Skill Version:** 1.0.1 | **Last reviewed:** 2026-09-14
