## Description:

Using a fixed camera at a balcony door or home entrance, this skill analyzes child entry and exit events, estimates daily outdoor-activity duration, and returns structured monitoring results with parent-facing reminders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, parents, schools, kindergartens, and developers can use this skill to analyze fixed-camera video from home entrances or balcony doors and produce child outdoor-activity duration reports. It is intended for visual activity statistics and friendly reminders, not medical diagnosis or direct measurement of actual exercise.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload home entrance or balcony footage involving minors to remote APIs and associate reports with managed identities and stored tokens.

Mitigation: Install only after confirming the publisher's privacy terms, retention and deletion controls, access controls, and token-storage practices are acceptable for minors' home footage.

Risk: Cloud-backed analysis and report history are identity-linked rather than local-only.

Mitigation: Treat generated reports as sensitive records, limit access to authorized guardians or operators, and confirm that users understand where analysis and history are stored.

Risk: Outdoor duration is estimated from visual entry and return events and may not represent actual outdoor exercise or health status.

Mitigation: Use outputs as activity statistics and reminders only, and avoid presenting them as medical advice or diagnosis.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-child-outdoor-activity-monitor-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API 接口文档](references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON structured analysis report with report links and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes child detection status, ROI status, exit and return events, daily outdoor duration, goal completion, alert type, recommendations, and historical report listings when requested.]

## Skill Version(s):

1.0.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
