# Code Analysis Strategy Guide

How to decide what to include in a diagram and how to handle different project scales.

## What to Include

### Include functions that:

- Are **entry points** (CLI commands, API handlers, pipeline steps, hooks, UI init)
- Have **high fan-out** (call >= 2 project-internal functions)
- Have **high fan-in** (called from >= 3 sites)
- Contain **dispatch/routing logic** (switch/match, plugin registries, middleware chains)
- Perform **state mutation** or orchestrate multi-step workflows
- Implement **core domain logic** (the "why" of the project, not the "how")

### Exclude functions that:

- Are trivial getters/setters with no side effects
- Are thin wrappers around a single external call
- Are generic utilities (`format_*`, `ensure_*`, `clamp`, `retry`, `debounce`)
- Only perform logging, metrics, or telemetry
- Are auto-generated boilerplate (serializers, validators from schema)

**When in doubt, include** — more detail is better than missing logic. Excluded functions may still appear as collapsed `children` inside their caller's attr.

## Scoping by Project Size

### Small projects (< 20 files, < 2000 LOC)

- Include almost everything; one Overview + 1-2 call chains suffices
- Skip filtering thresholds; show the full picture

### Medium projects (20-100 files, 2k-20k LOC)

- Apply standard thresholds: fan-out >= 2, fan-in >= 3
- Generate Overview first, then offer 3-5 call chain options
- Group by module/package in Overview

### Large projects (100+ files, 20k+ LOC)

- Raise thresholds: fan-out >= 3, fan-in >= 4
- Collapse deeper calls into `children` rather than separate nodes
- Summarize repetitive patterns ("N similar handlers")
- Cross-module calls reference the target diagram name in `sig` hint
- Consider splitting into multiple Overview diagrams (by layer/domain)

## Architecture Detection

Identify the project's architecture type early to guide diagram structure:

| Architecture | Primary Diagram Style | Key Signals |
|---|---|---|
| **CLI tool** | Entry-point call chains per command | `argparse`, `click`, `clap`, `cobra` |
| **Web API** | Route handler → service → repo layers | Express, FastAPI, Gin, Spring routes |
| **UI application** | Widget hierarchy + event flow | Qt, React, Vue, SwiftUI imports |
| **Pipeline/ETL** | Stage-by-stage data flow | DAG definitions, step/stage functions |
| **Library/SDK** | Public API surface + internal impl | `__init__.py` exports, `mod.rs pub` |
| **Microservices** | Per-service entry + inter-service calls | Docker/K8s configs, gRPC/REST clients |

## Analysis Order

1. **Identify entry points** — `main()`, route handlers, CLI commands, signal handlers
2. **Trace hot paths** — Follow the most-called functions from entry points
3. **Map module boundaries** — Package/folder structure = natural grouping
4. **Find hub functions** — High fan-in/fan-out nodes are diagram anchors
5. **Detect patterns** — Factory, Observer, Strategy, Middleware → shape connections

## Tips for Accuracy

- **Read the actual source** — do not guess from file names alone
- **Follow imports** to understand module relationships before drawing connections
- **Check for dynamic dispatch** — metaclasses, decorators, DI containers may hide call relationships
- **Verify return types** — a function returning a callable may be an indirect caller
- **Watch for async** — `await`, channels, callbacks create non-obvious call chains
