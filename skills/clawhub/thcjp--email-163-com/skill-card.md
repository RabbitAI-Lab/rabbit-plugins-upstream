## Description: <br>
Email 163 Com helps agents operate a 163.com mailbox through IMAP/SMTP tasks, including sending, reading, searching, folder actions, attachment handling, and message deletion or movement. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to ask an agent to manage a 163.com mailbox: send messages, read and search mail, organize folders, download attachments, and perform explicit message operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide high-impact mailbox actions such as bulk deletion, movement, and sending. <br>
Mitigation: Require message previews and explicit user confirmation before bulk sending, deleting, moving, or marking mail. <br>
Risk: The skill relies on a local mailbox authorization-code configuration that could expose account access if mishandled. <br>
Mitigation: Store credentials outside version control, restrict config-file permissions, and limit use to the intended 163 mailbox tasks. <br>
Risk: Broad command and file authority can expand the impact of incorrect or unrelated mailbox automation. <br>
Mitigation: Restrict execution to explicit 163 IMAP/SMTP workflows and avoid unrelated communication automation or bulk messaging. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/email-163-com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and text output examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce mailbox state changes and local attachment files when the agent executes the generated commands.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
