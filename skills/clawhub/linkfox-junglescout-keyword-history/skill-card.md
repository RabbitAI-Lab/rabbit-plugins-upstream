## Description:

Queries weekly exact-match Amazon keyword search-volume history from Jungle Scout across 10 marketplaces for trend and seasonality analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace analysts, and agents use this skill to query historical Amazon keyword search volume, identify seasonality, compare periods, and summarize demand trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles LinkFox/Jungle Scout account setup, API keys, and payment-order workflows.

Mitigation: Prefer creating accounts, adding credits, and storing API keys through first-party LinkFox pages, then verify endpoint environment variables before use.

Risk: Keyword-history queries consume paid credits, and repeated calls can add cost.

Mitigation: Confirm the intended marketplace, keyword, and date range before running queries, and avoid automatic retries or exploratory repeated calls without user approval.

Risk: The skill saves full API responses, including queried keywords and returned data, under a local linkfox directory or fallback location.

Mitigation: Review the local output location and avoid querying sensitive keywords unless local storage is acceptable.

## Reference(s):

- [Jungle Scout keyword history API reference](artifact/references/api.md)
- [LinkFox authentication and billing onboarding](artifact/references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-junglescout-keyword-history)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON files, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses saved to local files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Queries consume paid credits; full responses are saved under a local linkfox dated session directory, with stdout summarized for larger responses unless inline output is requested.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
