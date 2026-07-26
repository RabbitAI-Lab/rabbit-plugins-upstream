## Description: <br>
Work with Obsidian vaults as a knowledge base with fuzzy and phonetic search, auto-folder detection, note creation, note reading and editing, frontmatter, tags, and wikilinks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xiiang0529](https://clawhub.ai/user/xiiang0529) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to query, organize, create, and update Markdown notes in an Obsidian vault through agent-driven CLI workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent broad read and persistent write access to a live local notes vault. <br>
Mitigation: Review the configured vault path before installing and use the skill only with agents trusted to read and modify the vault. <br>
Risk: Replace, clear, or bulk edit operations can overwrite or remove note content. <br>
Mitigation: Keep backups or version control enabled and require explicit approval before destructive or broad edit operations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xiiang0529/skills/obsidian-direct) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON CLI outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read from and write to a configured local Obsidian vault.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
