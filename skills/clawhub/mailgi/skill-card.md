## Description:

Give an AI agent a real, deliverable email address. Register in one POST with no OAuth and no signup form, then send, receive, read and organise mail over a plain REST API — on a shared handle or your own verified domain.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oyagev](https://clawhub.ai/user/oyagev)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to register and operate a real Mailgi mailbox through REST API calls, SDK examples, or CLI commands. It supports sending, receiving, reading, organizing, and deleting mail on shared or verified custom domains.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables an agent to send and read real email.

Mitigation: Install only when mailbox operation is intended, require review before outbound messages, and avoid sensitive content unless the mailbox is approved for it.

Risk: Mailgi API keys grant access to the mailbox and may be stored for reuse.

Mitigation: Protect stored API keys, avoid exposing them in logs or shared prompts, and revoke keys that are no longer needed.

Risk: Some API and CLI actions can mark mail read, delete messages, revoke keys, or permanently delete the mailbox.

Mitigation: Require explicit confirmation before destructive operations and prefer registering a second agent instead of deleting an account to reset state.

## Reference(s):

- [Mailgi homepage](https://www.mailgi.xyz)
- [Canonical Mailgi skill file](https://www.mailgi.xyz/SKILL.md)
- [Mailgi interactive API docs](https://api.mailgi.xyz/docs)
- [Mailgi OpenAPI specification](https://api.mailgi.xyz/openapi.json)
- [Mailgi ClawHub skill page](https://clawhub.ai/oyagev/skills/mailgi)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with REST examples, JSON payloads, TypeScript snippets, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce live email API calls and CLI commands; MAILGI_API_KEY is optional for reuse of an existing mailbox.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
