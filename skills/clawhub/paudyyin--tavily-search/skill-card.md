## Description:

Tavily Search gives AI agents web search, research-mode synthesis, image search, citations, and structured search results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paudyyin](https://clawhub.ai/user/paudyyin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to let agents query Tavily for current web results, research summaries, image URLs, citations, and JSON-formatted search responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package ships with an exposed Tavily API key and stores configured API keys in plaintext config.json.

Mitigation: Revoke and replace the bundled key before use, avoid placing secrets in search queries, and prefer environment variables or an OS credential manager instead of plaintext storage.

Risk: Search queries and optional raw content requests are sent to Tavily.

Mitigation: Do not submit confidential data, credentials, or sensitive internal material in queries; review returned sources before relying on results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/tavily-search)
- [Tavily website](https://tavily.com/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Plain text or JSON search results with titles, URLs, summaries, answer text, image URLs, and timing metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Tavily web search API responses; users can request basic search, research mode, image search, and optional raw content.]

## Skill Version(s):

1.0.0 (source: frontmatter, package.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
