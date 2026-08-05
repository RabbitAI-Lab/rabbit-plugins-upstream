## Description: <br>
Checks Huawei Cloud MRS Hive SQL statements against defined syntax, specification, and large-query interception rules using a local automated checker engine. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and data engineers use this skill to validate Huawei Cloud MRS Hive SQL before execution and to produce checker-based reports for syntax, specification, and large-query risk findings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: SQL text or explicitly provided SQL files may contain sensitive query content that appears in checker output. <br>
Mitigation: Only pass intended SQL inputs, avoid sensitive non-SQL files, and review generated reports before sharing them. <br>
Risk: The skill reports only violations detected by its defined checker rules and may not cover issues outside that rule set. <br>
Mitigation: Use the report as static rule-checking guidance and apply separate review for business logic, data access, and runtime behavior. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-mrs-hive-sql-check) <br>
- [MRS Hive SQL AST Node Schema](references/ast-schema.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown report or JSON checker output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports are generated from the local checker output and include rule IDs, severity, location, description, SQL snippets, and fix suggestions when detected.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
