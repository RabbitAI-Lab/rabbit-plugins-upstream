## Description:

Smart Charts reads user-supplied tabular files, analyzes their data characteristics with LLM assistance, and generates offline interactive ECharts HTML visualizations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[neuhanli](https://clawhub.ai/user/neuhanli)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external users use this skill to inspect user-provided CSV, TSV, text, Excel, or JSON data, choose suitable chart types, optionally transform data with pandas code, and generate self-contained HTML charts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read local tabular files, write HTML outputs, and execute LLM-generated Python transform code on local data.

Mitigation: Use it only with data intentionally provided for charting, review generated transform code when practical, and run it in an isolated environment for sensitive data.

Risk: The security verdict requires Review because the generated transform-code sandbox is not strong isolation.

Mitigation: Treat the built-in blacklist, AST whitelist, safe builtins, and timeout as guardrails rather than a containment boundary; rely on external isolation for higher-risk datasets.

## Reference(s):

- [Smart Charts Reference](references/REFERENCE.md)
- [Smart Charts ClawHub Page](https://clawhub.ai/neuhanli/skills/smart-charts)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Files]

**Output Format:** [Markdown guidance with inline shell commands and generated HTML chart files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs self-contained ECharts HTML files; successful CLI calls return JSON containing the chart status and html_path.]

## Skill Version(s):

5.1.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
