## Description:

Guides an agent in using the OKX Outcomes CLI for YES/NO event-contract market discovery, account review, setup, authenticated reads, and explicitly confirmed trading or settlement actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to browse OKX Outcomes YES/NO event markets, inspect balances and positions, complete setup, and prepare trading, order-management, split, merge, or redeem workflows. The skill is intended to keep write operations behind dry-run previews and explicit user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is flagged as suspicious because it recommends piping an unverified remote installer directly into a shell in a high-impact trading environment.

Mitigation: Prefer a pinned release, checksum or signature verification, and manual inspection before installing or running the OKX Outcomes binary.

Risk: The skill can guide authenticated account reads and trading-related write operations, including order placement, cancellation, split, merge, and redeem actions.

Mitigation: Require a dry-run summary with market, asset, notional, wallet, and available balance details, then execute only after the user replies with the exact confirmation token.

Risk: The setup stores OKX OAuth or session material and a signing-wallet key locally.

Mitigation: Use only environments where local credential storage is acceptable, rely on the keyring or encrypted fallback, and never request, print, or paste signing private keys in chat.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/searchworld/skills/okx-outcomes)
- [OKX homepage](https://www.okx.com)
- [Setup and Authentication](references/setup-auth.md)
- [Cross-Command Workflows](references/workflows.md)
- [Data Commands](references/data-commands.md)
- [Account Commands](references/account-commands.md)
- [CLOB Commands](references/clob-commands.md)
- [CTF Commands](references/ctf-commands.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-oriented command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write operations require a dry-run preview and an explicit user confirmation before execution.]

## Skill Version(s):

1.4.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
