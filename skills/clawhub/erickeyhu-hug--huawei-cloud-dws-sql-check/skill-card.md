## Description: <br>
Checks Huawei Cloud DWS SQL statements for syntax, DWS-specific grammar compatibility, specification compliance, naming standards, and common performance anti-patterns using a local tokenizer, parser, and rule engine. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and data engineers use this skill to review Huawei Cloud DWS SQL before execution, validate syntax and DWS-specific constructs, and generate rule-based findings for specification compliance and common performance concerns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Static findings may be incomplete for rules that require live DWS cluster metadata or execution plans. <br>
Mitigation: Use offline syntax and specification checks by default; run cluster-dependent performance review only as a separate opt-in action with read-only, least-privilege database access. <br>
Risk: Rule-based SQL guidance may produce false positives or false negatives for project-specific DWS standards. <br>
Mitigation: Have a DWS-aware reviewer validate reported violations and suggestions before applying SQL changes. <br>


## Reference(s): <br>
- [AST Schema](references/ast_schema.md) <br>
- [Syntax Rules](rules/syntax_rules.yaml) <br>
- [Specification Rules](rules/spec_rules.yaml) <br>
- [Performance Rules](rules/perf_rules.yaml) <br>
- [DWS SQL Keywords](rules/keywords.py) <br>
- [DWS Grammar Rules](rules/grammar_rules.py) <br>
- [ClawHub Skill Page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-dws-sql-check) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown report or JSON command output with rule IDs, severity, locations, descriptions, snippets, and fix suggestions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs locally with Python 3.8+ and standard library dependencies for syntax and specification checks.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
