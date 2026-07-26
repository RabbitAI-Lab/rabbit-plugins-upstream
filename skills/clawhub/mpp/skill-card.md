## Description: <br>
MPP helps developers build Machine Payments Protocol integrations for HTTP 402 paid APIs, payment-gated content, AI agent payments, MCP tool payments, and streaming or session-based billing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tenequm](https://clawhub.ai/user/tenequm) <br>

### License/Terms of Use: <br>
Apache 2.0 <br>


## Use Case: <br>
Developers and engineers use this skill to implement, test, and troubleshoot HTTP 402 machine-payment flows for paid APIs, payment-gated services, MCP tools, and agentic payment workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Wallet keys, mnemonics, Stripe keys, Privy secrets, and upstream API keys may be exposed or misused when adapting examples. <br>
Mitigation: Use environment variables or a secret manager, avoid hardcoding credentials, and treat all payment and upstream API credentials as production secrets. <br>
Risk: Automatic payment handling can spend real funds or retry paid requests unexpectedly. <br>
Mitigation: Start with sandbox or testnet flows, restrict payment clients to trusted origins, set spend limits, and require confirmation or logging for automatic retries. <br>
Risk: Generated integration code or guidance can misconfigure payment challenges, sessions, or SDK versions. <br>
Mitigation: Review proposed changes before execution, test against the referenced protocol and SDK documentation, and keep client and server payment flows on compatible versions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tenequm/skills/mpp) <br>
- [ClawHub metadata homepage](https://github.com/tenequm/skills/tree/main/skills/mpp) <br>
- [MPP website](https://mpp.dev) <br>
- [Payment HTTP Authentication Scheme](https://datatracker.ietf.org/doc/draft-ryan-httpauth-payment/) <br>
- [Protocol spec](references/protocol-spec.md) <br>
- [TypeScript SDK](references/typescript-sdk.md) <br>
- [Python SDK](references/python-sdk.md) <br>
- [Rust SDK](references/rust-sdk.md) <br>
- [Sessions](references/sessions.md) <br>
- [Transports](references/transports.md) <br>
- [Tempo payment method](references/tempo-method.md) <br>
- [Stripe payment method](references/stripe-method.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with code snippets, shell commands, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference credential environment variables and payment settings that require user-supplied secrets.] <br>

## Skill Version(s): <br>
0.8.3 (source: server release metadata, SKILL.md frontmatter, CHANGELOG.md; released 2026-07-22) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
