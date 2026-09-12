## Description:

Choose low-token Sendmux calls across MCP, CLI, SDKs, and HTTP by using snippets, counts, batches, deltas, cursors, ETags, and idempotency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw agents use this skill to choose efficient Sendmux routes for email, mailbox, management, attachment, webhook, and sending workflows while reducing token usage and unnecessary API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Granted Sendmux scopes can affect real email, mailbox, webhook, sending, and account resources.

Mitigation: Review scopes before use, especially root management keys, sending permissions, mailbox deletion or update operations, webhooks, and CLI profiles.

Risk: Secrets or large attachment payloads could be exposed if routed through model context.

Mitigation: Do not ask users to paste API keys; use Sendmux profiles, scoped tokens, file paths, presigned URLs, CLI attachment flags, or SDK file helpers instead of inline base64.

Risk: Retries or batch operations can create duplicate or mixed side effects.

Mitigation: Use idempotency keys for supported mutations, inspect per-message batch results, and require explicit confirmation before batch update or delete operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sendmux.ai/skills/sendmux-token-efficient-usage)
- [Sendmux skills homepage](https://github.com/Sendmux/skills)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline tables, bash commands, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance emphasizes lower-token Sendmux calls, scoped credentials, batching, deltas, cursors, ETags, attachment transfer paths, and idempotency.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter reports 1.5.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
