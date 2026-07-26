## Description: <br>
Generates SQL queries, explains SQL, drafts DDL, creates test data, and provides SQL quick-reference guidance from natural-language database requests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, product managers, testers, and AI agents use this skill to draft and understand SQL for routine database workflows. Generated SQL should be reviewed and dry-run before execution, especially for write or schema-changing operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated SQL may be incorrect, dialect-specific, or unsafe to execute directly. <br>
Mitigation: Review each statement, run syntax checks or EXPLAIN, and test in a dry-run or non-production environment before execution. <br>
Risk: The skill covers INSERT, UPDATE, DELETE, DROP, and migration-like workflows that could modify or destroy data. <br>
Mitigation: Use read-only credentials by default and require explicit human approval, transactions, and backups before any write or schema-changing command. <br>
Risk: Generated test data could be confused with real personal or business data. <br>
Mitigation: Use clearly synthetic values and reserved domains such as example.com, and avoid copying production data into prompts or outputs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/sql-gen-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with SQL, text examples, and command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce SQL statements, DDL, explanations, test data, and execution guidance that require human review before use.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
