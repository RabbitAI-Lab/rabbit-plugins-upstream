## Description:

YuanGe (元阁) provides orchestration routing, local skill inventory, and one-command installation and update workflows for the YottaMeta skill family.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to choose, install, update, inventory, and route among YottaMeta skills while keeping installation and configuration changes subject to user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation and update actions can download YottaMeta skill packages and modify local agent skill directories.

Mitigation: Review dry-run output, prefer OpenClaw's native install path when applicable, and pin the npm wrapper to an exact version for normal installs.

Risk: Inventory, hook, and update workflows can keep local state under ~/.yottaskills and scan installed skill metadata.

Mitigation: Review the selected target directories and local state location when agent separation or local data boundaries matter.

Risk: Using --range or --skip-scan weakens the normal pinned-install and scan-gate posture.

Mitigation: Avoid --range and --skip-scan unless the operator deliberately accepts that additional risk.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-skills)
- [Project homepage](https://github.com/YottaMeta/yotta-skills)
- [README](README.md)
- [Orchestration reference](references/orchestration.md)
- [Install flow reference](references/install-flow.md)
- [Skill list reference](references/skill-list.md)
- [Tutorial](references/tutorial.md)
- [FAQ](references/faq.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, JSON]

**Output Format:** [Markdown text with CLI commands and optional JSON output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are advisory by default; installation, update, and configuration writes require user confirmation or explicit command execution.]

## Skill Version(s):

0.19.15 (source: frontmatter, package.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
