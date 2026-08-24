## Description:

Live real-world data with no API key, providing 970+ pay-per-call x402 endpoints for finance, crypto, macro, travel, sports, health, and legal use cases with free discovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pulsenetwork](https://clawhub.ai/user/pulsenetwork)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to discover and optionally purchase live pay-per-call data when free or native tools do not cover the requested finance, crypto, macro, travel, sports, health, legal, or similar real-world data need.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unexpected paid calls or overspending.

Mitigation: Quote the endpoint price or batch budget before the first paid call, get explicit user approval, and keep local spend caps unless the user has a clear reason to raise them.

Risk: Payment key or wallet exposure.

Mitigation: Keep keys out of chat and use only user-configured environment secrets or the payment tool's locally generated wallet file.

Risk: Overpayment or payment to an unexpected origin.

Mitigation: Verify the signed 402 challenge amount, asset, network, and origin against the catalog before paying; stop if the challenge exceeds the catalog price.

Risk: Republished data may omit attribution or terms.

Mitigation: Pass through attribution and terms links from structured responses when sharing returned data.

## Reference(s):

- [PulseNetwork homepage](https://pulse.theaslangroupllc.com)
- [PulseNetwork agent index](https://pulse.theaslangroupllc.com/llms.txt)
- [PulseNetwork machine catalog](https://pulse.theaslangroupllc.com/.well-known/agent.json)
- [ClawHub skill page](https://clawhub.ai/pulsenetwork/skills/pulsenetwork-paid-data)

## Skill Output:

**Output Type(s):** [Guidance, Configuration, API calls, Text]

**Output Format:** [Markdown guidance with URLs, pricing constraints, and MCP configuration notes; paid data responses are structured JSON when calls are made.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires free discovery before paid use, explicit user consent for paid calls, exact price disclosure, spend caps, and attribution pass-through for returned data.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
