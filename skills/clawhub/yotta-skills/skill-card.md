## Description:

Yotta Skills coordinates the YottaMeta skill family by suggesting skill combinations, routing requests, installing selected skills, inventorying local skill directories, and adapting host hooks with user confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to select, install, update, inventory, and route YottaMeta skills for a target agent or skills directory. It provides guidance and commands for skill-family orchestration while requiring user confirmation for installation and configuration changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer can modify agent skill directories and run package-supplied lifecycle scripts.

Mitigation: Review the skill before use, trust the YottaMeta npm packages before installing, and review lifecycle scripts in packages selected for installation.

Risk: Broad install targets or skipped scans can reduce installation assurance.

Mitigation: Prefer explicit --agent or --dir targets, avoid install.sh --global and --skip-scan for normal use, and pin or mirror npm packages when higher assurance is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-skills)
- [Project homepage](https://github.com/YottaMeta/yotta-skills)
- [README](artifact/README.md)
- [Orchestration reference](artifact/references/orchestration.md)
- [Install flow reference](artifact/references/install-flow.md)
- [Skill list reference](artifact/references/skill-list.md)
- [FAQ](artifact/references/faq.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown or JSON with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or perform local skill-directory changes when the user confirms install, update, hook, or configuration actions.]

## Skill Version(s):

0.19.19 (source: evidence release, SKILL.md frontmatter, package.json, skill-manifest.json, CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
