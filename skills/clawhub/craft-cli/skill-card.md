## Description: <br>
Manage Craft documents via the craft CLI tool, supporting listing, searching, creating, updating, deleting, and exporting in JSON, table, or markdown formats. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nerveband](https://clawhub.ai/user/nerveband) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to manage Craft documents from the command line, including listing, searching, reading, creating, updating, deleting, and exporting content across configured Craft spaces. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The installer downloads a remote binary and moves it with sudo. <br>
Mitigation: Review the installer before use, prefer a user-local install path if possible, and verify the downloaded binary by checksum or signature. <br>
Risk: Craft commands can modify or delete content across configured spaces. <br>
Mitigation: Confirm the active Craft space and document ID before create, update, or delete commands; treat delete as potentially permanent unless the publisher documents recovery behavior. <br>


## Reference(s): <br>
- [Craft CLI on ClawHub](https://clawhub.ai/nerveband/skills/craft-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Text, Markdown, Configuration, Code] <br>
**Output Format:** [CLI commands and guidance; command results may be JSON, table text, Markdown, or exported files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read, create, update, delete, or export Craft documents depending on the invoked CLI command.] <br>

## Skill Version(s): <br>
1.6.2 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
