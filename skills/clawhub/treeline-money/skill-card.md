## Description:

Chat with your finances from Treeline Money. Query balances, spending, budgets, and transactions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zack-schrag](https://clawhub.ai/user/zack-schrag)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to inspect local Treeline Money data, answer personal finance questions, and guide safe setup, sync, import, backup, and query workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can query sensitive local financial data, including accounts, balances, budgets, and transaction details.

Mitigation: Only use it when the user wants an agent to inspect their Treeline database, keep financial details within the conversation unless explicitly asked, and avoid sharing account or transaction details externally.

Risk: Write, sync, import, restore, demo-toggle, and profile-saving actions can modify local financial data or local skill files.

Mitigation: Run read-only commands freely, use dry-run previews where available, and ask for clear user confirmation before actions that change data or save preferences.

Risk: Encrypted databases require unlocking, and credential handling would expose sensitive secrets.

Mitigation: Do not attempt to unlock encrypted databases or handle credentials; instruct the user to unlock Treeline directly in their own terminal or desktop app.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zack-schrag/skills/treeline-money)
- [Treeline Money](https://treeline.money)
- [Treeline desktop download](https://treeline.money/download)
- [Bank Sync guide](https://treeline.money/docs/integrations/bank-sync/)
- [CSV Import guide](https://treeline.money/docs/integrations/csv-import/)
- [Treeline CLI macOS download](https://github.com/treeline-money/treeline/releases/latest/download/tl-macos-arm64)
- [Treeline CLI Linux download](https://github.com/treeline-money/treeline/releases/latest/download/tl-linux-x64)
- [Treeline CLI Windows download](https://github.com/treeline-money/treeline/releases/latest/download/tl-windows-x64.exe)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with inline SQL and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses JSON-formatted CLI output when running Treeline commands and favors concise mobile/chat responses.]

## Skill Version(s):

26.8.1202 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
