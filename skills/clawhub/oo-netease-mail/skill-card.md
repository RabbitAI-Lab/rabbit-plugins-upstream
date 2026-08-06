## Description: <br>
Enables an agent to read, send, reply to, forward, organize, and delete NetEase Mail messages through the OOMOL oo CLI connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent operate a connected NetEase Mail account, including mailbox discovery, message retrieval, sending, replying, forwarding, moving, marking read or unread, downloading attachments, and deletion. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send, forward, reply to, move, mark, and delete email in a connected NetEase Mail account. <br>
Mitigation: Require user confirmation of the exact payload and expected effect before write actions, and explicit approval before destructive delete actions. <br>
Risk: The skill depends on the OOMOL oo CLI and a connected mail account, so account access is delegated through that provider. <br>
Mitigation: Install only when OOMOL is trusted for mail access, connect only the intended account, and review high-impact actions before approving them. <br>


## Reference(s): <br>
- [ClawHub NetEase Mail Skill](https://clawhub.ai/oomol/skills/oo-netease-mail) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>
- [NetEase Mail](https://mail.163.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector action responses include a data object and meta.executionId when run with --json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
