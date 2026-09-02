## Description:

money-machine-x402 gives agents and HTTP clients instructions for buying and downloading a paid trader toolkit through an x402 Base USDC payment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ssidharhubble](https://clawhub.ai/user/ssidharhubble)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to understand the paid x402 purchase flow, call the documented endpoint, and retrieve the trader toolkit after payment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may pay an external x402 USDC endpoint before confirming that the seller and service are trustworthy.

Mitigation: Verify the publisher, confirm the endpoint is live, and proceed only if the Base USDC payment address and payment flow are acceptable.

Risk: The artifact does not independently prove the quality of the downloaded financial toolkit.

Mitigation: Inspect downloaded files and validate formulas before relying on them for trading, tax, or investment decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ssidharhubble/skills/money-machine-x402)
- [Publisher profile](https://clawhub.ai/user/ssidharhubble)
- [Health check endpoint](https://money-machine-api-ssyopros.zocomputer.io/api/ping)
- [Trader toolkit purchase endpoint](https://money-machine-api-ssyopros.zocomputer.io/api/trader-toolkit)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files]

**Output Format:** [Markdown with inline bash commands and endpoint URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paid x402 endpoint is documented to return a downloadable toolkit after successful payment.]

## Skill Version(s):

2.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
