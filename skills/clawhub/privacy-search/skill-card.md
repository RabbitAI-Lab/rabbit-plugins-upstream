## Description:

privacy-search helps agents run privacy-oriented parallel web search across multiple engines, manage local SearXNG, cache and rank results, fetch page text, export results, and generate summaries with an extractive fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and privacy-conscious users use this skill to perform multi-engine web searches, compare ranked results, manage local SearXNG, export findings, and summarize fetched pages while controlling privacy settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic update checks can create non-search outbound connections.

Mitigation: Disable update checks when minimizing outbound connections is required.

Risk: Local cache and search history can persist sensitive queries or result data on disk.

Mitigation: Disable cache/history or clear them before use on shared or monitored machines.

Risk: Strict privacy mode does not hide the user's IP address by itself.

Mitigation: Configure a proxy or VPN when IP privacy is required.

Risk: Using LLM summaries with an API key can send queries or results to the LLM provider.

Mitigation: Avoid summarization for sensitive searches unless that data transfer is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/privacy-search)
- [Quick start guide](references/QUICK_START.md)
- [Search engine reference](references/engines.md)
- [Chinese engine and fallback strategy reference](references/engines_zh.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [CLI text, JSON search results, Markdown/HTML/PDF exports, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include cached search results, privacy reports, diagnostics, fetched page text, and optional summaries.]

## Skill Version(s):

1.5.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
