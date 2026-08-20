## Description:

Federated web search across multiple providers with explainable routing, extraction, crawl and research outputs, multilingual search, sourced answers, and news monitoring alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mohamedabdisamed](https://clawhub.ai/user/mohamedabdisamed)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run web and news searches, route across available providers, return sourced answers, and monitor topics for newly discovered results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and provider API calls may be sent to third-party services and may be logged or billed.

Mitigation: Avoid sensitive or internal queries, and review each configured provider's API-key billing, retention, and logging policies before use.

Risk: Local search cache or watch state may retain query history or monitored topics.

Mitigation: Run the skill in an appropriate workspace, clear local cache or watch state when no longer needed, and avoid monitoring sensitive topics.

Risk: The published artifact appears incomplete because search.mjs imports missing lib files.

Mitigation: Verify the package contains the required lib modules and run a basic search command before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mohamedabdisamed/skills/csu-min)
- [Publisher profile](https://clawhub.ai/user/mohamedabdisamed)
- [Web Search Pro project referenced by artifact](https://github.com/Zjianru/web-search-pro)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON search results with sourced-answer summaries and status text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include provider selection, routing summary, source URLs, federation telemetry, cache metadata, and watch-state updates.]

## Skill Version(s):

1.0.0 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
