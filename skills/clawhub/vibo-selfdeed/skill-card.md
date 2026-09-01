## Description:

ViBo SelfDeed helps an agent run an explicitly approved multi-step mission by clarifying intent, restoring local ViBo memory, scanning and proposing fixes, applying confirmed changes with backups, iterating, saving lessons, and reporting results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vnbochkarev-netizen](https://clawhub.ai/user/vnbochkarev-netizen)

### License/Terms of Use:

MIT-0 registry license; ViBo EULA for product use

## Use Case:

External users and developers use this skill to delegate a concrete multi-step project task to an agent that first confirms scope, then runs a local mission loop with memory lookup, scanning, proposed fixes, backups, iteration, lesson capture, and final reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent through local file changes during autonomous missions.

Mitigation: Keep each mission scoped to a specific folder, review proposed diffs before applying fixes, and rely on backups and rollback for changed files.

Risk: `--auto` skips per-fix confirmations and can apply changes without an approval step.

Mitigation: Avoid `--auto` for production, broad, or secret-adjacent work; use the default confirmation flow for normal missions.

Risk: Optional Telegram notifications and approvals can send mission summaries or prompts to an external service.

Mitigation: Leave Telegram disabled unless external delivery is acceptable, and configure it only with an explicit mission token and chat.

Risk: Mission progress and lessons may be stored locally in mission files and ViBo memory.

Mitigation: Tell users what will be stored before starting and use the documented deletion paths for mission folders, backups, and ViBo facts.

## Reference(s):

- [ClawHub listing for ViBo SelfDeed](https://clawhub.ai/vnbochkarev-netizen/skills/vibo-selfdeed)
- [ViBo product site](https://wwwvibo.com)
- [README](README.md)
- [Installation guide](INSTALL.md)
- [End User License Agreement](EULA.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and local JSON/log mission files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local mission state, backups, and ViBo memory entries in the scoped mission workspace.]

## Skill Version(s):

1.0.13 (source: frontmatter and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
