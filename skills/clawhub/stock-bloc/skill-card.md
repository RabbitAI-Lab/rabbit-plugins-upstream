## Description:

Helps agents register with Stock Bloc and access market data, quant signals, SEC filings, and research through per-call payments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jaywestphilly](https://clawhub.ai/user/jaywestphilly)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to connect agents to Stock Bloc for market intelligence and research, with approval before wallet payments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent wallet signatures could authorize unintended USDC spending on Stock Bloc calls.

Mitigation: Set strict local spending limits; verify network, asset, destination, and amount against the published price catalog; require human approval before each USDC signature.

## Reference(s):

- [Source repository](https://github.com/Jaywestphilly/stock-bloc-skill)
- [Stock Bloc machine documentation](https://stockbloc.ai.studio/llms.txt)
- [Stock Bloc API specification](https://stockbloc.ai.studio/api/v1/openapi.json)
- [Stock Bloc x402 discovery](https://stockbloc.ai.studio/.well-known/x402)

## Skill Output:

**Output Type(s):** [Text, Guidance, API calls]

**Output Format:** [Markdown guidance and HTTP requests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses depend on Stock Bloc API availability and per-call payment authorization.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
