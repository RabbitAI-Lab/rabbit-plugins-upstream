## Description:

Analyzes child night-time sleep audio/video to report rollover frequency, crying, sleep-talk events, sleep-quality signals, and possible nightmare or restless-sleep alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, guardians, and agents supporting child sleep monitoring use this skill to analyze uploaded night-time sleep media and return behavior statistics, report links, and non-diagnostic comfort guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive child bedroom audio/video and report history may be sent to a configured network service.

Mitigation: Confirm guardian consent, endpoint ownership, retention and deletion terms, and encryption or storage controls before use.

Risk: The skill can silently create or reuse identity records and query historical reports.

Mitigation: Require explicit operator approval for history lookup and verify that local token or identity storage matches the deployment's privacy policy.

Risk: Sleep-quality and nightmare alerts could be mistaken for medical conclusions.

Mitigation: Present results as behavioral observations only and route persistent sleep concerns to a qualified pediatric or sleep professional.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-child-nightmare-rollover-detection-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON sleep analysis report with event statistics, alerts, suggestions, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write the report to a requested output file.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter lists 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
