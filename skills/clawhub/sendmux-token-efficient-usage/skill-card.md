## Description:

Choose low-token Sendmux calls across MCP, CLI, SDKs, and HTTP by using snippets, counts, batches, deltas, cursors, ETags, and idempotency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to choose efficient Sendmux mailbox, sending, and management calls while minimizing unnecessary reads, transfers, and repeat requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad credentials or exposed secrets could permit unintended mailbox or management access.

Mitigation: Use credentials scoped to the intended actions and do not paste secrets into chat.

Risk: Sending email, deleting messages, and changing keys or webhooks can have significant effects.

Mitigation: Require user direction and review these actions before execution.

## Reference(s):

- [Sendmux skills homepage](https://github.com/Sendmux/skills)
- [Sendmux token-efficient usage on ClawHub](https://clawhub.ai/sendmux.ai/skills/sendmux-token-efficient-usage)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with CLI and SDK examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommends bounded results, batching, incremental sync, and safe retries.]

## Skill Version(s):

1.0.10 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
