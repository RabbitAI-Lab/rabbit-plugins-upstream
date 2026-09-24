## Description:

数据分析师 helps an agent read common data sources, clean data, run statistical and time-series analysis, generate Python visualization code, and draft analysis reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Data analysts, product managers, operations staff, developers, and external agent users can use this skill to prepare datasets, generate Python analysis and visualization snippets, inspect statistical patterns, and produce Markdown-style analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad read, write, and execute capability for data-analysis workflows.

Mitigation: Use it in a sandboxed agent environment, review requested file access, and confirm command execution or file writes before they happen.

Risk: Workspace datasets may contain private, regulated, or business-sensitive information.

Mitigation: Run the skill only on data intended for analysis in that environment and avoid exposing API keys or private datasets unless the environment is properly isolated.

Risk: Generated analysis, cleaning steps, or charts can be misleading if applied to unsuitable data or unverified assumptions.

Mitigation: Review generated code and statistical conclusions against the source data and business context before using them for decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/data-analyst-cn)
- [SkillHub homepage from artifact metadata](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline Python and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated Python snippets for Pandas, Matplotlib, Seaborn, Statsmodels, data-cleaning steps, charting instructions, and report text.]

## Skill Version(s):

1.0.1 (source: server release evidence; artifact frontmatter says 1.0.25)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
