## Description:

Looks up Amazon products in the same Jiimore niche as a reference ASIN and helps filter competitors by conversion, click, sales, review, rating, price, fee, and margin metrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and e-commerce analysts use this skill to find same-niche competitors for a reference ASIN, compare market metrics, and decide which competitor records to inspect further.

### Deployment Geography for Use:

Global use; Amazon marketplace data is limited to US, JP, and DE.

## Known Risks and Mitigations:

Risk: The skill uses a LinkFox API key and may guide users through account login flows.

Mitigation: Prefer self-service API key setup, avoid sharing SMS codes with the agent, and rotate or remove keys that are no longer needed.

Risk: The skill includes billing and payment-order flows and each uncached competitor lookup consumes credits.

Mitigation: Review any payment order before paying and confirm expected credit cost before repeated or paginated lookups.

Risk: The skill stores full API responses, session metadata, and cache files under a local linkfox directory.

Mitigation: Treat saved product research data as sensitive business data and periodically delete local linkfox session and cache files.

Risk: The skill can report feedback about skill behavior to a separate LinkFox feedback API.

Mitigation: Review feedback content before sending and avoid including confidential product, account, or customer information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-jiimore-page-asins-by-asin)
- [LinkFox publisher profile](https://clawhub.ai/user/linkfox-ai)
- [API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON files, guidance]

**Output Format:** [Markdown guidance with shell command examples, stdout summaries, and JSON API responses saved to local files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a reference ASIN and LinkFox API key; uncached calls consume LinkFox credits.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
