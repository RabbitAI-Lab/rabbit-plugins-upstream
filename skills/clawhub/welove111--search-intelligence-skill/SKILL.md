# Search Intelligence Skill

## Overview

Advanced AI-powered search skill using SearXNG as the universal search backend. Provides multi-engine dork generation, 90+ search engines, and intelligent search strategies for OpenClaw agents.

**⚠️ Privacy notice** — queries sent through this skill are relayed to the configured SearXNG instance and may be further forwarded to downstream third-party search engines. Do not send sensitive, confidential, or personally identifiable data (internal targets, investigative terms, credentials) through this skill without informed consent from the end user.

**⚠️ Responsible \& authorized use only** — intended strictly for authorized security research, OSINT on public data, and systems you own or have explicit written permission to assess. It must NOT be used for unauthorized reconnaissance, intrusive collection, surveillance, or anything that violates applicable laws, platform terms, or a target's reasonable expectation of privacy. The operator is solely responsible for authorization and legal compliance.

---

## Core Capabilities

### 1. Multi-Engine Search Orchestration
- Routes queries across 90+ search engines simultaneously
- Selects optimal engines per query type (academic, news, code, images, etc.)
- Aggregates and deduplicates results intelligently

### 2. Advanced Dork Generation
Automatically generates search operator combinations:
- `site:` — restrict to specific domains
- `filetype:` — target document types (pdf, csv, json, xml)
- `intitle:` / `inurl:` — precision title/URL matching
- `before:` / `after:` — time-bounded searches
- Boolean operators: `AND`, `OR`, `NOT`, `" "`

### 3. Intelligent Search Strategies

| Strategy | Use Case |
|----------|----------|
| **Broad Sweep** | Initial exploration, topic discovery |
| **Precision Drill** | Exact fact lookup, citation finding |
| **Lateral Search** | Finding alternatives, synonyms, related concepts |
| **Temporal Search** | Recent news, historical events |
| **Deep Web Search** | Academic papers, government data, archives |

### 4. Result Processing
- Relevance scoring across sources
- Automatic summarization of top results
- Source credibility assessment
- Deduplication and clustering

---

## Configuration

\`\`\`yaml
backend: SearXNG
engines:
  - general: [google, bing, duckduckgo, brave]
  - academic: [semantic_scholar, arxiv, pubmed, base]
  - news: [bing_news, google_news, reuters]
  - code: [github, stackoverflow, gitlab]
  - images: [bing_images, unsplash, flickr]
  - data: [wolframalpha, wikidata]

max_results_per_engine: 10
timeout_seconds: 15
safe_search: moderate
language: auto-detect
\`\`\`

---

## Version History

| Version | Changes |
|---------|---------|
| v0.2.0 | Current — 5 intelligent search strategies, adaptive engine selection, result caching, credibility scoring, multilingual support |
| v0.1.2 | Multi-engine support, dork generation |
| v0.1.1 | SearXNG backend integration |
| v0.1.0 | Initial release |

