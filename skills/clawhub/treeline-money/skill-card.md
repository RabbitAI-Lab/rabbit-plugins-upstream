## Description:

Chat with your finances from Treeline Money. Query balances, spending, budgets, and transactions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zack-schrag](https://clawhub.ai/user/zack-schrag)

### License/Terms of Use:

MIT-0

## Use Case:

External users and finance-focused agents use this skill to answer questions about local Treeline Money balances, spending, budgets, transactions, backups, and imports. It helps agents run Treeline CLI queries and turn local finance results into concise chat responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help an agent query sensitive local financial data.

Mitigation: Use read-only Treeline commands for routine questions, keep financial details inside the conversation, and avoid sharing transaction or account details unless the user explicitly asks.

Risk: Write, sync, import, restore, tag, and skill-saving actions can change local financial data or persist personal finance details.

Mitigation: Require user confirmation before those actions, prefer dry-run previews for imports and syncs, and review saved skill contents before allowing personal finance details to persist.

Risk: Encrypted databases require user-controlled unlock flows.

Mitigation: Do not handle credentials or attempt to unlock the database; ask the user to unlock Treeline directly in the desktop app or their own terminal.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zack-schrag/skills/treeline-money)
- [Treeline Money Homepage](https://treeline.money)
- [Treeline Bank Sync Setup Guide](https://treeline.money/docs/integrations/bank-sync/)
- [Treeline CSV Import Setup Guide](https://treeline.money/docs/integrations/csv-import/)
- [Treeline CLI Download for macOS](https://github.com/treeline-money/treeline/releases/latest/download/tl-macos-arm64)
- [Treeline CLI Download for Linux](https://github.com/treeline-money/treeline/releases/latest/download/tl-linux-x64)
- [Treeline CLI Download for Windows](https://github.com/treeline-money/treeline/releases/latest/download/tl-windows-x64.exe)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Concise chat Markdown with bullet lists, inline shell commands, SQL snippets, and JSON-aware command handling]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prefers rounded amounts, no markdown tables, and user confirmation before write, sync, import, restore, tag, or skill-saving actions.]

## Skill Version(s):

26.8.1203 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
