## Description:

Send, receive, and manage asynchronous messages between agents, handlers, and users with local file storage and optional cloud sync.

This skill is ready for commercial/non-commercial use.

## Publisher:

[noizceera](https://clawhub.ai/user/noizceera)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use Agent Mailbox to coordinate asynchronous agent-to-agent, handler-to-agent, and team workflows through local mailbox files, CLI commands, and a TypeScript API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mailbox files and exports are plaintext and may contain sensitive agent, task, or coordination data.

Mitigation: Use the skill only in trusted workspaces, limit mailbox directory access, and handle exports as sensitive files.

Risk: Optional heartbeat automation can process untrusted messages or trigger web callbacks.

Mitigation: Use trusted agent identifiers, avoid running heartbeat processing on untrusted mail, and require allowlists and authentication before enabling callbacks or cloud sync.

Risk: Filesystem writes and deletion behavior can affect local mailbox state.

Mitigation: Review configured mailbox paths before use and prefer archive over delete unless permanent removal is intended.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/noizceera/skills/agent-mailbox)
- [README](artifact/README.md)
- [Skill Overview](artifact/SKILL.md)
- [Agent Heartbeat Example](artifact/examples/agent-heartbeat.ts)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI examples, TypeScript code snippets, and JSON or Markdown mailbox data.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Mailbox messages are local plaintext Markdown files with YAML frontmatter; mailbox exports can be JSON.]

## Skill Version(s):

1.0.0 (source: server release metadata, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
