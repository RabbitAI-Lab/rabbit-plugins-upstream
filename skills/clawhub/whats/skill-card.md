## Description: <br>
Send WhatsApp messages to other people or search/sync WhatsApp history via the wacli CLI (not for normal user chats). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[engahmedsalah358-lgtm](https://clawhub.ai/user/engahmedsalah358-lgtm) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to direct an agent to send WhatsApp messages through wacli, or to search and sync WhatsApp history, only when explicitly requested. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access a linked WhatsApp account and send messages or files to contacts. <br>
Mitigation: Use it only after an explicit user request, verify the exact recipient, message, and attachment path, and confirm before sending. <br>
Risk: WhatsApp sync and search may store sensitive chat data locally. <br>
Mitigation: Keep sync and search scope narrow, review the configured store directory, and protect or remove local chat data when it is no longer needed. <br>
Risk: The skill depends on the external wacli CLI and the user's WhatsApp session. <br>
Mitigation: Install wacli only from trusted sources, run wacli doctor when needed, and expect backfill results to be best-effort when the phone is offline. <br>


## Reference(s): <br>
- [What's app ClawHub listing](https://clawhub.ai/engahmedsalah358-lgtm/skills/whats) <br>
- [wacli homepage](https://wacli.sh) <br>
- [wacli Go install module](https://github.com/steipete/wacli) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include wacli commands for authentication, sync, chat search, history backfill, and sending text or files.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
