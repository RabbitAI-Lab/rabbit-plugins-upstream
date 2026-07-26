## Description: <br>
docker-mailbox lets agents and scripts read, search, send, mark seen, and delete messages across one or more configured IMAP/SMTP mailboxes through a REST API and streamable HTTP MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to connect an agent to a running mailboxd service so it can inspect, search, send, and manage mail across configured accounts. It is suited to real mailbox workflows where the user can configure authentication and confirm destructive actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can operate real mailboxes, including reading and sending messages. <br>
Mitigation: Install only for mailboxes the user intends an agent or script to control, and point MAILBOX_URL only at a trusted mailboxd instance. <br>
Risk: If auth.tokens is empty, reachable HTTP and MCP endpoints have full mailbox access without authentication. <br>
Mitigation: Configure long random bearer tokens, keep the service bound locally or behind an authenticating proxy, and avoid public exposure unless remote access is required. <br>
Risk: Message deletion is permanent because deleted messages are expunged immediately. <br>
Mitigation: Require explicit user confirmation of the exact mailbox and UID before deletion, and avoid bulk deletion directly from broad search results. <br>
Risk: The configuration file and tunnel credentials contain sensitive mailbox passwords, bearer tokens, and remote access credentials. <br>
Mitigation: Protect config.yaml and tunnel credential files, keep them out of version control and chats, use restrictive permissions, and mount configuration read-only where possible. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/docker-mailbox) <br>
- [Publisher profile](https://clawhub.ai/user/psyb0t) <br>
- [Setup reference](references/setup.md) <br>
- [Project homepage](https://github.com/psyb0t/docker-mailbox) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, REST examples, MCP configuration snippets, and operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include mailbox search, read, send, mark-seen, and delete instructions that require a running mailboxd service and configured credentials.] <br>

## Skill Version(s): <br>
1.2.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
