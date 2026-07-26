## Description: <br>
Sync files between Clawdbot workspace and Obsidian. Run the sync server to enable two-way file synchronization with the OpenClaw Obsidian plugin. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[andybold](https://clawhub.ai/user/andybold) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and Obsidian users use this skill to run a local sync server that synchronizes markdown notes between an agent workspace and an Obsidian vault through the OpenClaw Obsidian plugin. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The sync server can read and overwrite files in configured workspace folders. <br>
Mitigation: Install it only when local file synchronization is intended, narrow SYNC_ALLOWED_PATHS where possible, and keep backups or versioning for important notes. <br>
Risk: Exposing the service beyond localhost could allow access to workspace files if the token or transport is not protected. <br>
Mitigation: Keep the server bound to localhost unless deliberately exposing it through a protected channel, and use a strong unique bearer token. <br>


## Reference(s): <br>
- [ClawHub Obsidian Sync Skill](https://clawhub.ai/andybold/skills/obsidian-sync) <br>
- [obsidian-openclaw GitHub Repository](https://github.com/AndyBold/obsidian-openclaw) <br>
- [Obsidian BRAT Plugin](https://github.com/TfTHacker/obsidian42-brat) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash commands, configuration snippets, and a Node.js server script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces guidance for running and configuring a local authenticated sync service.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
