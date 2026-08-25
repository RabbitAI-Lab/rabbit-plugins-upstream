## Description:

Queries LinkFox SIF keyword-overview data to summarize Amazon keyword competition, supply-demand ratio, search volume estimates, popularity rank, and ad or product counts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and e-commerce analysts use this skill to request keyword-level SIF metrics from LinkFox and compare competition, search demand, advertising density, and marketplace coverage for a single Amazon keyword.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends keyword queries, API keys, and session metadata to LinkFox services.

Mitigation: Use it only if you trust LinkFox with that data, and confirm any LINKFOX_* endpoint environment variables point to legitimate LinkFox domains.

Risk: The onboarding flow can involve phone verification, API-key setup, persistent credentials, and billing actions.

Mitigation: Provide SMS codes, persist credentials, or create payment orders only when you explicitly intend to register, authenticate, or recharge the account.

Risk: Automatic feedback reporting may submit feedback content to LinkFox.

Mitigation: Review the feedback behavior before installation and avoid sharing sensitive user or business content through feedback reports.

## Reference(s):

- [SIF keyword overview API reference](references/api.md)
- [Authentication and credits onboarding](references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-sif-keyword-overview)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON files, guidance]

**Output Format:** [Markdown summaries and tables, JSON API responses, and saved JSON data files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Queries one keyword per API call; full responses are saved under the working directory, and small responses may also print inline.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
