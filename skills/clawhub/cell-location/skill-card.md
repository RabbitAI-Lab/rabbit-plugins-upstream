## Description:

Provides paid cell-tower location lookup from MCC, MNC, TAC/LAC, and CI values through Juhe's API and an Alipay AI payment flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[juhemcp](https://clawhub.ai/user/juhemcp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to resolve a base-station identifier tuple into basic geographic location information after confirming payment. It is intended for authorized location checks, nearby-service support, and cell-site position verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The lookup sends user-provided cell-tower identifiers to Juhe's third-party API.

Mitigation: Use the skill only when the user is comfortable sharing those identifiers with Juhe and only for locations they are authorized to check.

Risk: The skill uses a paid Alipay flow before returning precise location data.

Mitigation: Confirm the submitted parameters and payment details with the user before proceeding.

Risk: Cell-tower location data could be misused to locate another person without consent.

Mitigation: Decline requests that appear to involve unauthorized tracking or non-consensual location checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/cell-location)
- [Juhe A2A query endpoint](https://apis.juhe.cn/a2a/query)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Guidance, Text]

**Output Format:** [Markdown guidance with JSON request examples and payment-flow instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return order details, latitude, longitude, and address when payment and lookup succeed.]

## Skill Version(s):

1.0.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
