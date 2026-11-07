## Description:

BlindOracle provides privacy-focused forecasting, credential verification, balance management, settlement, and cross-rail transfer capabilities for AI agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[craigmbrown](https://clawhub.ai/user/craigmbrown)

### License/Terms of Use:

Proprietary

## Use Case:

Developers and agent operators use this skill to add paid forecasting, credential checks, account balance queries, settlement requests, and cross-rail transfer workflows to OpenClaw-compatible agents. Because the skill can initiate financial settlement, conversion, swap, and withdrawal workflows, it is best used where each transaction can be reviewed and confirmed explicitly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can initiate settlement, conversion, swap, and withdrawal workflows involving funds.

Mitigation: Require explicit per-transaction user confirmation, payment-proof validation, and strict tool/domain scoping before enabling paid or fund-moving capabilities.

Risk: The security scan reports that the wrapper obscures underlying crypto rails in user-facing terminology.

Mitigation: Require truthful rail and asset names in operator-facing output and documentation before using the skill with real funds.

Risk: The security scan reports unsafe, unaudited runtime imports and dependency concerns.

Mitigation: Package or pin dependencies and review imported handler modules before deployment in autonomous or production settings.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/craigmbrown/skills/blindoracle)
- [Publisher profile](https://clawhub.ai/user/craigmbrown)
- [BlindOracle homepage](https://craigmbrown.com/blindoracle)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, API calls, Configuration, Guidance]

**Output Format:** [JSON-like request and response examples, Markdown instructions, and Python handler responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include payment-required responses, transaction details, security check details, account or quote data, and error messages.]

## Skill Version(s):

1.0.1 (source: server-resolved release evidence and artifact/SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
