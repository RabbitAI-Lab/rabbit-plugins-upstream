## Description:

Analyzes driver videos for unsafe behavior and produces driving-safety reports with findings and recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Drivers, fleet operators, and safety educators can review driving footage for signs of fatigue, distraction, seatbelt misuse, and other unsafe behavior, then examine safety reports or past results. Reports are educational aids, not substitutes for professional driving instruction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Driver footage or video URLs are sent to lifeemergence.com services for analysis.

Mitigation: Obtain consent and confirm the service's handling of sensitive footage before submitting it.

Risk: The skill creates or reuses an internal identity and stores account tokens in a local workspace database without clear user control.

Mitigation: Review identity and token-storage practices and restrict access to the workspace before using the skill.

Risk: Cloud-stored report history can be queried, while retention and deletion controls are not clearly documented.

Mitigation: Confirm retention, deletion, and history-access policies before processing personal driving footage.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-drive-analysis)
- [API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured driving-safety reports or JSON, with report links and optional history lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes identified behaviors, safety warnings, and recommendations; results can be saved to a file.]

## Skill Version(s):

1.0.15 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
