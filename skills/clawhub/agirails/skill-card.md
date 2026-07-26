## Description: <br>
Trustless payment protocol for AI agents - ACTP escrow and x402 instant payments, settled in USDC on Base L2. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unima3x](https://clawhub.ai/user/unima3x) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to configure AI agents that can pay for services, earn USDC, and manage escrow or instant payment flows. It guides wallet setup, network selection, payment-mode choice, code generation, and operational checks for AGIRAILS ACTP and x402 payments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill enables real-money blockchain payment flows and can help agents submit USDC escrow or instant payment transactions. <br>
Mitigation: Start in mock or testnet, use a dedicated low-balance wallet, configure strict spending limits and provider whitelists, and move to mainnet only after reviewing the security checklist. <br>
Risk: Wallet credentials, keystores, or raw private keys may expose funds if mishandled. <br>
Mitigation: Prefer encrypted keystores or ACTP_KEYSTORE_BASE64 with ACTP_KEY_PASSWORD, avoid raw private keys, keep secrets out of source files and logs, and use the deploy check before production. <br>
Risk: Cron jobs, external API, WhatsApp, IPFS, S3, or other integration examples can expand the agent's operational reach. <br>
Mitigation: Review and approve each integration before enabling it, keep alerts and transaction logs active, and pause payment automation when anomalies appear. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unima3x/skills/agirails) <br>
- [AGIRAILS documentation](https://docs.agirails.io) <br>
- [AGIRAILS FAQ](https://agirails.app/faq) <br>
- [AGIRAILS SDK for npm](https://www.npmjs.com/package/@agirails/sdk) <br>
- [AGIRAILS SDK for Python](https://pypi.org/project/agirails/) <br>
- [ACTP State Machine](references/state-machine.md) <br>
- [Requester Template](references/requester-template.md) <br>
- [Provider Template](references/provider-template.md) <br>
- [OpenClaw Security Checklist](openclaw/security-checklist.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline TypeScript, JavaScript, Python, JSON, and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Interactive onboarding guidance before code generation; outputs can include wallet setup, network mode, provider/requester templates, and payment verification steps.] <br>

## Skill Version(s): <br>
3.0.12 (source: server release metadata; artifact frontmatter is 3.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
