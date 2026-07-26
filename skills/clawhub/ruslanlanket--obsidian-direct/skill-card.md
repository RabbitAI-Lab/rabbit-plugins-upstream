## Description: <br>
Work with Obsidian vaults as a knowledge base, including fuzzy and phonetic search across notes, auto-folder detection for new notes, note creation, note reading, note editing with frontmatter, tag management, and wikilink management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruslanlanket](https://clawhub.ai/user/ruslanlanket) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users use this skill to let an agent query an Obsidian vault, answer from retrieved notes, create new Markdown notes, and update existing notes by prompt. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read local Obsidian notes, which may expose private or sensitive vault content to an agent workflow. <br>
Mitigation: Install it only for vaults the agent is allowed to access and configure the vault path deliberately before use. <br>
Risk: The skill can overwrite, clear, or replace sections in existing Markdown notes. <br>
Mitigation: Keep backups or version history enabled and require review or confirmation before destructive edit actions such as replace, clear, or replace-section. <br>
Risk: The skill can create notes in caller-supplied or automatically selected folders, which may place content in an unexpected part of the vault. <br>
Mitigation: Review the target folder and title before note creation, especially when using caller-provided folders or auto-folder behavior. <br>


## Reference(s): <br>
- [ClawHub Skill Listing](https://clawhub.ai/ruslanlanket/skills/obsidian-direct) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown responses, JSON CLI results, and Markdown note files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read, create, append, replace, clear, or section-replace Markdown notes in the configured Obsidian vault.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
