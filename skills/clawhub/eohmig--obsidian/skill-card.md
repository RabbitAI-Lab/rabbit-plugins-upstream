## Description: <br>
Work with Obsidian vaults (plain Markdown notes) and automate via obsidian-cli. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[eohmig](https://clawhub.ai/user/eohmig) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and note-taking users can use this skill to locate Obsidian vaults, search Markdown notes, create notes, and manage note paths through obsidian-cli. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Move, edit, or delete operations can alter or remove local notes in an Obsidian vault. <br>
Mitigation: Review any file-changing command before it runs, confirm the selected vault, and keep backups or version control for important notes. <br>
Risk: Multiple configured vaults can cause commands to affect the wrong note collection if the active or default vault is assumed. <br>
Mitigation: Resolve the active vault from Obsidian configuration or obsidian-cli print-default before creating, moving, or deleting notes. <br>


## Reference(s): <br>
- [Obsidian Help](https://help.obsidian.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands target local Obsidian vaults through obsidian-cli and direct Markdown file edits.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
