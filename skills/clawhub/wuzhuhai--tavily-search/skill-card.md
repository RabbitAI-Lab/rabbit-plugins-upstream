## Description:

Tavily Search gives AI agents web search, deep research, image search, citation-oriented source results, and structured search output through Tavily.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wuzhuhai](https://clawhub.ai/user/wuzhuhai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to let an agent query Tavily for current web results, deeper research summaries, image URLs, and JSON-formatted search responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release ships and stores Tavily API credentials in plaintext configuration.

Mitigation: Remove and revoke any bundled key before installation, avoid sensitive queries, and prefer an environment variable or OS credential manager for user credentials.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wuzhuhai/skills/tavily-search)
- [Tavily Website](https://tavily.com/)
- [Tavily Search API Endpoint](https://api.tavily.com/search)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, API calls, shell commands, configuration]

**Output Format:** [Plain text or JSON search results with answer text, source URLs, optional image URLs, and response metadata.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search behavior depends on Tavily API availability and on the configured API key.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter, package.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
