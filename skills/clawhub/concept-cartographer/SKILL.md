---
name: concept-cartographer
description: "Auto-generate prerequisite maps for learning any topic — shows what to learn first, what depends on what, and the optimal learning path. Use when starting to learn something new and feeling lost about where to begin."
version: 1.0.0
author: Denis Voronin
license: MIT
tags: [education, learning, prerequisites, knowledge-graph, study-planning, concept-maps]
---

# Concept Cartographer

## Overview

Concept Cartographer builds prerequisite maps for any topic. When you want to learn something new — say, "quantum computing" or "macroeconomics" — it maps out what you need to know first, what builds on what, and creates an optimal learning sequence. It eliminates the "where do I start?" paralysis that stops most self-learners.

The tool constructs a directed acyclic graph (DAG) of concepts, identifies your current knowledge baseline, and generates a personalized learning path that respects prerequisite dependencies.

## When to Use

- You want to learn a complex topic but don't know the prerequisites
- You're overwhelmed by the breadth of a new field and need a sequence
- You want to identify gaps in your knowledge before tackling an advanced topic
- You're planning a self-study curriculum for a new skill or domain
- **Don't use for:** single-task tutorials ("how to set up nginx") — use when the topic has a learning curve with multiple prerequisites

## How It Works

1. **Concept Graph** — Define topics and their prerequisites as a DAG
2. **Topological Sort** — Compute valid learning orders that respect dependencies
3. **Knowledge Audit** — Mark which concepts you already know
4. **Path Finding** — Generate the shortest path from your current knowledge to the target
5. **Critical Path** — Identify the longest prerequisite chain (the bottleneck)
6. **Export** — Render the map as JSON, text tree, or Mermaid diagram for visualization

## Quick Start

```bash
# Map prerequisites for a topic using the built-in knowledge base
python scripts/cartographer.py map "machine learning"

# Generate a learning path from your current knowledge
python scripts/cartographer.py path "machine learning" --known "python,basic-math,statistics"

# Visualize the concept map as a Mermaid diagram
python scripts/cartographer.py visualize "machine learning" --format mermaid

# Audit your knowledge — find gaps before starting
python scripts/cartographer.py audit "quantum computing" --known "linear-algebra,python"

# List all topics in the knowledge base
python scripts/cartographer.py topics
```

## Built-in Knowledge Base

The tool ships with prerequisite maps for common domains:
- **Programming**: Python, JavaScript, SQL, Algorithms, Data Structures
- **Math**: Calculus, Linear Algebra, Statistics, Discrete Math
- **ML/AI**: Machine Learning, Deep Learning, NLP, Computer Vision
- **Science**: Physics, Chemistry, Biology, Quantum Computing
- **Business**: Economics, Accounting, Finance, Marketing
- **Web**: HTML, CSS, React, Node.js, Databases

You can also define custom concept graphs (see `references/custom-graphs.md`).

## Workflow: Planning a Learning Journey

### Step 1: Map the territory
```bash
python scripts/cartographer.py map "deep learning"
```
This shows the full prerequisite tree — everything you'd eventually need to know.

### Step 2: Audit your current knowledge
```bash
python scripts/cartographer.py audit "deep learning" --known "python,linear-algebra,basic-statistics"
```
This highlights what you already know (✓), what you're missing (✗), and what's partially covered (~).

### Step 3: Generate your personalized path
```bash
python scripts/cartographer.py path "deep learning" --known "python,linear-algebra" --output my_plan.json
```
This produces the optimal sequence, skipping what you know and focusing on gaps.

### Step 4: Visualize
```bash
python scripts/cartographer.py visualize "deep learning" --format mermaid --output diagram.md
```
Paste the Mermaid output into any Markdown viewer to see the concept map.

## Learning Path Output

```
🎯 Target: Deep Learning
📊 Current knowledge: 2 concepts (python, linear-algebra)
⏱️  Estimated new concepts to learn: 8
🛤️  Critical path length: 6 steps

LEARNING PATH:
  1. ☐ Calculus (prerequisites: ✓) — derivatives needed for gradient descent
  2. ☐ Probability (prerequisites: ✓) — foundational for ML
  3. ☐ Statistics (prerequisites: ✓ probability)
  4. ☐ Machine Learning Basics (prerequisites: ✓ python, ☐ statistics)
  5. ☐ Neural Networks (prerequisites: ☐ ML basics, ☐ linear algebra ✓)
  6. ☐ Deep Learning (prerequisites: ☐ neural networks)
     └── 🎯 TARGET REACHED
```

## Common Pitfalls

1. **Skipping prerequisites to save time.** The critical path exists for a reason. Skipping calculus to learn ML leads to confusion and slower progress overall.
2. **Trying to learn everything at once.** The path is sequential for a reason. Master each step before moving to the next.
3. **Overestimating your knowledge.** Be honest in the audit. "I watched a YouTube video about it" ≠ "I know it."
4. **Ignoring the critical path.** The longest dependency chain determines your minimum time to competence. Focus there first.
5. **Treating the map as gospel.** Prerequisites are guidelines, not laws. Some people learn best non-linearly — adjust as you go.

## Verification Checklist

- [ ] `cartographer.py map "machine learning"` prints the prerequisite tree
- [ ] `cartographer.py path "machine learning" --known "python"` generates a learning sequence
- [ ] `cartographer.py audit "quantum computing" --known "linear-algebra"` shows gaps
- [ ] `cartographer.py visualize "machine learning" --format mermaid` produces Mermaid syntax
- [ ] `cartographer.py topics` lists all topics in the knowledge base

## References

- `references/custom-graphs.md` — how to define your own concept maps
- `references/learning-theory.md` — the cognitive science of prerequisite sequencing
