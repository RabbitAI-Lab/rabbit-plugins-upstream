## Description:

Fully automated multi-round code iteration with configurable N-dimension parallel review, onboarding/personalization, and a cross-assistant installer/update system with mandatory SHA256 checksum verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use Iterate to run structured, multi-round code review and repair passes across a project, with onboarding-generated project context, configurable quality dimensions, validation commands, and optional review-only operation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Autonomous git behavior could lead to unintended merge or push actions if publication settings are enabled or conflicting instructions are followed.

Mitigation: Keep git.auto_merge and git.push_per_round disabled unless publication is explicitly intended, review branch diffs before merging, and use review-only or dry-run mode for audit-only use.

Risk: Configured validation commands and installer paths can execute local commands during review, onboarding, or installation.

Mitigation: Review validation.commands and command whitelist entries before running the skill, prefer --no-cli when only the assistant skill is needed, avoid curl-to-shell installation paths, and do not pass GitHub tokens on shared command lines.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jingzhao-l/skills/iterate-skill)
- [README.md](README.md)
- [SKILL.md](SKILL.md)
- [npm installer package](https://www.npmjs.com/package/iterate-skill-installer)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown reports and agent actions with optional code edits, shell commands, and configuration file updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can operate in review-only mode or perform file and git actions according to configured approvals and validation settings.]

## Skill Version(s):

2.9.0 (source: frontmatter and pyproject.toml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
