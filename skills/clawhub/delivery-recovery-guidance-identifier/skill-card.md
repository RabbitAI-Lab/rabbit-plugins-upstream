## Description:

Sets concise delivery recovery guidance for a supplied handoff, transfer note, or service recovery request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations users use this skill during routine delivery work to choose a concise retry mode for a current handoff, transfer note, or service recovery request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The returned retry mode could be treated as operational direction without checking local delivery policy.

Mitigation: Confirm the guidance against the applicable delivery policy before applying it in a real workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/delivery-recovery-guidance-identifier)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [String]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns a concise retry_mode value from a user-supplied recovery_request.]

## Skill Version(s):

1.0.7 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
