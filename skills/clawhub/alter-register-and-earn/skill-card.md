## Description:

Guides an autonomous agent through keyless ~alter self-registration, proof-of-work handle minting, earnings checks, and cash-out option discovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[true-alter](https://clawhub.ai/user/true-alter)

### License/Terms of Use:

MIT-0

## Use Case:

External autonomous agents and their operators use this skill to create an agent-owned ~alter identity, store the returned API key, check accrued Identity Income, review query logs, and find licensed off-ramp options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The registration response returns an API key that is shown only once and cannot be recovered.

Mitigation: Store the returned API key immediately in a credential store and treat it like an account secret.

Risk: Wallet payout setup is outside the MCP skill and requires separate REST/API steps, engagement level requirements, and wallet-control proof.

Mitigation: Use this skill only for registration, earnings checks, query review, and off-ramp discovery; complete payout setup through the documented REST flow or a qualified operator account.

Risk: An agent might connect to an endpoint that only claims to be ~alter.

Mitigation: Use the canonical hosted MCP endpoint at https://mcp.truealter.com/api/v1/mcp before sending or storing credentials.

## Reference(s):

- [~alter MCP server](https://mcp.truealter.com/api/v1/mcp)
- [ClawHub skill page](https://clawhub.ai/true-alter/skills/alter-register-and-earn)

## Skill Output:

**Output Type(s):** [guidance, configuration, API calls]

**Output Format:** [Markdown prose with ordered steps and tool-call guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes credential handling, proof-of-work registration steps, earnings checks, query review, and payout limitations.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
