## Description: <br>
Work with Obsidian vaults, plain Markdown notes, and obsidian-cli automation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, knowledge workers, and automation-focused agent users can use this skill to find, create, move, rename, delete, and edit Markdown notes in Obsidian vaults through Obsidian's local files and obsidian-cli. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide delete or move actions in an Obsidian vault, which may remove or reorganize notes unexpectedly if the active vault or note path is wrong. <br>
Mitigation: Confirm the active vault and exact note path before delete or move operations, and keep regular vault backups. <br>
Risk: The skill relies on read and command-line access for obsidian-cli operations. <br>
Mitigation: Install it only for agents that are allowed to inspect the target vault and run local Obsidian CLI commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/obsidian) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and note paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or execute obsidian-cli operations and direct Markdown file edits when the agent has appropriate read and exec access.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
