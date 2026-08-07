## Description:

SkillMedic audits installed AI skills by inventorying them, detecting overlap or conflicts, scoring maturity, and producing recommendations for what to keep, merge, revise, or remove.

This skill is ready for commercial/non-commercial use.

## Publisher:

[songzhou666](https://clawhub.ai/user/songzhou666)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, team maintainers, and skill ecosystem administrators use this skill to review installed AI skills, identify conflicts or duplication, compare maturity, and produce a structured inspection report before consolidating or retiring skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can audit global and hidden agent skill folders, which may expose more skill metadata than the user intended to inspect.

Mitigation: Run with an explicit workspace-only scope when home-directory or global skill metadata should remain out of scope.

Risk: The skill persists audit outputs locally under .medic, which may be committed or shared accidentally.

Mitigation: Review .medic outputs before committing or sharing the workspace and keep generated audit artifacts out of public releases unless intentionally included.

Risk: Online rubric updates may introduce network access during an audit.

Mitigation: Decline or disable online rubric updates unless network access is expected and acceptable for the audit.

## Reference(s):

- [Server-resolved GitHub repository](https://github.com/songzhou666/skill-medic)
- [ClawHub skill page](https://clawhub.ai/songzhou666/skills/skill-medic)
- [README](README.md)
- [CLI guide](references/cli-guide.md)
- [Rubric detail](references/rubric-detail.md)
- [Conflict catalog](references/conflict-catalog.md)
- [Score keys](references/score-keys.md)
- [Examples](references/examples.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown reports with structured JSON artifacts and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local .medic audit artifacts and recommendations; it does not automatically execute remediation.]

## Skill Version(s):

0.4.9 (source: SKILL.md frontmatter and CHANGELOG); ClawHub release 0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
