## Description:

Normalize calendar handoffs and create coordination calendar entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill for routine meeting coordination, either to normalize a supplied calendar handoff into an event digest or to create a coordination calendar artifact from a prepared event digest.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Calendar event text supplied to the skill may contain sensitive meeting details.

Mitigation: Confirm the user is comfortable sharing the provided calendar event text before using the skill.

Risk: Generated calendar artifacts may contain incorrect or mismatched scheduling fields if the input event digest is inaccurate.

Mitigation: Review the event ID, start time, end time, timezone, duration, and generated ICS content before sending or importing the artifact.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/coordination-calendar-studio)

## Skill Output:

**Output Type(s):** [text, configuration]

**Output Format:** [Structured object fields for event digests and calendar artifacts, including generated ICS content.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are scoped to the current request and do not require credentials or private file access.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
