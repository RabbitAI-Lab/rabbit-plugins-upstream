## Description: <br>
Integrates Privy authentication, embedded wallets, and agent payment protocols into web and agentic apps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tenequm](https://clawhub.ai/user/tenequm) <br>

### License/Terms of Use: <br>
Apache 2.0 <br>


## Use Case: <br>
Developers and engineers use this skill to add Privy authentication, embedded wallets, smart wallets, Solana support, and agent payment protocols such as x402 and MPP to web or agentic applications. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Payment and wallet examples can enable automatic crypto payments or autonomous spending if copied into production without limits. <br>
Mitigation: Use testnets or small balances first, require explicit user confirmation, set spend caps, and allowlist payment destinations and contracts. <br>
Risk: Server-side signing, private-key handling, account deletion, and webhook examples can affect account control if credentials or authorization checks are mishandled. <br>
Mitigation: Keep PRIVY_APP_SECRET server-only, verify webhooks, validate transactions before signing, and wrap account creation or deletion in authorization, consent, logging, and recovery controls. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/tenequm/skills/privy-integration) <br>
- [Skill Homepage](https://github.com/tenequm/skills/tree/main/skills/privy-integration) <br>
- [React SDK Reference](references/react-sdk.md) <br>
- [Server SDK Reference](references/server-sdk.md) <br>
- [Wallets Reference](references/wallets.md) <br>
- [Solana Integration Reference](references/solana.md) <br>
- [Agent Payments Reference](references/agent-payments.md) <br>
- [Agent Auth and Agentic Wallets Reference](references/agent-auth.md) <br>
- [Privy Documentation Index](https://docs.privy.io/llms-full.txt) <br>
- [Privy Documentation](https://docs.privy.io) <br>
- [x402 Protocol](https://x402.org) <br>
- [MPP Protocol](https://mpp.dev) <br>
- [Agent Auth Protocol](https://agentauthprotocol.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline code and shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only guidance; examples should be reviewed before production use.] <br>

## Skill Version(s): <br>
0.4.2 (source: SKILL.md metadata and CHANGELOG, released 2026-07-22) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
