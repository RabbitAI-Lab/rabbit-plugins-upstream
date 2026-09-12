## Description:

Analyzes night video from a fixed living-room or bedroom camera for a person living alone to estimate lights-off timing, early-morning movement, baseline rhythm deviation, and rhythm-anomaly reminders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, caregivers, family members, and community care workers use this skill to review night-video rhythm indicators for people living alone and receive structured anomaly reminders for follow-up. It is intended to provide visual rhythm parameters and deviation prompts, not medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes highly private bedroom or living-room night video and health-adjacent rhythm reports.

Mitigation: Use only with explicit consent from the monitored person or lawful guardian, minimize captured footage, and prefer privacy-preserving views such as silhouettes or mosaics where possible.

Risk: Security evidence reports unsafe transport and persistent local credential storage for account tokens.

Mitigation: Do not use real footage or live accounts until production endpoints are HTTPS-only and token storage is secured.

Risk: Silent identity creation and historical report access can make account control, retention, and authorization hard to verify.

Mitigation: Require visible identity/account controls, clear retention and deletion terms, and access controls for report history and exported reports before deployment.

## Reference(s):

- [Living-Alone Rhythm API Documentation](artifact/references/api_doc.md)
- [SMYX Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown or text containing structured JSON-style analysis results, anomaly messages, historical report lists, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include current rhythm metrics, baseline metrics, deviation scores, anomaly type, alert level, follow-up message, and exported report URL.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
