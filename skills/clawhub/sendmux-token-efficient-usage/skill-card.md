## Description:

Choose low-token Sendmux calls across MCP, CLI, SDKs, and HTTP by using snippets, counts, batches, deltas, cursors, ETags, and idempotency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to choose efficient Sendmux MCP, CLI, SDK, or HTTP routes for mailbox, sending, management, attachment, sync, and log tasks while minimizing tokens and calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sendmux credentials or scoped tokens could be exposed if a user is asked to paste secrets into chat.

Mitigation: Use available environment variables, CLI profiles, OAuth sessions, or scoped tokens outside chat, and keep SENDMUX_API_KEY values out of model-visible content.

Risk: Email sending, message updates or deletes, and management changes can create external side effects.

Mitigation: Require clear user confirmation before side-effecting operations and use idempotency keys or conditional headers where the skill recommends them.

Risk: Broad mailbox, attachment, or log reads can expose unnecessary content and increase token usage.

Mitigation: Prefer counts, snippets, small limits, selected batch reads, metadata-only attachment handling, cursors, deltas, and ETag checks before fetching full content.

## Reference(s):

- [Sendmux skills homepage](https://github.com/Sendmux/skills)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with CLI, SDK, MCP, and HTTP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Focuses on low-token Sendmux route selection, credential boundaries, batching, cursors, ETags, idempotency, and attachment handling.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
