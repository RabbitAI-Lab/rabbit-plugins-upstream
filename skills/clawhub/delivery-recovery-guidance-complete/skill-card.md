## Description:

Turns delivery failures into a bounded retry schedule and next-action handoff, saving a local record and optionally delivering it to a configured destination.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations teams and developers use this skill to plan retries after a delivery failure, record the next action, and optionally submit the result to a configured destination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A configured delivery target may send the recovery record outside the local workspace.

Mitigation: Enable delivery deliberately; for local-only use, clear delivery endpoint and credential environment variables and omit the delivery configuration file.

Risk: The skill creates retry-schedule files in the chosen output location.

Mitigation: Use a dedicated output directory and review the recorded schedule before acting on it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/wxt-ai/skills/delivery-recovery-guidance-complete)
- [Skill README](artifact/README.md)

## Skill Output:

**Output Type(s):** [Guidance, JSON]

**Output Format:** [JSON result and local retry-schedule record]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes retry timing, a next action, and a delivery receipt when configured.]

## Skill Version(s):

1.2.0 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
