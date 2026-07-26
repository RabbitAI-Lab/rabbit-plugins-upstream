## Description: <br>
Records, imports, queries, and manages a user's Orchune personal-finance ledger through the Orchune MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[orchune](https://clawhub.ai/user/orchune) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and their agents use this skill to connect to Orchune, authenticate with an access token, record expenses, income, transfers, categories, accounts, imports, budgets, goals, and investment activity in the user's Orchune ledger. It is not for general financial advice, tax preparation, or unrelated spreadsheet analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill routes sensitive bookkeeping, account, and investment details through Orchune. <br>
Mitigation: Install only when the user wants Orchune to handle this data, and confirm before sending statement imports, account details, or investment records. <br>
Risk: The Orchune access token provides long-lived account access. <br>
Mitigation: Store the token only in a secure environment variable or MCP client secret mechanism, never in conversation text, files, logs, or tool arguments. <br>
Risk: Some operations can delete records, merge categories irreversibly, overwrite fund returns, or commit statement imports that cannot be reverted by MCP. <br>
Mitigation: Ask for explicit user confirmation before destructive or irreversible actions, preview imports before commit, and report when reversal requires the web app. <br>
Risk: Incorrect amount, date, currency, or name resolution can create inaccurate financial records. <br>
Mitigation: Follow the artifact conventions for positive major-unit inputs, minor-unit string outputs, account currency, timezone handling, and retry ambiguous names with resolved IDs. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/orchune/skills/personal-finance) <br>
- [First-time setup](artifact/references/setup.md) <br>
- [Orchune MCP tool reference](artifact/references/tools.md) <br>
- [Statement import workflow](artifact/references/bill-import.md) <br>
- [Orchune MCP endpoint](https://www.orchune.com/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with MCP configuration values, tool-call plans, and concise user-facing summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or execute MCP calls that read or modify bookkeeping records when an authenticated Orchune MCP server is available.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
