## Description: <br>
Send Signal messages and look up Signal recipients via the local signal-cli installation on macOS. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pseudobun](https://clawhub.ai/user/pseudobun) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Users and agents with a registered local signal-cli setup use this skill to resolve Signal contacts and send confirmed Signal messages or attachments from macOS. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent can use the local registered Signal account to send a message to the wrong recipient or with unintended content. <br>
Mitigation: Confirm the exact recipient, final message text, and attachments with the user before sending. <br>
Risk: Contact lookup may expose local Signal contact data or return ambiguous matches. <br>
Mitigation: Limit lookups to the requested recipient and present ambiguous matches for user selection before sending. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pseudobun/skills/signal-cli) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown guidance with shell commands and JSON script output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local signal-cli state and should confirm recipient, message text, and attachments before sending.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
