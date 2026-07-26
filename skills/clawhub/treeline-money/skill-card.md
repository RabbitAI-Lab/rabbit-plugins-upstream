## Description: <br>
Chat with your finances from Treeline Money. Query balances, spending, budgets, and transactions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zack-schrag](https://clawhub.ai/user/zack-schrag) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to inspect local Treeline Money finance data, answer questions about balances, spending, budgets, and transactions, and guide imports or sync workflows with user confirmation for data-changing actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read a user's local finance database through the Treeline CLI. <br>
Mitigation: Install only if the user is comfortable with that access, and avoid sharing account or transaction details outside the conversation unless explicitly requested. <br>
Risk: Sync, import, restore, tagging, demo-mode changes, write-enabled SQL, and saved user skills can change local data or persist finance-related context. <br>
Mitigation: Require explicit user approval before those actions and use dry-run or read-only previews where available. <br>
Risk: Reusable skill files can preserve sensitive finance details or secrets. <br>
Mitigation: Avoid saving secrets or overly sensitive details in reusable skill files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zack-schrag/skills/treeline-money) <br>
- [Treeline Money](https://treeline.money) <br>
- [Bank Sync documentation](https://treeline.money/docs/integrations/bank-sync/) <br>
- [CSV Import documentation](https://treeline.money/docs/integrations/csv-import/) <br>
- [Treeline CLI download for macOS](https://github.com/treeline-money/treeline/releases/latest/download/tl-macos-arm64) <br>
- [Treeline CLI download for Linux](https://github.com/treeline-money/treeline/releases/latest/download/tl-linux-x64) <br>
- [Treeline CLI download for Windows](https://github.com/treeline-money/treeline/releases/latest/download/tl-windows-x64.exe) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, SQL examples, and JSON-oriented CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the Treeline CLI (`tl`) with local finance data; read-only commands may run autonomously while write actions require explicit user confirmation.] <br>

## Skill Version(s): <br>
26.7.201 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
