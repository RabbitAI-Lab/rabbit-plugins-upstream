## Description:

Searches and browses product listings across multiple eBay international marketplaces for price comparison, sold-listing research, auction discovery, and market analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, e-commerce sellers, buyers, and analysts use this skill to search eBay listings, compare prices, inspect sold or completed listings, and evaluate marketplace conditions across supported regional eBay domains.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends eBay search queries, session metadata, feedback content, account onboarding data, API keys, and paid-credit workflow data to LinkFox services.

Mitigation: Install and run it only in environments where LinkFox handling of that data is acceptable, and control the configured LinkFox API key and related environment variables.

Risk: The security review verdict is suspicious and notes persistent local storage of LinkFox output files.

Mitigation: Review the skill before deployment, avoid sensitive workspaces, and manage or remove local linkfox result files according to the workspace's data-retention expectations.

Risk: Search calls consume paid credits, and repeated calls can create unexpected cost.

Mitigation: Use cached results when possible and confirm with the user before making additional searches, pagination calls, or changed-parameter retries.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-ebay-search)
- [eBay search API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, API calls, JSON files, guidance]

**Output Format:** [Markdown summaries and tables, shell commands, configuration snippets, API responses, and saved JSON result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search responses may be cached for 24 hours and full results may be written under a local linkfox session directory.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
