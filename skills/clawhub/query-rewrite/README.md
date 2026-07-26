# Query Rewrite — RAG Retrieval Pre-processing Layer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-SKILL-blue)](https://openclaw.ai)

> Intelligent query rewriting layer for RAG-based AI agents. Improves retrieval recall in multi-turn conversations.

## ✨ Features

- **6 Rewrite Modes**: Context extraction, comparison disambiguation, coreference resolution, multi-intent decomposition, rhetorical question detection, condition extraction
- **Fast Detection**: Determines whether rewrite is needed in under 0.5s
- **Dual-path Search**: Searches with both original and rewritten queries
- **Zero-rewrite Principle**: No unnecessary rewriting — if the query is clear, search directly
- **Graceful Fallback**: Falls back to original query when reference resolution is uncertain

## 📦 Installation

### Via ClawHub

```bash
clawhub install query-rewrite
```

### Via OpenClaw CLI

```bash
openclaw skills install query-rewrite
```

### Manual

```bash
git clone https://github.com/DaBin0927/query-rewrite.git ~/.openclaw/skills/query-rewrite
```

## 🚀 Quick Start

The SKILL activates automatically before any RAG retrieval call (`memory_search`, `wiki_search`, vector search).

### Basic Usage

1. Your agent is in a multi-turn conversation
2. Before any search, the SKILL checks if the current query needs rewriting
3. If yes, it extracts context, resolves references, or decomposes multi-intent queries
4. Searches with both original and rewritten queries, then merges results

### Example

```
Conversation turn 1: User asks about "iPhone 15 Pro colors"
Conversation turn 2: User asks "How long is warranty?"

→ query-rewrite detects incomplete semantics
→ Rewrites: "iPhone 15 Pro warranty period"
→ Searches both queries, returns merged results
```

## 📋 Rewrite Modes

| Mode | Description | Example |
|------|-------------|---------|
| Context Extraction | Adds missing entities from conversation history | "Warranty?" → "iPhone 15 Pro warranty" |
| Comparison Disambiguation | Expands comparison queries | "Which is faster?" → "A vs B performance" |
| Coreference Resolution | Replaces pronouns with actual entities | "Do they all support it?" → multiple independent queries |
| Multi-intent Decomposition | Splits multi-question queries | "Color? Size? Price?" → 3 independent queries |
| Rhetorical Question Detection | Converts rhetorical questions to information queries | "It won't take a month, right?" → "Expected delivery time" |
| Condition Extraction | Extracts and structures filter conditions | "Under $500 for women" → "gift budget 500 women" |

## 🏆 Why Query Rewrite?

- **No competitors on ClawHub** — The only RAG pre-processing rewrite layer available
- **57% of community SKILLs are pure prompt** — This SKILL has structured decision logic
- **Battle-tested** — Used internally in production agent workflows

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a PR with a clear description

## 📄 License

MIT © 2026 DaBin0927
