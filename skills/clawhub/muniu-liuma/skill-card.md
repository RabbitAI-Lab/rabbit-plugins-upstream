## Description:

MuniuLiuma is an SDD quality workflow bundle that helps agents choose and apply five step skills for specification writing, architecture design, task planning, implementation guidance, and delivery auditing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[timeaground](https://clawhub.ai/user/timeaground)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this bundle to select the appropriate SDD step skill, convert requirements into structured specs and downstream planning artifacts, generate implementation guidance and test skeletons, and audit delivery evidence against the planned work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some sub-skills inspect project code, configuration, architecture documents, and test result files during brownfield planning or audits.

Mitigation: Use the bundle only in workspaces where that review is intended and avoid providing unrelated project material.

Risk: Generated plans, implementation guidance, test skeletons, and audit judgments can be incomplete or incorrect.

Mitigation: Review generated artifacts and run project tests before relying on them for delivery decisions.

## Reference(s):

- [MuniuLiuma ClawHub release](https://clawhub.ai/timeaground/skills/muniu-liuma)
- [Publisher profile](https://clawhub.ai/user/timeaground)
- [TEST-SKELETON-SPEC.md](artifact/TEST-SKELETON-SPEC.md)
- [MuniuLiuma overview skill](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance]

**Output Format:** [Markdown with structured tables and code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces staged SDD artifacts such as specs, architecture plans, task lists, implementation guidance, executable test skeletons, audit reports, and installation or distribution guidance.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
