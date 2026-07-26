## Description: <br>
A notesmd-cli toolkit that helps agents manage Obsidian vaults through headless batch operations, frontmatter edits, daily note generation, and editor-based workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, knowledge workers, and agents use this skill to script Obsidian vault maintenance, including note creation, search, frontmatter updates, daily note generation, and batch archive workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Shell workflows can edit, move, delete, archive, or batch update Obsidian vault files. <br>
Mitigation: Preview target files, use dry-run where available, and keep the vault in Git or another backup system before execution. <br>
Risk: CI push workflows can publish unintended note changes. <br>
Mitigation: Review generated diffs before push and scope repository credentials to the intended workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/notes-cli-toolkit) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell, YAML, JSON, and code snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose commands that create, edit, move, delete, archive, or push note files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
