## Description:

Helps agents and users assess AI systems against the LGD Three-Laws rubric for registration, evidence, and gated release controls, producing a scorecard and concrete improvement items.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and governance reviewers use this skill to structure AI governance self-assessments around the LGD Three-Laws rubric. It can print the rubric, heuristically review a system description, or generate a Markdown or JSON scorecard from human-provided answers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Published install instructions rely on unpinned remote sources that can persist agent behavior on the user's machine.

Mitigation: Pin the source to a reviewed commit or release, avoid running remote install commands unless the package source is trusted, and install only into a controlled skill directory.

Risk: Rubric-based self-assessment output may be mistaken for legal, regulatory, or professional compliance advice.

Mitigation: Use the scorecard as a self-checking aid, keep unknown or missing evidence explicit, and confirm final compliance decisions against applicable official requirements and qualified professional advice.

## Reference(s):

- [LGD Hub](https://zhaoxinghua09-cell.github.io/lgd-hub/)
- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/lgd-three-laws-auditor)

## Skill Output:

**Output Type(s):** [analysis, markdown, json, shell commands, guidance]

**Output Format:** [Markdown report, JSON scorecard, or command-line text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local-only Python standard-library script; exit codes indicate pass, findings, or usage/environment error.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata and target metadata; artifact frontmatter says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
