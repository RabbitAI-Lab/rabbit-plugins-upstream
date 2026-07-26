## Description: <br>
Helps agents work with Obsidian vaults made of local Markdown notes and operate them through notesmd-cli. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, knowledge workers, and agent users can use this skill to find, create, edit, move, and delete notes in local Obsidian vaults through Markdown guidance and notesmd-cli commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to move, edit metadata for, or delete local Obsidian notes. <br>
Mitigation: Confirm exact note paths before destructive or restructuring commands, and keep backups or version control for important vaults. <br>
Risk: The skill relies on local command execution through notesmd-cli and the agent's file access. <br>
Mitigation: Use it only in vaults where local file operations are intended, and review proposed shell commands before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/obsidian-notesmd-cli) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose local note edits, vault configuration steps, and notesmd-cli commands.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
