## Description:

Set timers and alarms that run in the background and prompt the agent to notify the user when they complete.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hisxo](https://clawhub.ai/user/hisxo)

### License/Terms of Use:


## Use Case:

External users and developers use this skill to start, monitor, and cancel local countdown timers or reminders while working with an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill starts local background timer processes that continue until completion or cancellation.

Mitigation: List or poll running sessions and cancel timers that are no longer needed.

Risk: Reminder text is printed in process logs.

Mitigation: Avoid placing sensitive information in timer labels.

Risk: macOS sound playback depends on afplay being available.

Mitigation: Treat sound as optional and rely on the agent's completion message for the timer notification.

## Reference(s):

- [ClawHub skill page for timer](https://clawhub.ai/hisxo/skills/timer)
- [ClawHub publisher profile for hisxo](https://clawhub.ai/user/hisxo)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline bash and process-control commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a local Node.js runtime; timer labels are written to process output logs.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
