## Description:

Guides agents and developers through Nevermined payments, including purchasing plans, managing spending delegations, and protecting TypeScript or Python services with x402.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nevermined-io](https://clawhub.ai/user/nevermined-io)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers and autonomous agents use this skill to buy or sell access to AI services, manage payment plans and credits, and integrate x402 paywalls with Nevermined.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some paywall examples may expose protected content before payment settlement succeeds.

Mitigation: Confirm settlement succeeds before releasing content; buffer streaming responses or charge before streaming.

Risk: API keys and payment-signature tokens may be disclosed in logs or copied output.

Mitigation: Keep credentials and payment tokens out of logs and shared output.

Risk: Payment delegations may authorize unintended spending.

Mitigation: Test in the sandbox first and set tight delegation budgets and durations.

## Reference(s):

- [Nevermined Payments release](https://clawhub.ai/nevermined-io/skills/nevermined)
- [Nevermined API keys](https://nevermined.app)
- [Autonomous payment operations](artifact/references/autonomous-operations.md)
- [Client-side payment integration](artifact/references/client-integration.md)
- [x402 HTTP integration](artifact/references/x402-protocol.md)
- [MCP paywall integration](artifact/references/mcp-paywall.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with TypeScript, Python, and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes payment-flow and integration guidance; does not itself settle payments.]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
