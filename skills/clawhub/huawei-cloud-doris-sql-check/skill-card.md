## Description: <br>
Checks Apache Doris SQL syntax and specification compliance using a local tokenizer, parser, and rule engine. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and data engineers use this skill to review Apache Doris SQL before execution, including syntax validation, Doris-specific construct checks, naming and object-design rules, and specification guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: SQL submitted for review can contain sensitive schema, object names, or business logic even when processed locally. <br>
Mitigation: Only provide SQL text that is appropriate for local analysis in the agent environment; the release security evidence states that this skill does not send SQL externally. <br>
Risk: Cluster-dependent checks are not performed by the static local workflow. <br>
Mitigation: Treat view-depth, index-count, non-pushdown, and performance findings as out of scope unless a future workflow receives separate approval and scoped credentials for cluster access. <br>
Risk: The parser is based on Apache Doris 3.1.4 grammar and may not cover every syntax difference in newer Doris versions. <br>
Mitigation: Verify important findings against the target Doris cluster version before using the report as a deployment gate. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-doris-sql-check) <br>
- [AST Schema](artifact/references/ast_schema.md) <br>
- [Syntax Rules](artifact/rules/syntax_rules.yaml) <br>
- [Specification Rules](artifact/rules/spec_rules.yaml) <br>
- [Performance Rules](artifact/rules/perf_rules.yaml) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown report or JSON result with rule violations, severity, location, SQL snippets, and fix suggestions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Static checks run locally; cluster-dependent performance checks are defined but skipped unless a future workflow adds approved cluster access.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
