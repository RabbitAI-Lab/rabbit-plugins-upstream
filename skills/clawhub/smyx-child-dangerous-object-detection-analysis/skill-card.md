## Description:

Analyzes child activity-zone images or videos to detect contact with dangerous objects or socket-insertion behavior and return alerts, structured results, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, guardians, educators, and developers use this skill to analyze child activity-area media for dangerous-object contact and related emergency warning signals. It can also return cloud-backed historical analysis records associated with the skill's internal identity flow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive child and home monitoring media or media URLs may be sent to configured lifeemergence.com and open.lifeemergence.com services.

Mitigation: Use only with explicit guardian consent, clear retention and deletion expectations, and the minimum media needed for the analysis.

Risk: The skill automatically creates or reuses a persistent cloud-linked identity and may keep local workspace data or tokens for report history access.

Mitigation: Review identity and token handling before deployment, limit workspace access, and require deliberate confirmation before querying historical reports.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-child-dangerous-object-detection-analysis)
- [Child dangerous object detection API documentation](artifact/references/api_doc.md)
- [Analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files]

**Output Format:** [Markdown or JSON-like structured analysis text with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include detected child-safety events, alert level, confidence, event metadata, report links, and history-list results.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
