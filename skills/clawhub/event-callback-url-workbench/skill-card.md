## Description:

Register an event callback address.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Integration operators and developers use this skill to record a callback URL supplied in the current request for an event subscription workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A user may interpret the recorded callback object as confirmation that an external subscription was actually registered.

Mitigation: Treat the output as a structured record only, and perform any real subscription change through an authorized downstream system or workflow.

Risk: An incorrect callback_url could propagate into later integration steps.

Mitigation: Validate the supplied callback URL before using the recorded callback in downstream subscription or routing work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/event-callback-url-workbench)

## Skill Output:

**Output Type(s):** [text, configuration]

**Output Format:** [Structured text record]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns recorded_callback with subscription_draft_id, callback_url, callback_host, and callback_path.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
