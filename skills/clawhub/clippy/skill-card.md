## Description: <br>
Microsoft 365 / Outlook CLI for calendar and email management, including calendar events, email workflows, and people or room search. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[foeken](https://clawhub.ai/user/foeken) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to operate the Clippy CLI for Microsoft 365 and Outlook calendar, email, invitation, people, and room workflows from an agent session. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can operate through a signed-in Microsoft 365 browser session to send mail, change calendar data, and keep the session alive persistently. <br>
Mitigation: Install only if the external clippy CLI is trusted, secure and stop keepalive when not needed, and require explicit confirmation before send, reply-all, forward, delete, move, or attachment-download actions. <br>
Risk: The release has no license identifier in the server evidence. <br>
Mitigation: Confirm the applicable license and terms before deployment or redistribution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/foeken/skills/clippy) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands and CLI usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the external clippy binary and a signed-in Microsoft 365 browser session.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
