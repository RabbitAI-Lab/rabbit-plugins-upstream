## Description:

Preflight an x402 payment or screen a public payee with SpendPreflight. Use only preflight_payment and check_payee. Defaults to offline hold with no signer; paid API calls require explicit human approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wisted-1](https://clawhub.ai/user/wisted-1)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers and agent operators use SpendPreflight to evaluate a supplied x402 payment challenge against a local spend policy or screen a public payee through an already configured MCP connection. Offline mode returns a hold or unknown status; each potentially paid remote screening call requires explicit approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A remote screening call to the external service may incur a separate USDC fee.

Mitigation: Show the current quote or hard cap and obtain explicit human approval for each potentially paid call; hold if the transport cannot enforce the approved cap.

Risk: Offline checks have no remote evidence, and a screening allow result is not authorization to pay a target merchant.

Mitigation: Preserve hold and unknown outcomes, report the result's scope, and require separate human authorization for any target payment.

Risk: The security assessment is incomplete: it covered five of six components, and a static misuse check was degraded.

Mitigation: Treat the benign, medium-confidence assessment as incomplete and review the external service use against your needs.

## Reference(s):

- [Setup, scope and offline example](artifact/references/usage.md)
- [SpendPreflight MCP and Spend Policy](https://docs.spendpreflight.com/mcp/)
- [SpendPreflight SDK 0.4.0](https://www.npmjs.com/package/spendpreflight/v/0.4.0)
- [OpenClaw skill format](https://docs.openclaw.ai/clawhub/skill-format)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Guidance]

**Output Format:** [Structured screening and preflight results with concise human-readable guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offline checks preserve hold or unknown outcomes when remote evidence is unavailable; an allow result is screening only.]

## Skill Version(s):

1.0.0 (source: package.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
