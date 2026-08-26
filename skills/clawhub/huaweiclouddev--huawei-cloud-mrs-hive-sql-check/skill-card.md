## Description:

Checks Huawei Cloud MRS Hive SQL statements against defined syntax, specification, and large-query interception rules using a local static checker.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and data engineers use this skill to statically validate Huawei Cloud MRS Hive SQL before execution and generate checker-defined findings for syntax, development standards, and resource-risk patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Checked SQL may be echoed back in generated reports, which could expose secrets embedded in SQL text.

Mitigation: Do not submit SQL containing secrets, credentials, or unrelated sensitive file contents; review generated reports before sharing them.

Risk: The skill reports only rule-defined checker findings and may omit issues outside the bundled syntax, specification, and interception rules.

Mitigation: Use the checker as a static review aid and apply separate expert review for concerns beyond the defined rule set.

## Reference(s):

- [MRS Hive SQL AST Node Schema](references/ast-schema.md)
- [Syntax Rules](rules/syntax_rules.yaml)
- [Specification Rules](rules/spec_rules.yaml)
- [Performance Rules](rules/perf_rules.yaml)
- [Keywords](rules/keywords.py)
- [Grammar Rules](rules/grammar_rules.py)
- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-mrs-hive-sql-check)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown report with summary tables, violation entries, original SQL, and optional shell commands for local checker execution]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports must only present findings emitted by the checker engine.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
