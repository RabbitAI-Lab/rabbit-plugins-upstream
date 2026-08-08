## Description: <br>
Checks Huawei Cloud DWS SQL statements for syntax validity, DWS-specific compatibility, and development specification issues using a local tokenizer, parser, and rule engine. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and data engineers use this skill to review DWS SQL before execution, catch syntax and compatibility issues, and identify specification or performance anti-patterns in SQL statements. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: SQL text from untrusted sources may contain shell metacharacters if pasted directly into a command line. <br>
Mitigation: Pass untrusted SQL through a safely quoted argument or a temporary file before invoking the checker. <br>
Risk: Static checks skip rules that require a live DWS cluster, such as index count, non-pushdown SQL, and view dependency analysis. <br>
Mitigation: Treat static results as pre-execution review and run cluster-dependent checks separately when those findings are needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-dws-sql-check) <br>
- [AST Schema](references/ast_schema.md) <br>
- [Syntax Rules](rules/syntax_rules.yaml) <br>
- [Specification Rules](rules/spec_rules.yaml) <br>
- [Performance Rules](rules/perf_rules.yaml) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown reports, JSON check results, and concise command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Static syntax and specification checks run locally; cluster-dependent performance rules are documented but skipped in static mode.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
