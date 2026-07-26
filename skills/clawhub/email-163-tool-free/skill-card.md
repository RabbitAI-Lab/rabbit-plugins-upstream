## Description: <br>
163邮箱助手免费版 helps personal users manage a NetEase 163 mailbox through command-line assisted sending, reading, searching, folder management, and attachment workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, personal developers, and small teams use this skill to operate a user-owned 163 mailbox for everyday email sending, reading, searching, folder operations, and attachment handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires sensitive 163 mailbox access through an authorization code. <br>
Mitigation: Use a dedicated authorization code, store it only in a private config file or environment variable, and rotate it regularly. <br>
Risk: The skill can send email, delete messages, delete folders, download attachments, and use callback URLs. <br>
Mitigation: Require explicit user confirmation before destructive actions, outbound email sending, attachment downloads, or callback URL use. <br>
Risk: Broad communication automation can be misused for unwanted or unsafe messaging. <br>
Mitigation: Limit use to the user's own mailbox and avoid generic or bulk communication workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/email-163-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Text, JSON] <br>
**Output Format:** [Markdown guidance with command examples and text or JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce mailbox operation status, search results, logs, configuration snippets, and attachment download paths.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
