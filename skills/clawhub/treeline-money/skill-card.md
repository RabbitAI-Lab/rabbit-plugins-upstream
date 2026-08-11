## Description:

Chat with your finances from Treeline Money. Query balances, spending, budgets, and transactions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zack-schrag](https://clawhub.ai/user/zack-schrag)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to inspect local Treeline Money finance data, answer questions about balances, spending, budgets, and transactions, and guide imports or sync workflows with user confirmation for changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read a local Treeline financial database that may contain sensitive account, balance, transaction, and tag information.

Mitigation: Use it only where local finance data access is expected, and do not share transaction descriptions or account details outside the conversation unless explicitly requested.

Risk: Some Treeline CLI commands can modify or import financial data when write access, sync, import, backup restore, tagging, or demo-mode changes are used.

Mitigation: Run read-only commands freely, preview imports or syncs with dry-run options when available, and ask for user confirmation before executing commands that change local data.

Risk: Saved user-created finance skills can influence future conversations and financial interpretations.

Mitigation: Only save reusable finance knowledge after the user confirms and reviews the exact skill content.

Risk: Encrypted Treeline databases require user-managed unlocking and may involve credentials or keychain access.

Mitigation: Do not attempt to unlock the database or handle credentials; ask the user to unlock it directly in the desktop app or their own terminal.

## Reference(s):

- [Treeline Money](https://treeline.money)
- [Bank Sync documentation](https://treeline.money/docs/integrations/bank-sync/)
- [CSV Import documentation](https://treeline.money/docs/integrations/csv-import/)
- [Treeline CLI for macOS](https://github.com/treeline-money/treeline/releases/latest/download/tl-macos-arm64)
- [Treeline CLI for Linux](https://github.com/treeline-money/treeline/releases/latest/download/tl-linux-x64)
- [Treeline CLI for Windows](https://github.com/treeline-money/treeline/releases/latest/download/tl-windows-x64.exe)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands, SQL examples, and concise finance summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses JSON CLI output when available and favors concise mobile/chat formatting.]

## Skill Version(s):

26.8.802 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
