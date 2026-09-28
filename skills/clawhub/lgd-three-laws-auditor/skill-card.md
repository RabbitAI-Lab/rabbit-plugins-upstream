## Description:

Applies the LGD three-laws rubric to assess an AI system's registration, supporting evidence, and governance gates, then suggests improvements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (code only); documentation and theoretical text: all rights reserved

## Use Case:

Developers and AI-governance teams use this skill to review an AI system against the LGD registration, evidence, and gatekeeping rubric and identify missing controls. Heuristic results are prompts for review, not compliance determinations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A self-assessment score could be mistaken for a legal or regulatory compliance finding.

Mitigation: Treat the report as a review aid and confirm conclusions against applicable requirements with qualified experts.

Risk: The skill requests WebFetch and Write access beyond its local assessment workflow.

Mitigation: Restrict unnecessary WebFetch and Write permissions where per-skill tool scoping is available.

## Reference(s):

- [LGD project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)
- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/lgd-three-laws-auditor)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Guidance]

**Output Format:** [Markdown rubric or scored report; optional JSON report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports checkpoint scores and improvement items; heuristic findings require confirmation.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata; bundled frontmatter says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
