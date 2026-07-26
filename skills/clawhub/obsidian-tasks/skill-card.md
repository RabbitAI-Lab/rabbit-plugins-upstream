## Description: <br>
Set up and manage an Obsidian task board with Kanban columns, Dataview dashboards, structured task notes, synchronized board/frontmatter updates, and wikilinks to supporting notes or research. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[larsderidder](https://clawhub.ai/user/larsderidder) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to let an agent initialize and maintain a local Obsidian task board with Kanban columns, Dataview dashboards, structured task notes, and wikilinked supporting notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup workflow creates or updates files in a user-specified Obsidian vault, so an incorrect path or unreviewed edits could affect important notes. <br>
Mitigation: Provide the exact vault path, keep normal Obsidian backup or sync history available, and review generated board and task changes before relying on them. <br>
Risk: The artifact includes a maintainer publish script that is not needed for normal task-board use. <br>
Mitigation: Ignore the publish script unless maintaining and publishing the skill release; normal users should use the setup workflow for their vault. <br>


## Reference(s): <br>
- [Obsidian](https://obsidian.md) <br>
- [Obsidian Kanban plugin](https://github.com/mgmeyers/obsidian-kanban) <br>
- [Obsidian Dataview plugin](https://github.com/blacksmithgu/obsidian-dataview) <br>
- [ClawHub skill page](https://clawhub.ai/larsderidder/skills/obsidian-tasks) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and generated Markdown files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local Obsidian Board.md and Dashboard.md files when the setup script is run against a user-provided vault path.] <br>

## Skill Version(s): <br>
0.1.2 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
