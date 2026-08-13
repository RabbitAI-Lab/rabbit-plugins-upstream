## Description:

Queries Jungle Scout historical exact-match Amazon keyword search volume in weekly periods across supported marketplaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and ecommerce analysts use this skill to retrieve weekly keyword search-volume history, inspect trend direction, and compare seasonality across supported Amazon marketplaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes account registration, API-key setup, billing, payment, and payment QR-code behavior beyond read-only keyword lookup.

Mitigation: Use it only when those account and billing flows are expected, and require explicit user confirmation before registration, payment, package ordering, or API-key configuration.

Risk: The skill can save full API responses to local linkfox session directories.

Mitigation: Review stored files for sensitive keyword, account, or billing data and limit access to the workspace where the skill runs.

Risk: Automatic feedback submission can transmit information about user satisfaction or task outcomes.

Mitigation: Confirm feedback behavior is acceptable for the deployment context before enabling the skill.

## Reference(s):

- [Jungle Scout keyword history API reference](artifact/references/api.md)
- [Authentication and billing onboarding](artifact/references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-junglescout-keyword-history)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API responses and saved JSON result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may be cached for 24 hours and full API responses may be written under a local linkfox session directory; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
