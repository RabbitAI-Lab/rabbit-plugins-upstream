## Description:

This skill analyzes fixed-camera infrared or low-light footage of an older adult at rest to estimate respiratory rate and flag tachypnea or dyspnea risk from visual breathing motion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, caregivers, and developers can use this skill to submit elderly rest-state chest or abdominal monitoring videos for respiratory-rate analysis, structured risk flags, and historical report lookup. The skill is an auxiliary monitoring aid and is not a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive bedroom monitoring videos and related health reports are uploaded to the publisher cloud service.

Mitigation: Use only with explicit consent from the monitored person or authorized caregiver, and apply appropriate retention, access, and encryption controls for source videos and reports.

Risk: The security evidence flags unsafe default HTTP configuration.

Mitigation: Require HTTPS production endpoints before use and avoid development or LAN HTTP endpoints for sensitive health footage.

Risk: The security evidence flags automatic local identity and token persistence.

Mitigation: Apply token storage controls, limit local access to persisted identity data, and provide a documented way to clear stored local identity records.

Risk: Visual respiratory-rate estimates and alert levels can be mistaken for clinical diagnosis.

Mitigation: Present outputs as auxiliary monitoring signals, require human follow-up for urgent alerts, and direct users to qualified medical care when symptoms or risk indicators are serious.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-elderly-tachypnea-detection-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Elderly Tachypnea API Documentation](artifact/references/api_doc.md)
- [Shared Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown and JSON text containing structured analysis results, respiratory-rate fields, risk level, alert text, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload local files or pass remote video URLs to the publisher cloud service; supports historical report listing.]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata; artifact frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
