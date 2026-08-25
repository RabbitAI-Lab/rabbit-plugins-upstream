## Description:

Federated web search across 10+ search engines (DuckDuckGo, Brave, Google, Bing), multi-language, news-aware, answer-first results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[northcap-group](https://clawhub.ai/user/northcap-group)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run federated web or news searches, compare provider routing, and produce short source-backed answers from search results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries may be sent to configured external search providers.

Mitigation: Avoid sensitive query text unless the configured provider and its data handling are acceptable for the use case.

Risk: The package is incomplete because imported scripts/lib modules are missing.

Mitigation: Supply and review the missing runtime modules before relying on the search, cache, routing, or provider behavior.

Risk: Monitoring stores result URLs locally and notification behavior may change if real Slack or Telegram integration is added.

Mitigation: Use non-sensitive monitored topics and review notification destinations and local state retention before enabling alerts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/northcap-group/skills/clawsearch-ultra)
- [Publisher profile](https://clawhub.ai/user/northcap-group)

## Skill Output:

**Output Type(s):** [text, markdown, JSON]

**Output Format:** [Plain text, Markdown, or JSON search result summaries with source URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include selected provider, routing summary, federated provider usage, cache status, and source URLs.]

## Skill Version(s):

1.0.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
