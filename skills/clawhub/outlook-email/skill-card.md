## Description: <br>
Microsoft Outlook/Live.com email client via Microsoft Graph API. List, search, read, send, and reply to emails. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[abhiramee08b021](https://clawhub.ai/user/abhiramee08b021) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and email operators use this skill to manage Outlook, Live, or Hotmail mailboxes from an agent-guided command-line workflow, including listing, searching, reading, sending, and replying to messages after Microsoft Graph authentication. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires high-impact mailbox access while the reviewed bundle does not include the actual CLI source. <br>
Mitigation: Review the external CLI source before installing or authenticating, and test first with a non-sensitive mailbox. <br>
Risk: Send and reply commands can change mailbox state or disclose message content to unintended recipients. <br>
Mitigation: Use the narrowest Microsoft Graph permissions available and confirm every recipient and message body before send or reply actions. <br>
Risk: Local OAuth tokens and client credentials may remain available after use. <br>
Mitigation: Remove stored tokens when the tool is no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/abhiramee08b021/skills/outlook-email) <br>
- [Outlook CLI homepage](https://github.com/abhiramee08b021/outlook-cli) <br>
- [Azure Portal](https://portal.azure.com) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes mailbox read and message-changing workflows; users should verify recipients and message bodies before send or reply actions.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
