## Description:

Git工具包专业版 helps developers and engineering teams manage Git repositories with batch branch operations, automated review guidance, Git hook setup, commit policy checks, repository history analysis, and CI/CD integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to standardize Git workflows, automate branch cleanup and review checks, configure Git hooks, and integrate repository checks into CI/CD pipelines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential exposure from plaintext credential helper or token-in-URL examples.

Mitigation: Use SSH, an OS-backed credential manager, or a scoped secret mechanism; do not place tokens in remote URLs.

Risk: Destructive branch cleanup commands can delete local branches without enough safeguards.

Mitigation: List candidate branches before deletion, protect main, master, and develop branches, and require explicit confirmation before cleanup removes branches.

Risk: Git hooks, aliases, and remote configuration changes can alter repository behavior for a team.

Mitigation: Review proposed changes with repository maintainers and apply them only in repositories where those workflow changes are intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/git-toolkit)
- [Publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash, YAML, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Git commands and configuration changes that should be reviewed before execution.]

## Skill Version(s):

1.0.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
