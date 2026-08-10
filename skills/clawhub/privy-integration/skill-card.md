## Description:

Integrates Privy authentication, embedded wallets, and agent payment protocols into web and agentic apps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill to add Privy authentication, embedded wallets, smart-wallet controls, server-side token verification, and x402 or MPP payment flows to web and agentic applications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes examples for wallet transactions and paid HTTP requests that could spend funds if copied into live systems.

Mitigation: Use testnets and sandbox wallets first, and require explicit approval before transaction broadcasts or paid fetches.

Risk: Privy app secrets, webhook signing secrets, and private-key material may be exposed if placed in client code, logs, or prompts.

Mitigation: Keep secrets server-side, avoid logging sensitive values, and prevent agents from echoing credentials into prompts or generated files.

Risk: Agentic wallet, gas sponsorship, KYC, and recipient lookup flows can create authorization or compliance exposure if policies are too broad.

Mitigation: Define strict wallet policies, spending limits, recipient controls, and human approval gates before production use.

## Reference(s):

- [React SDK Reference](references/react-sdk.md)
- [Server SDK Reference](references/server-sdk.md)
- [Wallets Reference](references/wallets.md)
- [Solana Reference](references/solana.md)
- [Agent Payments Reference](references/agent-payments.md)
- [Agent Auth Reference](references/agent-auth.md)
- [Privy LLM Documentation Index](https://docs.privy.io/llms-full.txt)
- [Privy Integration Homepage](https://github.com/tenequm/skills/tree/main/skills/privy-integration)
- [ClawHub Skill Page](https://clawhub.ai/tenequm/skills/privy-integration)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline TypeScript, JavaScript, JSON, and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include environment variable names and security guidance for wallet, payment, webhook, and authentication integrations.]

## Skill Version(s):

0.4.3 (source: SKILL.md frontmatter and CHANGELOG.md, released 2026-08-07)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
