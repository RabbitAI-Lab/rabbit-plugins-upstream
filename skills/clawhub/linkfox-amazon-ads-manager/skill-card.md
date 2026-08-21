## Description:

Manages Amazon Ads Sponsored Products, Sponsored Brands, and Sponsored Display campaigns, including listing, creating, updating budgets, bids, status, keywords, targets, product ads, creatives, and budget rules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External advertisers and agent operators use this skill to manage Amazon Ads entities across SP, SB, and SD accounts after resolving the correct authorized store profile. It is suited for campaign maintenance tasks such as querying entities, changing bids or budgets, updating status, and creating advertising structures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or update Amazon Ads entities, including budgets, bids, and status, which may affect advertising spend.

Mitigation: Confirm every create, update, or purchase action before execution and review the affected entities, field changes, and budget impact.

Risk: The skill handles LinkFox onboarding, API-key generation, phone/SMS login, payment/order flows, and credential-bearing endpoint configuration.

Mitigation: Use it only with a trusted LinkFox account, keep API keys out of logs and chat transcripts, and verify any LINKFOX_* endpoint overrides before use.

Risk: Full LinkFox responses are stored locally and may contain Amazon Ads business data.

Mitigation: Regularly review and delete local linkfox response files that are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-ads-manager)
- [API overview](references/api.md)
- [Sponsored Products API reference](references/api/sp.md)
- [Sponsored Brands API reference](references/api/sb.md)
- [Sponsored Brands V3 reference](references/api/sb-v3.md)
- [Sponsored Brands V4 reference](references/api/sb-v4.md)
- [Sponsored Brands V3/V4 coexistence notes](references/api/sb-coexistence.md)
- [Sponsored Display API reference](references/api/sd.md)
- [Onboarding and billing guidance](references/onboarding.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts write full LinkFox response files under the current working directory and may summarize large responses on stdout.]

## Skill Version(s):

1.1.1 (source: server release evidence, released 2026-08-14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
