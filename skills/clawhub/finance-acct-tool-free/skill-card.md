## Description: <br>
A finance and accounting starter skill for personal users and small businesses that guides bookkeeping, bank reconciliation, basic tax calculations, and standard financial report generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Personal users, freelancers, independent developers, and small businesses use this skill to guide local finance workflows including bookkeeping, bank reconciliation, basic VAT and income-tax calculations, and financial statement generation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests local write and command-execution ability for sensitive accounting workflows. <br>
Mitigation: Review commands and file changes before execution, especially for imports, records, reconciliations, and generated reports. <br>
Risk: Callback URLs could send financial results outside the local environment. <br>
Mitigation: Avoid using callback_url with real financial data unless the destination and data handling are fully understood. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/finance-acct-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code, markdown] <br>
**Output Format:** [Markdown guidance with bash, YAML, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose local file creation and command execution for SQLite-backed finance workflows.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release evidence; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
