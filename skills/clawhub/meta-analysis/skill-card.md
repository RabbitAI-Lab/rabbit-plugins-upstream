## Description:

Supports systematic reviews and R-based medical meta-analysis, from literature screening and data extraction through statistical analysis, figures, and manuscript drafting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT-0

## Use Case:

Clinicians, clinical researchers, and medical statisticians use this skill to plan systematic reviews, synthesize study data, generate meta-analysis results and figures, and draft research reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote workflow responses can trigger local file uploads without sufficiently narrow file selection.

Mitigation: Review remote transfer paths before use; avoid sensitive datasets or credentials unless uploads require user-approved file allowlists, trusted destinations, and consent for each transfer.

Risk: Remote workflow responses can direct local file writes outside intended outputs.

Mitigation: Require output paths to stay within a contained, user-approved directory before using the skill.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/medstatstar/skills/meta-analysis)
- [ClawHub publisher profile](https://clawhub.ai/user/medstatstar)
- [Project homepage listed in skill metadata](https://github.com/medstatstar/meta-analysis)
- [Meta-analysis workbench](https://meta.app.workbuddy.host/)
- [Analysis reference index](references/references.md)

## Skill Output:

**Output Type(s):** [Text, Code, Files]

**Output Format:** [HTML reports with figures and tables; reproducible R code and written guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return SVG/PNG figures and CSV tables; numerical analysis requires access to the remote service.]

## Skill Version(s):

2.20.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
