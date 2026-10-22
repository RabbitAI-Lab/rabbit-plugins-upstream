## Description:

Analyzes children's study-area video or video URLs through a cloud service and presents focus scores, distraction periods, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and teachers use the skill to review focus scores, distraction intervals, and historical reports from children's study-area videos as an aid to observation, not a substitute for their judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Children's study-area videos or URLs and resulting reports are sent to cloud services.

Mitigation: Obtain guardian or school consent and confirm service access controls, retention, deletion, and report sharing before use.

Risk: A silently managed local identity and authentication state can link reports across sessions or accounts.

Mitigation: Check account separation, protect local tokens, and verify whether historical reports can be exported or revoked.

Risk: Focus scores and distraction labels may be mistaken for a definitive assessment of a child.

Mitigation: Use the results only as observational aids and review them with the child's context in mind.

## Reference(s):

- [Child focus analysis API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis text or JSON; Markdown table for historical reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include per-minute focus scores, distraction events, and cloud report links; results can be saved to a file.]

## Skill Version(s):

1.0.13 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
