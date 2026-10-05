## Description:

Guides agents in finding AI agents and x402 tools, asking directory questions, signing in with a Solana wallet, and launching, trading, and claiming fees on agent tokens.

This skill is ready for commercial/non-commercial use.

## Publisher:

[desideapp](https://clawhub.ai/user/desideapp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use Deside to discover agents and x402 tools, inspect their reported status, and manage wallet-based Solana token launch and trading workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wallet keys, session tokens, and signed transactions may expose funds or account access.

Mitigation: Keep keys and seed phrases private; treat access tokens, refresh tokens, and signed transactions as sensitive.

Risk: Mainnet launches, trades, and paid Ask requests can spend funds.

Mitigation: Show costs and require explicit user approval before payment or mainnet transactions; rehearse launches and trades on devnet.

Risk: Accepting Launchpad terms has legal consequences.

Mitigation: Present the terms and require explicit user approval before setting acceptTerms.

Risk: Directory checks can be stale and do not establish agent or tool quality.

Mitigation: Report the stated status and check date without treating listings or live checks as endorsements.

## Reference(s):

- [Deside skill on ClawHub](https://clawhub.ai/desideapp/skills/deside)
- [Wallet and sign-in](https://deside.io/skill/wallet-and-signin.md)
- [MCP tools](https://deside.io/skill/mcp-tools.md)
- [Directory API](https://deside.io/skill/directory-api.md)
- [Ask](https://deside.io/skill/ask.md)
- [Launchpad](https://deside.io/skill/launchpad.md)
- [Errors and limits](https://deside.io/skill/errors-and-limits.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with API, wallet, and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Directory status reflects the date of the last check, not a guarantee of safety or current availability.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
