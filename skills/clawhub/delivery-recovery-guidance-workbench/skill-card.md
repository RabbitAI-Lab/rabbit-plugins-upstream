## Description:

Turn delivery failure details into a bounded retry schedule and a next-action handoff record.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External teams and developers use this skill after a delivery attempt fails to turn retry guidance into a bounded schedule and handoff record.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A retry schedule could exceed the intended maximum attempts or continue after a terminal delivery state.

Mitigation: Apply the documented max_attempts limit and stop scheduling when a terminal response, expired delivery window, or manual-handling request is present.

Risk: If the retry policy is missing or ambiguous, the agent could produce unsupported timing guidance.

Mitigation: Return a next action asking the delivery owner to choose a structured retry policy before scheduling.

## Reference(s):

- [Handoff Recovery Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/delivery-recovery-guidance-workbench)

## Skill Output:

**Output Type(s):** [text, guidance, configuration]

**Output Format:** [Markdown or structured text describing recorded_retry_mode]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces attempts_remaining, ordered retry_times, and next_action fields for the delivery handoff.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
