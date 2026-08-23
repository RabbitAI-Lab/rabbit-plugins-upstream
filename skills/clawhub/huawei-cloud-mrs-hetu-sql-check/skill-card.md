## Description:

Checks HetuEngine SQL for syntax compatibility and specification compliance using a local tokenizer, parser, rule engine, and report generator.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and data engineers use this skill to validate HetuEngine SQL syntax, review SQL against development best practices, and identify specification or performance issues before running statements on a cluster.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SQL text or local file contents provided for checking may be reflected in generated reports.

Mitigation: Provide only SQL text or file paths intended for local review, and review generated reports before sharing them.

Risk: Static SQL analysis can miss cluster-dependent behavior; artifact notes say rules marked requires_cluster, such as SPEC030, are skipped in static mode.

Mitigation: Use this skill as a pre-execution review aid and validate cluster-dependent findings in the target HetuEngine environment.

## Reference(s):

- [AST Schema](references/ast_schema.md)
- [Syntax Rules](rules/syntax_rules.yaml)
- [Specification Rules](rules/spec_rules.yaml)
- [Keywords](rules/keywords.py)
- [Grammar Rules](rules/grammar_rules.py)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown report with syntax and specification findings; the checker command can also return JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Inputs are SQL text or local file paths plus an optional check mode: syntax, spec, or all.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
