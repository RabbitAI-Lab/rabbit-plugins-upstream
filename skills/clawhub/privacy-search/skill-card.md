## Description:

Privacy Search provides a privacy-oriented multi-engine search workflow with CLI and MCP tools for parallel search, answer synthesis, page fetching, caching, export, ranking, diagnostics, and local SearXNG integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to add privacy-oriented web search, source-backed answer synthesis, and page fetching to command-line workflows or MCP-compatible agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive search queries and fetched page content can leave the machine when external search engines, page fetching, or synthesis providers are used.

Mitigation: Use strict mode, local SearXNG where appropriate, and avoid external LLM synthesis for confidential work unless privacy controls are explicitly configured.

Risk: Local cache and search history can retain sensitive query material on disk.

Mitigation: Disable cache/history for sensitive workflows or clear them after use with the documented cache and history commands.

Risk: Setup, update checks, Docker or pip-based SearXNG installation, and MCP use broaden the host and network impact of the skill.

Mitigation: Review setup steps before installation, disable startup update checks if needed, and run the MCP server only in trusted local agent environments.

## Reference(s):

- [ClawHub privacy-search release page](https://clawhub.ai/fyniujin/skills/privacy-search)
- [Quick Start](references/QUICK_START.md)
- [Search engine adapters](references/engines.md)
- [Chinese engines and fallback strategy](references/engines_zh.md)
- [MCP tool schema](references/mcp_schema.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance, CLI text, JSON search results, MCP JSON-RPC tool responses, and exported Markdown/HTML/PDF search results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include result URLs, snippets, source citations, cache status, diagnostic notices, fetched page text, and privacy reports.]

## Skill Version(s):

1.7.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
