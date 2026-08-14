## Description:

Use when an agent needs to confirm a specific person is a known, verified identity before transacting with them, granting access, accepting a claim about their credentials, or relaying a decision on their behalf.

This skill is ready for commercial/non-commercial use.

## Publisher:

[true-alter](https://clawhub.ai/user/true-alter)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agent builders use this skill to verify a named person's ~alter registration, verification tier, archetype, or trait-range claims before taking a meaningful action such as payment, access, or relaying a credential claim.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends a specific person's identifier and optional claim checks to ~alter's hosted MCP service.

Mitigation: Use it only for a real transaction, access decision, or credential claim, and avoid speculative lookups.

Risk: Trait verdicts with no data can be mistaken for failed claims.

Mitigation: Read has_data beside each trait verdict and treat has_data false as nothing tested, not as a failed claim.

Risk: Engagement level can be misused as a permission or trust score.

Mitigation: Use verification tier for identity checks and trait ranges for specific claims; do not gate decisions on engagement level alone.

## Reference(s):

- [~alter MCP service](https://mcp.truealter.com/api/v1/mcp)
- [ClawHub skill page](https://clawhub.ai/true-alter/skills/alter-verify-human)
- [~alter publisher profile](https://clawhub.ai/user/true-alter)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Configuration]

**Output Format:** [Markdown guidance with JSON tool-call examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ALTER_API_KEY for the hosted ~alter MCP service.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
