## Description:

Use this skill to help an agent work with Evite invitations and hosted events, including event lookup, guest lists, RSVP summaries, messages, and event authoring actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent manage Evite event workflows, inspect invitation and RSVP state, and prepare or execute host and guest actions with confirmation where writes are involved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup can expose Evite account credentials or browser session cookies.

Mitigation: Use a scoped secret store or environment injection, avoid committing real credentials to `.mcp.json`, and disable browser-cookie bootstrap unless the environment is trusted.

Risk: The setup uses an unpinned external MCP package by default.

Mitigation: Install or invoke a pinned package version in a project-scoped configuration before enabling the skill.

Risk: Guest lists, invitation messages, RSVP changes, and cancellation actions are sensitive account operations.

Mitigation: Review dry-run previews and require explicit confirmation before sending, editing, canceling, or messaging through Evite.

## Reference(s):

- [ClawHub evite skill page](https://clawhub.ai/chrischall/skills/evite)
- [evite-mcp npm package](https://www.npmjs.com/package/evite-mcp)
- [evite-mcp source repository](https://github.com/chrischall/evite-mcp)
- [Evite](https://www.evite.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dry-run previews for write actions and confirmation-gated event operations.]

## Skill Version(s):

0.8.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
