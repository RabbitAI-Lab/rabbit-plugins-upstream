## Description:

SkillMedic audits installed AI skills by inventorying them, identifying duplicates or conflicts, scoring maturity, and producing keep, merge, remediate, or remove recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[songzhou666](https://clawhub.ai/user/songzhou666)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, team skill maintainers, and skill ecosystem administrators use this skill to audit installed skills, understand overlaps or conflicts, assess maturity, and decide which skills to keep, merge, remediate, or remove.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated reports may contain local skill inventory and path information.

Mitigation: Review generated reports before sharing them outside the intended audience.

Risk: Global scans can expose global skill names or paths that a user considers sensitive.

Mitigation: Use the workspace-only scan scope when global skill names or paths should not be included.

Risk: Prescription recommendations may be incomplete or context-dependent.

Mitigation: Treat keep, merge, remediate, and remove recommendations as review inputs, and confirm changes before acting on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/songzhou666/skills/skill-medic)
- [Server-resolved GitHub source](https://github.com/songzhou666/skill-medic)
- [README](artifact/README.md)
- [CLI guide](artifact/references/cli-guide.md)
- [Rubric detail](artifact/references/rubric-detail.md)
- [Conflict catalog](artifact/references/conflict-catalog.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown reports with JSON intermediate files and CLI command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write .medic inventory, scoring, conflict, prescription, and report artifacts in the project.]

## Skill Version(s):

0.1.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
