## Description: <br>
Helps agents read and record Memory Bank project state through mb-cli for projects that use a SQLite-backed memory-bank database. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[space-cadet](https://clawhub.ai/user/space-cadet) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to inspect tasks and sessions, record work, synchronize Memory Bank database templates, and regenerate Memory Bank Markdown from a SQLite backend. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad activation language and inconsistent approval rules could cause persistent Memory Bank state changes without clear user intent. <br>
Mitigation: Install only in repositories that intentionally use mb-cli with memory-bank/database, narrow activation language, and require explicit user approval before mb commands that create, update, delete, sync, or regenerate files. <br>
Risk: The workflow records chronological project state but does not fully maintain the knowledge layer. <br>
Mitigation: Review and manually update architecture, product context, technical context, and implementation details after recording or regenerating Memory Bank state. <br>


## Reference(s): <br>
- [Memory Bank Database API Reference](references/api-reference.md) <br>
- [SQLite Schema](references/schema.sql) <br>
- [Integrated Rules v6.12](references/integrated-rules-v6.12.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands target local mb-cli projects that intentionally use memory-bank/database.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
