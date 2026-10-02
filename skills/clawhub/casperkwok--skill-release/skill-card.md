## Description:

Publish and manage Claude Code skills on ClawHub (clawhub.ai).

This skill is ready for commercial/non-commercial use.

## Publisher:

[casperkwok](https://clawhub.ai/user/casperkwok)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to check ClawHub readiness, publish new Claude Code skills, update released versions, and generate release changelogs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing or updating the wrong skill directory could release unintended content to ClawHub.

Mitigation: Run check or dry-run first, confirm the target directory and ClawHub account, and review any generated changelog before publishing.

Risk: The publish workflow may modify SKILL.md version metadata before releasing.

Mitigation: Review the SKILL.md version change before publishing or committing the artifact.

Risk: Installing an unpinned global ClawHub CLI can change publish behavior over time.

Mitigation: Use a reviewed pinned ClawHub CLI version for controlled environments.

## Reference(s):

- [Skill Release on ClawHub](https://clawhub.ai/casperkwok/skills/skill-release)
- [ClawHub](https://clawhub.ai)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown, code]

**Output Format:** [Markdown with inline shell commands and status messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update SKILL.md version metadata and produce changelog text during publish workflows.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
