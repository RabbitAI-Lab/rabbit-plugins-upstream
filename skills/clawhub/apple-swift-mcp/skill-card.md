## Description: <br>
This skill helps an agent work with Apple app data through a native Swift MCP for Calendar, Reminders, Contacts, Maps, Mail, Messages, Notes, and Photos on macOS. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent query and automate macOS Apple apps, including calendars, reminders, contacts, mail, messages, notes, maps, and photos. It is most relevant for Apple Silicon Macs running macOS 14 or later. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The native MCP can access sensitive local Apple app data, including Mail, Messages, Photos, Notes, Calendar, Reminders, and Contacts. <br>
Mitigation: Install only when the publisher and release binary are trusted, and grant the minimum macOS permissions needed for the intended workflow. <br>
Risk: The skill can enable message sending, email sending, record deletion, photo export, and Messages history access. <br>
Mitigation: Require explicit user confirmation before sending messages or email, deleting records, exporting photos, or granting Full Disk Access for Messages history. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/apple-swift-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline commands and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide installation and use of a native MCP that accesses local Apple app data.] <br>

## Skill Version(s): <br>
1.4.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
