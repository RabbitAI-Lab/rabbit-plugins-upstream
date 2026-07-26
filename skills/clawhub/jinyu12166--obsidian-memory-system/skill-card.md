## Description: <br>
obsidian-memory-system helps AI coding agents maintain cross-session memory in a local Obsidian vault while using a remote clawtip service for order creation and paid authorization. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jinyu12166](https://clawhub.ai/user/jinyu12166) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and AI coding-agent users use this skill to preserve work logs, tasks, decisions, and project context across sessions in an Obsidian vault. It is suited for users who accept local vault reads and writes plus paid service authorization through clawtip. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The paid authorization flow sends user question text and an encrypted payment credential to api.ideaidea.com.cn. <br>
Mitigation: Install only if this data flow is acceptable, review the displayed payment notices before continuing, and avoid submitting sensitive question text during order creation. <br>
Risk: The skill requests filesystem read and write access for the configured Obsidian vault. <br>
Mitigation: Confirm the vault path before use, keep backups of important notes, and review generated memory entries before relying on them. <br>
Risk: Local order metadata and payment-related fields are stored under the OpenClaw order directory. <br>
Mitigation: Delete local order files when they are no longer needed and protect the user profile directory with normal workstation access controls. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jinyu12166/skills/obsidian-memory-system) <br>
- [Publisher profile](https://clawhub.ai/user/jinyu12166) <br>
- [clawtip verification service endpoint](https://api.ideaidea.com.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown and text guidance with shell command snippets and local Obsidian note files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a configured Obsidian vault and paid clawtip authorization; stores local order metadata under the OpenClaw order directory.] <br>

## Skill Version(s): <br>
3.0.38 (source: server release evidence; artifact frontmatter reports 3.0.33) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
