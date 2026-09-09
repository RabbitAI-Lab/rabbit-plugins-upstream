## Description:

Uses visual AI on frontal faces to recognize multi-dimensional emotions like happiness, sadness, depression, calmness, anger, surprise, and fear in real-time, with emotion intensity quantification and abnormal emotion marking for human-computer interaction and mental health monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze face images or videos for structured emotion-recognition results, anomaly flags, trends, recommendations, and report links. The output is informational and should not be treated as a professional mental health diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Face images, videos, and emotion-analysis metadata may be sent to the publisher's cloud service.

Mitigation: Use only with appropriate consent and data-handling approval, and avoid regulated diagnostic use unless reviewed by qualified professionals.

Risk: Distributed defaults include insecure development HTTP endpoints.

Mitigation: Switch configuration to reviewed HTTPS production endpoints and verify network destinations before deployment.

Risk: The skill can create or reuse identities and store tokens locally.

Mitigation: Document identity and retention behavior, prefer explicit account provisioning, and clear local tokens when access should end.

Risk: API documentation and dependency declarations may not match the implemented cloud emotion-analysis behavior.

Mitigation: Validate dependencies, API endpoints, file limits, and response formats in a staging environment before production use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-human-emotion-recognition-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)
- [Common Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [JSON or Markdown analysis reports with optional report links and Markdown tables for historical report listings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include emotion scores, abnormal emotion markers, trend summaries, recommendations, and cloud report export links.]

## Skill Version(s):

1.0.14 (source: server release metadata; artifact frontmatter says 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
