# 2Ryun API Skill

Claude Code skill for the [2Ryun](https://2ryun.com) platform — an AI-era knowledge operating system.

## What it does

This skill enables Claude Code to interact with 2Ryun's REST API, providing:

- **Document Management** — Create, read, update, delete, import, and search documents
- **Knowledge Base** — Semantic search, knowledge graphs, automatic knowledge extraction
- **Website Generation** — Convert documents to beautiful web pages (75+ templates), build multi-page sites
- **Notes** — Lightweight notes for quick capture and memos

## Installation

```bash
# Via Claude Code Skill Marketplace (recommended)
claude install 2ryun-api

# Or manually
git clone https://github.com/iguoguo/2Ryun-skill ~/.claude/skills/2ryun-api
```

## Setup

1. Get an API Key from 2Ryun: Settings → API Keys → Create New Key
2. Set the environment variable:
   ```bash
   export RYUN_API_KEY="sk-xxxx"
   ```
3. Start using Claude Code — just mention "2Ryun", "knowledge base", or "build a site"

## Authentication

All API calls use `Authorization: Bearer <api-key>` header.

## API Documentation

Full API spec: [2ryun-api-spec.md](https://github.com/iguoguo/2Ryun/blob/main/docs/2ryun-api-spec.md)

## License

MIT
