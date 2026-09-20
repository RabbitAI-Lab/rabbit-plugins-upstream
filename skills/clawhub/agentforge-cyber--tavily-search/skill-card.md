## Description:

Tavily AI search tool for agents that supports real-time web search, deeper research, image search, citation generation, and structured search results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentforge-cyber](https://clawhub.ai/user/agentforge-cyber)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent query Tavily for current web information, research summaries, image URLs, and source-linked structured results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release evidence reports that the artifact ships a plaintext Tavily API key.

Mitigation: Revoke or remove the bundled key before use and configure a user-controlled credential through a safer storage method.

Risk: Search queries are transmitted to Tavily's third-party API and may expose sensitive terms.

Mitigation: Do not send secrets, private business terms, or regulated data unless Tavily use is approved for that data.

Risk: The security verdict is suspicious because credential handling and third-party query disclosure are weak.

Mitigation: Review and fix credential handling and disclosure before broad deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/agentforge-cyber/skills/tavily-search)
- [Tavily website](https://tavily.com/)
- [Tavily Search API endpoint](https://api.tavily.com/search)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Plain text or JSON search results with answers, source URLs, dates, snippets, optional image URLs, and response timing.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Tavily API key and sends search queries to Tavily's third-party API.]

## Skill Version(s):

1.0.0 (source: release evidence, frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
