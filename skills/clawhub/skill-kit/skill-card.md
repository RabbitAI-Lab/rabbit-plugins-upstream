## Description: <br>
Claude Code skill authoring and management toolkit for creating, linting, merging, upgrading, routing, discovering, and publishing skills, including trigger and dependency-graph workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drumrobot](https://clawhub.ai/user/drumrobot) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to create, validate, organize, convert, and maintain Claude Code skills and related topic documentation. It can also help compile trigger hooks, inspect skill dependencies, and prepare skills for publishing workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Trigger compilation can persistently modify Claude hook scripts and settings. <br>
Mitigation: Use dry-run or list modes first, then inspect generated ~/.claude/hooks files and ~/.claude/settings.json changes before applying them. <br>
Risk: Skill-owned scripts may run during trigger workflows with limited user control. <br>
Mitigation: Compile triggers only from trusted skills and review referenced scripts before enabling generated hooks. <br>
Risk: Merge, convert, and dedup workflows can move or replace local skill files. <br>
Mitigation: Keep backups and review selected skills and target paths before accepting cleanup or consolidation actions. <br>
Risk: Global installation flags can install skills without further confirmation. <br>
Mitigation: Avoid global non-interactive installs unless that scope and confirmation bypass are intentional. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/skill-kit) <br>
- [README](README.md) <br>
- [Trigger guide](trigger.md) <br>
- [skills.sh](https://skills.sh/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, code snippets, generated skill files, hook scripts, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or generate filesystem changes, hook scripts, and settings updates that should be reviewed before execution.] <br>

## Skill Version(s): <br>
0.6.0 (source: ClawHub release metadata and CHANGELOG, released 2026-07-28) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
