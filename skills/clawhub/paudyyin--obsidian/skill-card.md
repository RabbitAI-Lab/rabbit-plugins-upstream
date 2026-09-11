## Description: <br>
Work with Obsidian vaults as plain Markdown notes and automate vault operations through notesmd-cli. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, knowledge workers, and agent operators use this skill to search, create, edit, move, and delete Markdown notes in an Obsidian vault through a local CLI workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agent actions can modify, move, or delete local Markdown notes in an Obsidian vault. <br>
Mitigation: Confirm the active vault path and exact note path before destructive or rename operations, and keep backups or version control for important vaults. <br>
Risk: CLI-level vault access can expose personal or sensitive note content to the agent workflow. <br>
Mitigation: Install and use the skill only when agent CLI access to the intended vault is acceptable. <br>


## Reference(s): <br>
- [Obsidian Help](https://help.obsidian.md) <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/obsidian) <br>
- [Publisher profile](https://clawhub.ai/user/paudyyin) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires notesmd-cli and local access to the user's Obsidian vault files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
