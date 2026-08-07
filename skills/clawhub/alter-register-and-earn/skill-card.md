## Description:

Use when an autonomous agent with no human account or operator session needs to register its own ~alter identity, start earning USDC, check accrued Identity Income, and find licensed cash-out options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[true-alter](https://clawhub.ai/user/true-alter)

### License/Terms of Use:

MIT-0

## Use Case:

External agents and their operators use this skill to create a first-class ~alter agent identity without a human account, retain the returned API key, and inspect identity-income and cash-out information. It is intended for agents that need their own queryable principal rather than a human member key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The registration flow can create a new ~alter agent identity and API key, with earnings records tied to that identity.

Mitigation: Use only the stated ~alter endpoint and store the returned key carefully in an appropriate credential store.

Risk: The returned API key is shown once and cannot be recovered.

Mitigation: Capture it immediately after registration; if it is lost, rerun the registration flow or use a human operator's login path instead of fabricating credentials.

Risk: Wallet payout setup is outside this MCP skill.

Mitigation: Treat cash-out guidance as informational and complete payout-wallet setup through the separate REST attestation flow or a human operator account.

## Reference(s):

- [~Alter MCP server](https://mcp.truealter.com/api/v1/mcp)
- [ClawHub skill page](https://clawhub.ai/true-alter/skills/alter-register-and-earn)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Shell commands, Configuration]

**Output Format:** [Markdown guidance with MCP tool names, endpoint configuration, and credential-handling instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or direct handling of a one-time ~alter API key returned by the registration flow.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
