## Description:

Choose low-token Sendmux calls across MCP, CLI, SDKs, and HTTP by using snippets, counts, batches, deltas, cursors, ETags, and idempotency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to choose efficient Sendmux MCP, CLI, SDK, or HTTP routes for mailbox, sending, attachment, log, and management tasks while minimizing token-heavy reads and repeated requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may use Sendmux credentials or permissions beyond what the user intends.

Mitigation: Use only Sendmux credentials and permissions intended for the agent, and do not ask users to paste secrets into chat.

Risk: Email sending, deletion, key, webhook, or management actions can have external side effects.

Mitigation: Review these actions before approval and use the skill's batching, idempotency, and explicit-confirmation guidance for mutations.

Risk: Large mailbox bodies, logs, or attachments can expose unnecessary content and consume excessive context.

Mitigation: Prefer counts, snippets, selected IDs, metadata, presigned URLs, small limits, and attachment transfer paths outside model context.

## Reference(s):

- [Sendmux Skills Repository](https://github.com/Sendmux/skills)
- [ClawHub Skill Page](https://clawhub.ai/sendmux.ai/skills/sendmux-token-efficient-usage)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Focuses on lower-token Sendmux route selection; it does not generate files.]

## Skill Version(s):

1.0.7 (source: server release evidence; artifact frontmatter reports 1.4.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
