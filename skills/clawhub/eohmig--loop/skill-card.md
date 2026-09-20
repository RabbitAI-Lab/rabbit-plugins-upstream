## Description:

Run a prompt or skill in this session on a recurring or variable interval (e.g. /loop 5m /foo).

This skill is ready for commercial/non-commercial use.

## Publisher:

[eohmig](https://clawhub.ai/user/eohmig)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to run a prompt or another skill immediately and then repeat it on a fixed interval or self-paced event-driven schedule within the current session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repeated prompt execution can repeat any side effects in the prompt.

Mitigation: Use specific prompts and reasonable intervals, and stop loops when they are no longer needed.

Risk: A recurring loop can keep generating session work until stopped.

Mitigation: Track the loop or watcher process, avoid duplicate loops, and stop the tracked process when the user asks.

## Reference(s):

- [Loop skill page](https://clawhub.ai/eohmig/skills/loop)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Session-local scheduling guidance; repeated runs may continue until stopped.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
