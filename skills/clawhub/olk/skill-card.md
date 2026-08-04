## Description: <br>
Microsoft Outlook and OneDrive CLI and MCP for email, calendar, contacts, tasks, and files, for personal and enterprise accounts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rlrghb](https://clawhub.ai/user/rlrghb) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to operate Outlook mail, calendar, contacts, tasks, and OneDrive files through the olk CLI or MCP server. It supports personal Microsoft accounts and enterprise Azure AD/Entra ID workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access broad Microsoft account data across Outlook and OneDrive. <br>
Mitigation: Install and authorize it only when that account access is acceptable for the intended user or environment. <br>
Risk: Agent or unattended runs could mutate account state or send outbound messages. <br>
Mitigation: Use OLK_NO_WRITE=1, OLK_NO_SEND=1, OLK_NO_INPUT=1, and command allowlists for unattended operation. <br>
Risk: Forced destructive actions can bypass interactive confirmation. <br>
Mitigation: Avoid --force and OLK_FORCE unless the user explicitly intends the action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/rlrghb/skills/olk) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference JSON, table, or plain-text command output from olk.] <br>

## Skill Version(s): <br>
1.11.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
