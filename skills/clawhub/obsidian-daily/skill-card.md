## Description: <br>
Manage Obsidian Daily Notes via obsidian-cli, including creating and opening daily notes, appending entries, reading notes by date, and searching vault content. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bastos](https://clawhub.ai/user/bastos) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to manage Obsidian daily notes from an agent, including journaling, task capture, links, timestamped logs, date-based reads, and vault searches. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read or search notes in the configured Obsidian vault, which may expose private note content to the agent. <br>
Mitigation: Confirm the default vault before use and avoid broad reads or searches when the vault contains notes the user does not want the agent to inspect. <br>
Risk: The skill can create or append daily-note content through obsidian-cli. <br>
Mitigation: Review create and append requests before allowing them, especially when adding journal entries, tasks, links, or timestamped logs. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands and note content examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires obsidian-cli and a configured default Obsidian vault.] <br>

## Skill Version(s): <br>
1.2.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
