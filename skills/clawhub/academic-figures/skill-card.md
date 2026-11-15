## Description:

Creates publication-ready scientific figures from structured data, with statistical and journal-format options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and developers can turn structured study data into figures for analysis and paper submissions, including survival, meta-analysis, diagnostic, and multi-panel charts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan flags an unpinned Git-based MCP installation source and commands executed from example metadata; its analysis was partial.

Mitigation: Wait until the MCP source is pinned and those commands are reviewed or removed. If installing, use a restricted environment without secrets, pin dependencies, and inspect files that were only partly analyzed.

Risk: The security guidance says generated statistical figures may contain correctness defects.

Mitigation: Check the input data, statistical assumptions, and resulting figures before relying on them in a submission or decision.

Risk: Reproducibility packages may contain sensitive data.

Mitigation: Inspect package contents for sensitive information before sharing.

## Reference(s):

- [Academic Figures skill page](https://clawhub.ai/docsor1212/skills/academic-figures)
- [Project website](https://docsor.cn)

## Skill Output:

**Output Type(s):** [Static figure files, Shell commands, Configuration guidance]

**Output Format:** [PNG, TIFF, PDF, SVG, or EPS figures, with command-line and JSON/YAML examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Static figures rendered locally; output resolution can reach 600 dpi.]

## Skill Version(s):

7.9.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
