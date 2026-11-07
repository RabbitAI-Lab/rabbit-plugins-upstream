## Description:

Monitors restricted area intrusions, climbing on dining tables, and rummaging through trash cans, and issues real-time alerts, suitable for home pet monitoring scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners use it to review home monitoring videos for restricted-area entry, climbing on dining tables, and rummaging through trash, and to receive structured alerts and reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using private home footage may expose sensitive information.

Mitigation: Before using private home footage, have the publisher fix export-only mode and confirm the service's privacy, retention, and account-deletion policies.

Risk: Account credentials or local tokens may be exposed.

Mitigation: Keep API secrets separate from account identifiers, restrict credential-bearing requests to approved HTTPS destinations, and protect the local token database.

Risk: The bundle may not provide continuous live alerts.

Mitigation: Do not rely on it for continuous live monitoring; confirm reported alerts by checking the scene.

## Reference(s):

- [Skill overview and demo](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-restricted-area-warning-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured JSON results or Markdown analysis summaries and alerts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports summarize detected behaviors, alert thresholds, and recommendations when provided by the service.]

## Skill Version(s):

1.0.19 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
