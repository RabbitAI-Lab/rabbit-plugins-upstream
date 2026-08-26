## Description:

Chat with your finances from Treeline Money. Query balances, spending, budgets, and transactions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zack-schrag](https://clawhub.ai/user/zack-schrag)

### License/Terms of Use:

MIT-0

## Use Case:

External users and personal finance agents use treeline to inspect local Treeline Money data, answer balance, spending, budget, and transaction questions, and guide imports or syncs with confirmation for write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access local financial data through the Treeline CLI.

Mitigation: Use demo mode for trials, keep financial data within the conversation, and do not share transaction descriptions or account details outside the conversation unless explicitly requested.

Risk: Write-enabled operations such as imports, syncs, restores, tagging, demo toggles, and SQL with --allow-writes can modify the local finance database.

Mitigation: Use read-only commands and dry-run previews where available, then ask for explicit user confirmation before any write action.

Risk: The security summary flags persistence of reusable finance facts without clear opt-in or retention limits.

Mitigation: Do not store financial memories unless the user explicitly approves each item and the retention boundary.

Risk: Encrypted database unlocks may involve credentials or keychain access.

Mitigation: Have the user unlock the database outside the agent conversation and do not handle credentials or unlock keys.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zack-schrag/skills/treeline-money)
- [Treeline Money](https://treeline.money)
- [Bank Sync guide](https://treeline.money/docs/integrations/bank-sync/)
- [CSV Import guide](https://treeline.money/docs/integrations/csv-import/)
- [Query cookbook](https://docs.treeline.money/ai-agents/query-cookbook/)
- [Treeline CLI macOS download](https://github.com/treeline-money/treeline/releases/latest/download/tl-macos-arm64)
- [Treeline CLI Linux download](https://github.com/treeline-money/treeline/releases/latest/download/tl-linux-x64)
- [Treeline CLI Windows download](https://github.com/treeline-money/treeline/releases/latest/download/tl-windows-x64.exe)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown chat responses with inline shell commands and JSON-oriented CLI guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses are concise and mobile-oriented; read-only commands are preferred, and write actions require user confirmation.]

## Skill Version(s):

26.8.1901 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
