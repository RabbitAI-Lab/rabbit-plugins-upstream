## Description: <br>
AgentMail (QQ) lets an agent operate a QQ AgentMail mailbox through OOMOL's agent_qq connector for listing aliases, searching and reading messages, sending mail, and deleting messages. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to manage an AgentMail (QQ) mailbox through an OOMOL-connected account, including reading, searching, sending, and deleting messages with user confirmation for state-changing actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read, send, and delete AgentMail QQ mailbox content through OOMOL-connected tools. <br>
Mitigation: Install only when mailbox access through OOMOL is intended, and review send and delete payloads carefully before approving state-changing actions. <br>
Risk: One-time CLI installation, account sign-in, connector authorization, and billing actions are sensitive setup steps. <br>
Mitigation: Treat setup prompts as approval-sensitive actions and only run them when a command fails for the matching authentication, connection, or billing reason. <br>
Risk: Connector action schemas can change, making stale payload assumptions unsafe. <br>
Mitigation: Inspect the live agent_qq connector schema before each action and build payloads from the returned contract. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-agent-qq) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>
- [AgentMail (QQ) Homepage](https://agent.qq.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and connector JSON responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires live connector schema inspection before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
