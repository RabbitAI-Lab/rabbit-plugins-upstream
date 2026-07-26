## Description: <br>
BrainRepo helps an agent capture, organize, and retrieve a local Markdown personal knowledge repository using PARA and Zettelkasten conventions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[codezz](https://clawhub.ai/user/codezz) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to maintain an agent-managed Markdown knowledge base for notes, projects, people, resources, tasks, and review workflows. It is suited to local personal knowledge management with Obsidian, VS Code, or any editor that reads Markdown. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Captured notes may include secrets or unnecessary sensitive personal details. <br>
Mitigation: Review captures before saving and avoid storing credentials, private keys, or unnecessary sensitive personal information. <br>
Risk: Agent-managed cleanup or review workflows may delete or move local knowledge-base files unexpectedly. <br>
Mitigation: Confirm deletes, archive moves, and cleanup actions before execution, and keep git history or backups for recovery. <br>
Risk: Git sync commands may push private notes to the wrong remote. <br>
Mitigation: Verify that any configured Git remote is private and correct before allowing git push. <br>


## Reference(s): <br>
- [BrainRepo Structure Guide](references/structure.md) <br>
- [BrainRepo Workflows](references/workflows.md) <br>
- [BrainRepo Templates](assets/templates/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown files and concise guidance, with shell commands when setting up or syncing the repository] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes local Markdown under ~/Documents/brainrepo/ and may use git when the user permits repository initialization or syncing.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata, created 2026-02-04) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
