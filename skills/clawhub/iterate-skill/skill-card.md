## Description:

Automates multi-round code review and fixes with configurable review dimensions, project onboarding, and a defensive programming mode.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to review and improve code in iterative rounds, onboard project context, and apply defensive checks to coding tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repository-configured validation and invariant commands may execute shell commands.

Mitigation: Use trusted repositories and approve configured commands outside the repository before running checks.

Risk: Automated edits and git actions can affect more code than intended or publish changes.

Mitigation: Start with dry-run or review-only mode, inspect changes, and keep automatic merge and per-round push disabled.

Risk: Remote installation can run unreviewed scripts.

Mitigation: Avoid curl-to-bash installation paths.

## Reference(s):

- [Iterate on ClawHub](https://clawhub.ai/jingzhao-l/skills/iterate-skill)

## Skill Output:

**Output Type(s):** [Code, Markdown, Shell commands, Configuration]

**Output Format:** [Code changes, Markdown review summaries, and project configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce project knowledge and iteration reports.]

## Skill Version(s):

3.5.1 (source: frontmatter, pyproject.toml, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
