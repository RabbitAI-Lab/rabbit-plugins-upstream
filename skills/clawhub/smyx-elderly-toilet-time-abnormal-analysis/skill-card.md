## Description:

Analyzes bathroom doorway or privacy-filtered bathroom video to detect elderly toilet entry and exit events, calculate continuous occupancy time, and alert when the stay exceeds the default 30-minute threshold.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers, family members, nursing-home operators, and safety-monitoring agents use this skill to analyze provided video or video URLs for unusually long elderly bathroom occupancy and to retrieve structured monitoring reports. It supports alert-oriented monitoring only and does not provide medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes highly sensitive bathroom-related video, URLs, report history, and identity-linked metadata through configured lifeemergence.com services.

Mitigation: Use only with clear consent from the monitored person or legal caregiver, prefer doorway-only or pre-blurred footage, avoid unrelated URLs, and verify retention, account, and credential handling before production use.

Risk: The skill silently creates or reuses local account identity and tokens.

Mitigation: Review account and token handling before installation, restrict execution to trusted environments, and avoid exposing identity values in user-facing output.

Risk: Long bathroom occupancy alerts can be mistaken for medical conclusions.

Mitigation: Treat results as auxiliary occupancy alerts and require human verification for emergency response or care decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-elderly-toilet-time-abnormal-analysis)
- [API interface reference](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown text containing structured JSON analysis results, alert details, history listings, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local video files or video URLs; documented inputs include mp4, avi, and mov files up to 10 MB.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
