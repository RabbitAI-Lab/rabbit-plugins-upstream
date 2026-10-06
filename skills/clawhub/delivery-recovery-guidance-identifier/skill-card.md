## Description:

Set delivery recovery guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Delivery operations staff use the skill to turn a recovery request into concise retry guidance. It does not carry out delivery recovery actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Retry guidance may be mistaken for a complete delivery recovery system.

Mitigation: Use the result only as guidance; verify and carry out recovery separately.

Risk: Switching configuration to downstream mode without an implemented path could break the operation.

Mitigation: Keep the shipped upstream configuration unless an updated materialization path has been implemented and reviewed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wxt-ai/skills/delivery-recovery-guidance-identifier)

## Skill Output:

**Output Type(s):** [Guidance, Text]

**Output Format:** [JSON object with a retry_mode string]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No external communication or persisted business artifact.]

## Skill Version(s):

1.1.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
