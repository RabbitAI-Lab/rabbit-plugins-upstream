## Description:

Helps Amazon sellers query and analyze nearly three years of weekly Amazon Brand Analytics search term data across 15 marketplaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and ecommerce analysts use this skill to turn natural-language ABA search term questions into LinkFox API queries for keyword trends, marketplace opportunity discovery, click-share analysis, conversion-share analysis, and downloadable result review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends ABA query intent, API credentials, and session metadata to LinkFox-controlled endpoints.

Mitigation: Install and use it only when LinkFox is an approved vendor for the workspace, and verify endpoint environment variables before making queries.

Risk: The onboarding flow can handle phone login, SMS codes, API-key generation, and billing actions.

Mitigation: Avoid sharing SMS codes or API keys in ordinary chat unless necessary, and require explicit user confirmation before recharge or paid-query steps.

Risk: Query responses, caches, and download URLs may contain sensitive business data.

Mitigation: Treat saved linkfox data and cache files as sensitive, limit access to the workspace, and avoid exposing generated download links beyond intended recipients.

Risk: The service may consume credits dynamically and can incur substantial cost for some queries.

Mitigation: Explain credit consumption before execution and do not retry, broaden, or paginate failed or empty queries without user approval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-aba-intelligent-query)
- [ABA intelligent query API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API parameters, shell commands, tabular result summaries, and saved JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are saved under a linkfox workspace data directory; small responses may also be printed as JSON, while larger responses print summaries unless inline output is requested.]

## Skill Version(s):

1.0.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
