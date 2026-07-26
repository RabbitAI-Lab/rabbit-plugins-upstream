## Description: <br>
Simpleerp DB helps agents export live SimpleERP Oracle schema references and run bounded read-only SELECT, WITH, and EXPLAIN PLAN queries for tables, columns, joins, row counts, and ad-hoc reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[icystssi-lang](https://clawhub.ai/user/icystssi-lang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and database operators use this skill to inspect the SimpleERP Oracle schema, regenerate local schema references, and run read-only reporting queries when Oracle credentials are available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles live Oracle credentials and may persist them in a workspace .env file. <br>
Mitigation: Use a least-privilege read-only Oracle account, prefer short-lived environment injection or a protected secret manager, and delete any workspace .env after use. <br>
Risk: The skill can run live database queries without a separate confirmation step. <br>
Mitigation: Review SQL before execution, keep exploratory queries bounded, and avoid production or sensitive ERP data unless the operator has approved the query. <br>
Risk: Query results and generated schema files may contain business-sensitive database information. <br>
Mitigation: Store generated outputs only in the intended workspace, review artifacts before sharing, and avoid exporting row-level sensitive data outside authorized channels. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/icystssi-lang/skills/simpleerp-db) <br>
- [Publisher profile](https://clawhub.ai/user/icystssi-lang) <br>
- [Bootstrap guide](references/bootstrap.md) <br>
- [Tools reference](references/tools.md) <br>
- [Read-only database playbook](references/playbook.md) <br>
- [Table index](references/table-index.md) <br>
- [Table reference](references/table-reference.md) <br>
- [Table relationships](references/table-relationships.md) <br>
- [Journal table pattern](references/journal-pattern.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, SQL snippets, and JSON query artifacts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write generated schema references and query result files under the skill workspace.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
