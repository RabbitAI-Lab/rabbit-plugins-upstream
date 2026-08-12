## Description:

Tracks FOMO App smart-money wallets and helps agents list wallets, inspect wallet details, check live balances, and produce current token-buying summaries with FOMO token links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[0xcii](https://clawhub.ai/user/0xcii)

### License/Terms of Use:

MIT-0

## Use Case:

External crypto researchers and trading-analysis agents use this skill to inspect a curated FOMO smart-money wallet dataset, verify wallet activity against public chain RPC services, and summarize recent token-buying activity. Outputs should be treated as research signals, not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill performs automatic network lookups against public RPC services and DexScreener.

Mitigation: Run it only in environments where outbound access to those public services is acceptable, and review generated outputs before acting on them.

Risk: The skill outputs FOMO referral links by default and displays promotional footer content.

Mitigation: Disclose referral behavior to users and review link output before sharing or publishing results.

Risk: The skill writes a hidden marker file in the user's home directory to track promotional display state.

Mitigation: Install only where this local state file is acceptable, or remove the marker behavior before deployment.

Risk: Wallet and token summaries can be mistaken for trading recommendations.

Mitigation: Present outputs as research signals only and require independent verification before any trading decision.

## Reference(s):

- [fomo-family-frontend.md](references/fomo-family-frontend.md)
- [ClawHub skill page](https://clawhub.ai/0xcii/skills/fomo-smart-money)
- [ClawHub publisher profile](https://clawhub.ai/user/0xcii)
- [FOMO App](https://fomo.family/r/AntCaveClub)
- [DexScreener token API](https://api.dexscreener.com/latest/dex/tokens/{mint})

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown and terminal text with inline links and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include referral links and public wallet or token URLs; live checks depend on external RPC and market-data services.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
