## Description:

Chat with your finances from Treeline Money. Query balances, spending, budgets, and transactions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zack-schrag](https://clawhub.ai/user/zack-schrag)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to answer personal-finance questions from a local Treeline Money database, including balances, spending, budgets, transactions, imports, backups, and health checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose sensitive local financial summaries and transaction data to the agent during normal use.

Mitigation: Use it only with Treeline Money data you intend the agent to read, keep responses concise, and do not share transaction descriptions or account details outside the conversation unless explicitly requested.

Risk: Sync, import, backup restore, tag, compact, demo toggle, and write-enabled SQL actions can change local financial data or database state.

Mitigation: Confirm those actions with the user first, prefer dry-run or read-only commands when available, and run SQL without write access unless writes are explicitly approved.

Risk: Encrypted databases require a local unlock step that could involve credentials or keychain access.

Mitigation: Have the user unlock the database outside the chat through the desktop app or their own terminal, and do not ask the agent to handle credentials.

## Reference(s):

- [Treeline Money](https://treeline.money)
- [Treeline Bank Sync documentation](https://treeline.money/docs/integrations/bank-sync/)
- [Treeline CSV Import documentation](https://treeline.money/docs/integrations/csv-import/)
- [Treeline AI Agents Query Cookbook](https://docs.treeline.money/ai-agents/query-cookbook/)
- [Treeline CLI macOS download](https://github.com/treeline-money/treeline/releases/latest/download/tl-macos-arm64)
- [Treeline CLI Linux download](https://github.com/treeline-money/treeline/releases/latest/download/tl-linux-x64)
- [Treeline CLI Windows download](https://github.com/treeline-money/treeline/releases/latest/download/tl-windows-x64.exe)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, guidance]

**Output Format:** [Markdown with concise text, bullet lists, SQL snippets, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses JSON CLI output when available and favors mobile-readable summaries over tables.]

## Skill Version(s):

26.8.1401 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
