## Description: <br>
Desktop Notify sends cross-platform desktop notifications and sound alerts when a long-running task, generated artifact, or background job completes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cipher0117](https://clawhub.ai/user/cipher0117) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and agent users use this skill to receive local audio and visual completion alerts after long-running work finishes. It can also configure WorkBuddy to run a local notification command after future responses when the user explicitly runs setup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Running setup persistently changes global WorkBuddy memory so a notification command runs after future responses. <br>
Mitigation: Use the notify script directly for one-off alerts, avoid setup unless persistent behavior is desired, and remove the block marked <!-- desktop-notify-auto --> from ~/.workbuddy/MEMORY.md to disable it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cipher0117/skills/desktop-notify) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell command examples and short status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Notification scripts may trigger local OS desktop notifications and sound alerts; setup scripts may append a marked rule to ~/.workbuddy/MEMORY.md.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact manifest) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
