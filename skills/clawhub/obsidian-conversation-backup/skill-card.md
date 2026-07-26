## Description: <br>
Automatic conversation backup system for Obsidian with incremental snapshots, hourly breakdowns, and formatted chat-style markdown. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[laserducktales](https://clawhub.ai/user/laserducktales) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to back up Clawdbot conversation history into an Obsidian vault, preserving incremental and full markdown snapshots before resets or for later review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can copy full Clawdbot conversations into an Obsidian vault, which may expose sensitive chat content if the vault is shared, synced, or unencrypted. <br>
Mitigation: Use a private or encrypted vault, review what is being backed up, and avoid installing the skill when conversation archives may contain secrets that should not be persisted. <br>
Risk: The monitoring script can read a local Telegram token and send token-threshold alerts to Telegram. <br>
Mitigation: Review or disable the Telegram alert section unless external token alerts are explicitly desired, and protect any local Telegram credentials used by the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/laserducktales/skills/obsidian-conversation-backup) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Files, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown files and shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces Obsidian-formatted conversation snapshots and optional token-threshold alert behavior.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
