## Description:

Search local documents, files, notes, and knowledge bases. Index directories, search with BM25/vector/hybrid, get AI answers with citations. Use when user wants to search files, find documents, query notes, look up information in local folders, index a directory, set up document search, build a knowledge base, needs RAG/semantic search, or wants to start a local web UI for their docs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gmickel](https://clawhub.ai/user/gmickel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, knowledge workers, and agent operators use this skill to let an agent set up and query a local GNO knowledge base, retrieve cited evidence from indexed files, manage second-brain notes and memory, and configure CLI or MCP access to local document search.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives an agent broad, purpose-aligned access to run the local GNO CLI over the user's documents.

Mitigation: Install only when local document search is intended, index only approved folders, and review the collections and scopes before retrieval or capture workflows.

Risk: Write-enabled MCP, non-loopback daemon access, publishing, export, model downloads, force flags, and broad user-scope installs can change local state or expose content when used carelessly.

Mitigation: Keep MCP read-only and loopback-only by default, enable writes or non-loopback access only when explicitly needed, review commands such as --force and publish/export, and follow collection egress policy checks.

Risk: Search, generated answers, and memory recall can be stale, incomplete, or unsupported if the local index or evidence set is out of date.

Mitigation: Check index health when freshness matters, retrieve exact passages before citing them, preserve gaps and abstentions, and verify writes with gno search, gno query, or gno get.

## Reference(s):

- [GNO ClawHub listing](https://clawhub.ai/gmickel/skills/gno)
- [README.md](README.md)
- [SKILL.md](SKILL.md)
- [CLI reference](cli-reference.md)
- [MCP reference](mcp-reference.md)
- [Usage examples](examples.md)
- [GNO agent instructions](https://gno.sh/docs/agents-install)
- [GNO MCP documentation](https://www.gno.sh/docs/MCP)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, citations, and optional JSON-producing CLI or MCP calls]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the local GNO CLI for execution; outputs may include gno:// URIs, line citations, retrieval receipts, and configuration snippets.]

## Skill Version(s):

1.2.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
