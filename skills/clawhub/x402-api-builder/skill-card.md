## Description:

Build your own pay-per-call API with the x402 standard: FastAPI + payment manifest + API keys + MCP wrapper. Sell your data/services per call (USDC). Template with ON-CHAIN payment verification (secure-by-default).

This skill is ready for commercial/non-commercial use.

## Publisher:

[northcap-group](https://clawhub.ai/user/northcap-group)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to scaffold a paid pay-per-call API with FastAPI endpoints, x402 payment discovery, USDC payment verification, API-key gating, and an MCP wrapper.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated bearer API keys are stored in a local JSON file.

Mitigation: Set restrictive permissions for api_keys.json, keep it out of source control and backups, and move to managed secret or database storage before production use.

Risk: A misconfigured payment wallet or key secret can weaken payment handling.

Mitigation: Set PAYMENT_WALLET and KEY_SECRET explicitly for each deployment and review the payment configuration before accepting live payments.

Risk: The template can expose a local API server and network endpoints.

Mitigation: Review exposed routes, require HTTPS for non-local clients, and deploy behind normal authentication, rate limiting, logging, and network controls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/northcap-group/skills/x402-api-builder)
- [Base mainnet RPC](https://mainnet.base.org)
- [Telegram Bot API](https://api.telegram.org)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python code templates and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a FastAPI server template, MCP wrapper, test client, x402 manifest guidance, payment configuration guidance, and API-key setup guidance.]

## Skill Version(s):

1.0.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
