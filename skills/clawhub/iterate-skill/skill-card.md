## Description:

Guides coding assistants through multi-round code review and repair, defensive incremental coding, project onboarding, and cross-assistant installation and updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use Iterate to review and improve code across configurable quality dimensions, or to complete incremental coding tasks with defensive checks. It guides assistants through fixes, validation, and convergence reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates this release suspicious with medium confidence, citing installation and update paths, credential handling, and activity beyond the stated scope; its analysis was partial.

Mitigation: Have the installer, update paths, credential handling, and publishing instructions independently reviewed. If installing, use a restricted environment without valuable credentials and review overwrite and network activity.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/jingzhao-l/skills/iterate-skill)
- [Agent Skills specification](https://agentskills.io/)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Markdown reports]

**Output Format:** [Code changes, shell commands, configuration guidance, and Markdown review summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May repeat review, repair, and validation rounds until findings converge or the configured round limit is reached.]

## Skill Version(s):

3.14.0 (source: frontmatter, pyproject.toml, CHANGELOG, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
