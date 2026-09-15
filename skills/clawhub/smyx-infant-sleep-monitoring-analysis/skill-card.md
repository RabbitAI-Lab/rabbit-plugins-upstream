## Description:

Identifies infant sleep states such as deep sleep, light sleep, waking, and restlessness, then generates daily sleep reports and schedule analysis to help caregivers understand sleep patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers and agent users use this skill to analyze infant sleep monitoring videos or video URLs, classify sleep states, and retrieve structured sleep reports and report history from the Life Emergence cloud service. Results are for caregiving reference and do not replace professional medical advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive infant sleep videos, report history, and account-linked metadata may be sent to the Life Emergence cloud service.

Mitigation: Use the skill only with explicit upload consent and after reviewing retention, deletion, and data handling terms for the cloud service.

Risk: Security evidence reports hidden identity handling and plaintext token storage.

Mitigation: Review local credential storage before installation, run in an isolated workspace, and clear stored tokens or report data after use.

Risk: Security evidence reports active plaintext development configuration and recommends HTTPS-only production configuration.

Mitigation: Do not deploy until the publisher ships HTTPS-only production endpoints and removes plaintext development configuration from the release.

Risk: Infant sleep analysis results could be mistaken for medical guidance.

Mitigation: Treat results as caregiving reference only and consult a pediatric clinician for abnormal sleep or health concerns.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-sleep-monitoring-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Interface Documentation](references/api_doc.md)
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON]

**Output Format:** [Markdown-formatted text with structured JSON analysis results and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can optionally write returned report text to a local output file; accepts local mp4, avi, or mov files up to 10 MB, or public video URLs.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter reports 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
