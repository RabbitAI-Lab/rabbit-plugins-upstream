## Description:

Issue and manage wallet-owned virtual cards through x402.

This skill is ready for commercial/non-commercial use.

## Publisher:

[elvismusli](https://clawhub.ai/user/elvismusli)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to discover, issue, top up, and manage a wallet-owned x402card virtual card while validating exact Base-USDC payment details and preserving owner-only credential handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The one-line remote shell installer creates supply-chain risk for a wallet and payment workflow.

Mitigation: Prefer a source checkout or versioned release with verifiable checksums or signatures, and inspect the installer before running it.

Risk: Payment actions can move funds if a wallet signer approves an incorrect or repeated request.

Mitigation: Use a wallet or signer with limited funds and require explicit confirmation for each payment action, including amount, network, payee, resource, and idempotency key.

Risk: Virtual card credentials may be exposed through chat, logs, stdout, files, or model context.

Mitigation: Reveal credentials only after fresh owner authentication and keep them out of MCP, chat transcripts, logs, stdout, files, and model context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/elvismusli/skills/x402card-agent)
- [x402card card discovery API](https://api.x402card.org/api/card/discovery)
- [x402card agent API](https://api.x402card.org/api/agent)
- [x402card top-up discovery API](https://api.x402card.org/api/card/topup/discovery)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with inline commands and API endpoints]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes wallet/payment validation steps and owner-authenticated card management guidance.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
