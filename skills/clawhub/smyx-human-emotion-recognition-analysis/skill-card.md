## Description:

Uses visual AI on frontal faces to recognize multi-dimensional emotions like happiness, sadness, depression, calmness, anger, surprise, and fear in real-time, with emotion intensity quantification and abnormal emotion marking for human-computer interaction and mental health monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can use this skill to submit face images or videos for cloud-based emotion recognition, review structured emotion indicators, and retrieve historical analysis reports. It is intended for informational emotional state analysis and should not be treated as professional psychological diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends face images, videos, media URLs, and inferred emotional or psychological indicators to the Life Emergence cloud service.

Mitigation: Use only with clear user consent and an approved basis for processing sensitive biometric and emotional data.

Risk: The skill may silently create or reuse a persistent identity, store tokens locally, and maintain cloud report history.

Mitigation: Review identity, token storage, retention, deletion, and report access controls with the publisher before deployment.

Risk: Emotion recognition results can be misleading if treated as psychological diagnosis.

Mitigation: Present outputs as informational signals only and route sustained or severe concerns to qualified professionals.

Risk: Network media URLs are fetched by the cloud service, which can create authorization and URL-fetching exposure.

Mitigation: Restrict inputs to authorized media and confirm the service has protections for private, internal, or untrusted URLs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-human-emotion-recognition-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown reports, JSON analysis results, Markdown history tables, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include emotion labels, intensity scores, abnormal-emotion markers, recommendations, and cloud report export links.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter lists 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
