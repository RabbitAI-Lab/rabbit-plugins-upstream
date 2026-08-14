## Description:

Helps an autonomous agent register its own ~alter identity, check accrued Identity Income, and find licensed cash-out options without a human account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[true-alter](https://clawhub.ai/user/true-alter)

### License/Terms of Use:

MIT-0

## Use Case:

Autonomous agents and their operators use this skill to mint a ~alter handle through proof-of-work registration, preserve the returned API key, inspect earnings, and locate off-ramp options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The one-time API key can authorize later Alter calls if exposed.

Mitigation: Store the returned API key securely, avoid pasting it into public chats or logs, and rotate or re-register if it is exposed.

Risk: Agents without code execution cannot complete the proof-of-work registration flow.

Mitigation: Confirm local code execution is available before starting registration, and stop rather than guessing a nonce when execution is unavailable.

Risk: Cash-out setup is not completed entirely through MCP.

Mitigation: Use the skill only to inspect earnings and locate licensed off-ramp options; complete wallet attestation and payout setup through the documented non-MCP flow.

## Reference(s):

- [~alter MCP server](https://mcp.truealter.com/api/v1/mcp)
- [ClawHub skill page](https://clawhub.ai/true-alter/skills/alter-register-and-earn)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with Python and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires local code execution to solve the proof-of-work nonce; the returned API key is shown once and must be stored securely.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
