## Description:

Smart Charts turns CSV, TSV, TXT, Excel, or JSON data files into standalone offline ECharts HTML visualizations with traceable plot statistics and data previews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[neuhanli](https://clawhub.ai/user/neuhanli)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to generate offline interactive HTML charts from tabular data and include traceable caption facts without building a backend dashboard.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Model-written transform code may have more local execution power than users expect.

Mitigation: Run the skill in an isolated environment, review or disable transform-code use for untrusted inputs, and avoid processing untrusted transform code on machines with sensitive files or credentials.

Risk: Generated HTML may carry misleading or unsafe content if published under a trusted site origin without review.

Mitigation: Inspect generated HTML and its embedded chart facts before publishing or sharing it from a trusted origin.

Risk: Dependency drift or crafted GeoJSON filenames may increase operational risk.

Mitigation: Prefer a locked dependency set and process custom GeoJSON only in a constrained working directory.

## Reference(s):

- [Smart Charts reference](artifact/references/REFERENCE.md)
- [ClawHub skill page](https://clawhub.ai/neuhanli/skills/smart-charts)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Files, Markdown, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON stdout; generated artifacts are standalone HTML files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated HTML is self-contained for offline rendering and includes plot statistics plus data previews for traceable captions.]

## Skill Version(s):

8.3.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
