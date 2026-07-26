## Description: <br>
Mailbox helps an agent read, search, send, triage, and manage email across Gmail, QQ, 163, Outlook, and other IMAP/SMTP accounts through a command-line mailbox tool. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leeguooooo](https://clawhub.ai/user/leeguooooo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to automate mailbox workflows, including listing unread mail, searching messages, reading message bodies, sending email, and preparing or applying mailbox cleanup actions with JSON-oriented command output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may install the mailbox CLI by piping a remote installer to a shell. <br>
Mitigation: Review the installer first and prefer a pinned or verifiable install path before running it. <br>
Risk: Mailbox credentials are configured on disk for agent-accessible email accounts. <br>
Mitigation: Configure only the mail accounts the agent needs and restrict permissions on the mailbox auth file. <br>
Risk: The optional persistent daemon can provide always-on mailbox automation. <br>
Mitigation: Skip the daemon unless persistent mailbox access is required, and review daemon status during setup. <br>


## Reference(s): <br>
- [Server-resolved GitHub source](https://github.com/leeguooooo/Mailbox/tree/main/skills/mailbox) <br>
- [Mailbox repository](https://github.com/leeguooooo/Mailbox) <br>
- [Mailbox CLI npm package](https://www.npmjs.com/package/@leeguoo/mailbox-cli) <br>
- [ClawHub skill page](https://clawhub.ai/leeguooooo/skills/mailbox) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON response expectations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands are expected to request JSON output and check success or error fields before continuing.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
