## Description: <br>
Secure email access via read-no-evil-mcp. Protects against prompt injection attacks in emails. Use for reading, sending, deleting, and moving emails. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thekie](https://clawhub.ai/user/thekie) <br>

### License/Terms of Use: <br>
Apache 2.0 <br>


## Use Case: <br>
Developers and agent users use this skill to connect an AI agent to a read-no-evil-mcp server for email listing, reading, sending, moving, and deletion while relying on server-side prompt-injection scanning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can enable an agent to send, move, or delete email from real mailboxes. <br>
Mitigation: Prefer read-only accounts and restricted folders unless write actions are required, and require explicit user approval before outbound email or mailbox-changing actions. <br>
Risk: Mailbox credentials are provided through a .env file and Docker container environment. <br>
Mitigation: Treat the .env password file and container environment as sensitive and limit access to the host and container. <br>
Risk: Remote server connections can expose email traffic if plain HTTP is used outside localhost. <br>
Mitigation: Use HTTPS for non-localhost server connections. <br>


## Reference(s): <br>
- [read-no-evil-mcp server](https://github.com/thekie/read-no-evil-mcp) <br>
- [Protect AI DeBERTa prompt-injection model](https://huggingface.co/protectai/deberta-v3-base-prompt-injection-v2) <br>
- [Protect AI](https://protectai.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and command-line text output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill can produce email summaries, server setup guidance, configuration commands, and mailbox action commands.] <br>

## Skill Version(s): <br>
0.3.1 (source: server release and changelog, released 2026-02-17; SKILL.md frontmatter lists 0.3.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
