## Description:

Integrates Privy authentication, embedded wallets, and agent payment protocols into web and agentic apps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill to add Privy authentication, embedded wallets, smart wallets, Solana and EVM wallet flows, x402 payments, MPP payments, and agentic wallet controls to web and agentic applications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Examples can move funds through live wallet, payment, and agent automation workflows.

Mitigation: Default to testnets or tiny balances, set explicit payment caps and allowlists, and require human approval for meaningful transfers.

Risk: Wallet secrets, Privy app secrets, webhook signing secrets, and payment identifiers may be exposed if copied into logs, code, or prompts.

Mitigation: Store secrets in environment variables or a secret manager, never hardcode or log private keys or app secrets, and treat email or phone payment identifiers as sensitive personal data.

Risk: Autonomous agent wallets may execute unintended transactions if policies are too broad.

Mitigation: Attach scoped wallet policies with spending limits, chain restrictions, contract allowlists, monitoring, and revocation paths before enabling autonomous execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/privy-integration)
- [ClawHub publisher profile](https://clawhub.ai/user/tenequm)
- [OpenClaw homepage](https://github.com/tenequm/skills/tree/main/skills/privy-integration)
- [Privy documentation index](https://docs.privy.io/llms-full.txt)
- [Privy React quickstart](https://docs.privy.io/basics/react/quickstart)
- [Privy Node.js quickstart](https://docs.privy.io/basics/nodeJS/quickstart)
- [Privy wallets overview](https://docs.privy.io/wallets/overview)
- [Privy x402 integration](https://docs.privy.io/recipes/agent-integrations/x402)
- [Privy MPP integration](https://docs.privy.io/recipes/agent-integrations/mpp)
- [Privy agentic wallets](https://docs.privy.io/recipes/agent-integrations/agentic-wallets)
- [React SDK reference](references/react-sdk.md)
- [Server SDK reference](references/server-sdk.md)
- [Wallets reference](references/wallets.md)
- [Solana integration reference](references/solana.md)
- [Agent payments reference](references/agent-payments.md)
- [Agent Auth and agentic wallets reference](references/agent-auth.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with TypeScript and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces integration guidance and examples for Privy SDK setup, wallet configuration, payment flows, and agent wallet policies.]

## Skill Version(s):

0.4.4 (source: frontmatter, changelog, and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
