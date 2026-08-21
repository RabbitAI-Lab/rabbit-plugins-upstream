## Description:

Federated web search across 10+ search engines with multi-language, news-aware, and answer-first results for agent workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[northcap-group](https://clawhub.ai/user/northcap-group)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to run federated web and news searches, produce answer-first summaries with sources, and monitor topics for newly discovered results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and results may be sent to configured search providers and may be retained locally through cache or watch state.

Mitigation: Use only approved providers for the deployment, avoid sensitive queries unless policy permits them, and clear local cache or watch state when retention is not acceptable.

Risk: The packaged artifact appears incomplete because local lib modules required by the search runtime are not included.

Mitigation: Treat the release as incomplete until the missing runtime modules are supplied and the scripts are tested in the target environment.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/northcap-group/skills/clawsearch-ultra)
- [Web Search Pro reference project](https://github.com/Zjianru/web-search-pro)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON search results with source URLs, routing details, cache indicators, and provider metadata.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires node and curl; optional provider API keys enable premium search backends.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
