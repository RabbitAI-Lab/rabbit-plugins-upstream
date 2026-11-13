## Description:

Verify before you act: pay-per-call checks for bank transfers, invoices, business-day deadlines, public holidays and stablecoin transfers via agentshield.live (x402, USDC on Base). Use before money moves, an invoice is sent or paid, or a date is promised.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bartelmost](https://clawhub.ai/user/bartelmost)

### License/Terms of Use:

MIT-0

## Use Case:

Agents handling bank transfers, invoices, business-day deadlines, or stablecoin transfers use this skill to request checks before executing a transaction or committing to a date.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags financial details being sent to a third-party service without a privacy warning, with data handling and retention unclear.

Mitigation: Review the service's privacy and retention terms and confirm you are comfortable sharing each field before making a call.

## Reference(s):

- [agentshield.live routes and pricing](https://agentshield.live/llms.txt)
- [agentshield.live MCP endpoint](https://agentshield.live/mcp)
- [agentshield-agent-kit](https://github.com/bartelmost/agentshield-agent-kit)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Guidance]

**Output Format:** [JSON check results with concise procedural guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Pay-per-call checks; results are deterministic and may be stored rather than reflecting live market data.]

## Skill Version(s):

1.0.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
