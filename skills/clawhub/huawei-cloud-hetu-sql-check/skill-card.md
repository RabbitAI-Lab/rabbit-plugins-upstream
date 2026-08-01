## Description: <br>
Comprehensive SQL statement checking for HetuEngine, covering syntax validation, statement structure checks, HetuEngine compatibility, and specification checks for object design, data operations, and naming conventions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and data engineers use this skill to review HetuEngine SQL before execution, identify syntax or compatibility problems, and receive specification findings with fix suggestions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs local Python scripts and can read a SQL file path supplied by the user. <br>
Mitigation: Only pass SQL text or files intended for local analysis, and review generated findings before applying changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-hetu-sql-check) <br>
- [AST Schema](references/ast_schema.md) <br>
- [Syntax Rules](rules/syntax_rules.yaml) <br>
- [Specification Rules](rules/spec_rules.yaml) <br>
- [Report Template](templates/report_template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON check reports with rule IDs, severity, locations, descriptions, snippets, and fix suggestions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local static analysis for SQL text or user-provided SQL files; no database cluster connection is required.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
