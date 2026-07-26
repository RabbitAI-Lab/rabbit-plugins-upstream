## Description: <br>
Turns conversations, project materials, meeting records, troubleshooting notes, workflows, and topic discussions into structured Obsidian knowledge-base notes with properties, summaries, reusable content blocks, references, and file links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[luojiangyong](https://clawhub.ai/user/luojiangyong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, knowledge workers, and teams use this skill to turn active work context and source materials into reusable Obsidian notes. It is suited for project archives, technical notes, decision records, reference notes, and agent workflow documentation that need traceable references and consistent metadata. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may read source materials and write or patch notes in an Obsidian vault. <br>
Mitigation: Review target paths and proposed content before writing, read back notes after writes where tooling is available, and require explicit confirmation for destructive changes. <br>
Risk: Source materials may contain secrets or sensitive credentials. <br>
Mitigation: Avoid writing API keys, cookies, tokens, auth codes, or bearer values by default unless the user explicitly requests inclusion. <br>
Risk: Summaries can become misleading if evidence boundaries are lost. <br>
Mitigation: Preserve source identity, URLs, file paths, page or section details, confidence, and Key references so readers can trace important claims. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/luojiangyong/skills/obsidian-notes-skill) <br>
- [Obsidian note template](references/note-template.md) <br>
- [Obsidian note types](references/note-types.md) <br>
- [Obsidian source types](references/source-types.md) <br>
- [Obsidian note style guide](references/style-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown notes, structured note sections, configuration snippets, shell commands, and guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write or patch Markdown notes in an Obsidian vault when an Obsidian integration is available; otherwise provides Markdown for manual insertion.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
