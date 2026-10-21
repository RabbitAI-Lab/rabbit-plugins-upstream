## Description:

Analyzes fixed-camera video at a home entrance or balcony door to estimate a child's daily outdoor time from exit and return events and provide reminders when the estimated time falls short.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Guardians and their authorized assistants use doorway or balcony video to review estimated outdoor-session durations, receive activity reminders, and view historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Child and household entrance or balcony footage is sent to a cloud service.

Mitigation: Obtain informed guardian consent, confirm where the footage is processed, and use only relevant recordings.

Risk: Reports are tied to a locally persisted internal user identity and token.

Mitigation: Review where reports and tokens are stored and restrict access to them before use.

Risk: Door-crossing estimates can misrepresent actual outdoor exercise or confuse children in multi-child footage.

Mitigation: Treat durations as approximate and review ambiguous events before acting on reminders.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-child-outdoor-activity-monitor-analysis)
- [Publisher profile](https://clawhub.ai/user/18072937735)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured report or Markdown history list, with JSON available on request]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Estimated outdoor durations, reminders, report links, and optional saved output.]

## Skill Version(s):

1.0.13 (source: server-resolved ClawHub release; skill frontmatter says 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
