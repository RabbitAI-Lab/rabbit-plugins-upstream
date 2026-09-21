## Description:

Checks Apache Doris SQL statements for syntax compatibility and specification compliance using a local tokenizer, parser, and rule engine based on Doris 3.1.4 grammar.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database engineers use this skill to review Apache Doris SQL before execution, checking syntax, Doris-specific constructs, naming conventions, object design, and common performance anti-patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Documented command examples can allow untrusted SQL to trigger local shell execution if copied into shell command strings.

Mitigation: Invoke checker scripts through direct imports, argv arrays, stdin, or securely handled files instead of interpolating untrusted SQL into shell commands.

Risk: Checker findings are advisory and may not reflect live cluster state or future cluster-backed performance checks.

Mitigation: Review results before use and require explicit read-only opt-in before enabling any live database or MCP-backed checks.

## Reference(s):

- [Doris SQL AST Node Schema](references/ast_schema.md)
- [ClawHub Skill Page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-doris-sql-check)
- [Publisher Profile](https://clawhub.ai/user/huaweicloudskill)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON report with rule IDs, severity levels, locations, snippets, and fix suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Static local analysis; no cluster connection is required for syntax and specification checks.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
