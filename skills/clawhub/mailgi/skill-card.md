## Description:

Give an AI agent a real, deliverable email address. Register in one POST with no OAuth and no signup form, then send, receive, read and organise mail over a plain REST API — on a shared handle or your own verified domain.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oyagev](https://clawhub.ai/user/oyagev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to give agents a deliverable email inbox, then send, receive, read, and organize mail through REST API, SDK, or CLI workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents can send and read email and manage mailbox state.

Mitigation: Review send, delete, mailbox, API-key, and account-removal actions before execution.

Risk: Mailgi API keys and custom-domain registration tokens grant mailbox or address-creation capabilities.

Mitigation: Treat API keys and domain registration tokens as credentials; provide domain tokens only when the agent should create addresses on that domain.

Risk: Deleting an agent account is permanent and burns the email address.

Mitigation: Avoid account deletion for resets; register another agent and stop using the old mailbox instead.

Risk: Sending immediately after registration can fail while the mailbox is provisioned.

Mitigation: Wait briefly after registration and retry once on transient server errors.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oyagev/skills/mailgi)
- [Mailgi homepage](https://www.mailgi.xyz)
- [Canonical Skill File](https://www.mailgi.xyz/SKILL.md)
- [Mailgi API Docs](https://api.mailgi.xyz/docs)
- [Mailgi OpenAPI Specification](https://api.mailgi.xyz/openapi.json)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown with REST examples, shell commands, TypeScript snippets, and CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes API-key handling guidance, mailbox lifecycle notes, rate limits, and unsupported-feature constraints.]

## Skill Version(s):

1.1.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
