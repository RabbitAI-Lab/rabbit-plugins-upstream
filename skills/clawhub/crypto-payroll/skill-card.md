## Description:

Prepares and executes USDC payroll on Base for a roster in one on-chain transaction through the Spraay gateway, with local checks and separate approvals before sharing data, paying for the API call, and signing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[plagtech](https://clawhub.ai/user/plagtech)

### License/Terms of Use:

MIT-0

## Use Case:

Payroll operators use this skill to validate a recipient roster locally and prepare a USDC pay run on Base for treasury-wallet approval and signing. It does not handle payroll compliance, tax withholding, or worker classification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes paid non-payroll gateway actions outside its stated payroll scope.

Mitigation: Limit this skill to explicitly requested USDC payroll runs; use separate workflows with their own approval, validation, and signing controls for other gateway actions.

Risk: Recipient wallet addresses and payment amounts become public on-chain, and confirmed transfers cannot be reversed.

Mitigation: Keep HR fields out of the roster sent to the gateway, confirm wallet changes with the user, and verify every recipient, amount, fee, and contract before signing.

Risk: Paid gateway calls and treasury-wallet signatures can incur costs or transfer funds.

Mitigation: Obtain distinct user approvals before any paid call and before signing; stop if the quoted API price or decoded transactions differ from the approved run.

## Reference(s):

- [Spraay Protocol documentation](https://docs.spraay.app)
- [Spraay Protocol](https://spraay.app)
- [Spraay gateway x402 discovery](https://gateway.spraay.app/.well-known/x402.json)

## Skill Output:

**Output Type(s):** [Text, JSON, Code, Shell commands, Guidance]

**Output Format:** [Markdown guidance, local roster JSON and validation code, and transaction details for wallet review]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports payment only after on-chain confirmation; requires separate user approvals before data transfer, paid calls, and signing.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
