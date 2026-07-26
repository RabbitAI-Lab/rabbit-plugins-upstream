## Description: <br>
Porteden Email helps agents manage email through the Porteden CLI, including reading, searching, sending messages, handling attachments, and switching accounts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill for agent-assisted mailbox workflows across Gmail, Outlook, and Exchange via Porteden CLI commands. It is intended for reading and searching mail, sending messages, downloading attachments, and switching configured accounts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read and send email, manage accounts, and write attachments. <br>
Mitigation: Restrict the account available to the agent, avoid sensitive mailboxes, and manually review every send and download action before execution. <br>
Risk: Broad command pass-through and Invoke-Expression can allow unintended Porteden CLI arguments to run. <br>
Mitigation: Use a reviewed wrapper that removes arbitrary argument pass-through, avoids Invoke-Expression, and confirms outbound email actions. <br>
Risk: Attachment downloads can write mailbox content to local storage. <br>
Mitigation: Confine attachment downloads to a dedicated folder and inspect files before opening or moving them into trusted locations. <br>
Risk: The artifact makes privacy and credential-storage claims that the security evidence does not verify. <br>
Mitigation: Confirm Porteden CLI behavior and terms before using the skill with sensitive mailboxes or regulated data. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with PowerShell command examples and Porteden CLI invocations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an installed and authenticated Porteden CLI; actions may read, send, and download mailbox content.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
