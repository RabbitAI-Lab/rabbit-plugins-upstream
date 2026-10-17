## Description:

Iterate helps coding assistants review, fix, and verify code across multiple rounds or apply defensive checks to incremental coding tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to review and improve code over repeated rounds, or to implement incremental changes with defensive checks and verification. A read-only mode supports review without changing files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic Git pushes can publish changes unexpectedly or use available Git credentials.

Mitigation: Remove or clarify final and session-end push instructions; leave auto_merge and push_per_round disabled unless explicitly needed.

Risk: Configured validation commands may execute untrusted or installation commands.

Mitigation: Review validation.commands before running the skill and restrict them to trusted test or build commands, not package installation.

## Reference(s):

- [Iterate on ClawHub](https://clawhub.ai/jingzhao-l/skills/iterate-skill)
- [Agent Skills specification](https://agentskills.io/)

## Skill Output:

**Output Type(s):** [Code, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Code changes and Markdown review or progress reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only review mode can report findings without modifying files.]

## Skill Version(s):

3.5.2 (source: release metadata, skill frontmatter and pyproject.toml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
