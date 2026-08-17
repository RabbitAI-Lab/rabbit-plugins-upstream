## Description:

Helps agents manage Amazon Seller store authorization by generating authorization links, listing authorized stores, refreshing token status, and confirming seller and region context for downstream workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and ecommerce operators use this skill to connect Amazon Seller accounts to LinkFox, manage authorized stores, refresh authorization state, and prepare sellerId plus region selectors for downstream Amazon workflows.

### Deployment Geography for Use:

Global; marketplace operations are scoped by the skill's NA, EU, and FE region codes.

## Known Risks and Mitigations:

Risk: The skill handles sensitive Amazon access tokens, refresh tokens, LinkFox API keys, and local response files.

Mitigation: Use only in a trusted workspace, avoid exposing tokens in chat or logs, prefer status metadata over raw token values, and review saved linkfox response files before sharing or committing them.

Risk: The onboarding flow can perform LinkFox login, API key issuance, plan selection, and payment order creation.

Mitigation: Run onboarding and payment commands only after explicit user intent, confirm LinkFox endpoints and environment variables, and treat payment selection as a separate sensitive action.

Risk: The server security verdict is suspicious because the skill includes token handling, account login, payment flows, feedback reporting, and local response storage.

Mitigation: Review the artifact before installing, confirm the LinkFox endpoints are controlled, and avoid automatic retries or repeated paid actions without user confirmation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-store-auth)
- [Amazon Store Authorization Skill README](artifact/README.md)
- [Amazon Store Authorization API Reference](artifact/references/api.md)
- [Amazon Store Authorization Flow](artifact/references/authorization-flow.md)
- [Amazon Store Authorization Quick Start](artifact/references/quick-start.md)
- [Authentication and Billing Onboarding](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Configuration]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save full API responses to local linkfox session files and print summaries for large responses; token query and refresh scripts strip raw token fields before display.]

## Skill Version(s):

1.0.7 (source: evidence.release.version; artifact _meta.json reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
