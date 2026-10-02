## Description:

Turn delivery failure details into a bounded retry schedule and a next-action handoff record.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Delivery operators use this skill after a failed attempt to plan remaining retries under their active policy and record the next handoff action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unreviewed or free-form retry guidance can produce an inappropriate local schedule.

Mitigation: Check retry_mode against the active policy and review the generated times and next action before acting on them.

Risk: The operation writes a local retry schedule file to the selected output directory.

Mitigation: Use a dedicated writable output directory and inspect the reported effect receipt.

## Reference(s):

- [Handoff Recovery Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/delivery-recovery-guidance-workbench)
- [wxt-ai publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [Text, Files, Guidance]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns attempts_remaining, ordered retry_times, and next_action; also writes a local retry schedule and reports its effect receipt. Does not execute delivery retries.]

## Skill Version(s):

1.1.0 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
