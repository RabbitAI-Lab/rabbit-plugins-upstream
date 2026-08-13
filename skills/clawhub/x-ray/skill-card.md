## Description:

X-ray scans an unfamiliar software project to identify its project type, technology stack, architecture, file structure, complexity, learning fit, and recommended reading order.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ppshux](https://clawhub.ai/user/ppshux)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use X-ray to quickly understand, inspect, or take over an unfamiliar codebase through static project analysis and a generated local report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill inspects project contents and file names in the directory where it is run.

Mitigation: Run it only from the intended repository root and avoid directories that contain secrets or unrelated private material.

Risk: The skill creates local report files during analysis.

Mitigation: Review generated xray-data.json and xray-report.html before sharing or committing them.

## Reference(s):

- [X-ray Skill Page](https://clawhub.ai/ppshux/skills/x-ray)
- [analysis-rules.md](references/analysis-rules.md)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance, configuration]

**Output Format:** [JSON scan data and a standalone HTML report with explanatory text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates local xray-data.json and xray-report.html files from static analysis.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
