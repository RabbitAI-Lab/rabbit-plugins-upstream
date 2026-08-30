## Description:

Uses visual AI on frontal faces to recognize multi-dimensional emotions like happiness, sadness, depression, calmness, anger, surprise, and fear in real-time, with emotion intensity quantification and abnormal emotion marking for human-computer interaction and mental health monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze face images or videos for structured visual emotion recognition reports, including dominant emotions, intensity scores, abnormal emotion flags, report links, and historical report lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends face images or videos and derived emotion-analysis data to a configured cloud service.

Mitigation: Use only with appropriate consent and avoid high-stakes contexts such as clinical, employment, school discipline, or similar decisions unless separate controls are in place.

Risk: Reports are linked to an internally managed identity and account tokens may be stored locally in the workspace.

Mitigation: Review retention, access controls, and workspace storage before installation, and limit use to environments where this identity and token handling is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-human-emotion-recognition-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [Analysis API interface documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON structured analysis report with optional report link and historical report table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save the analysis result to a caller-provided output file.]

## Skill Version(s):

1.0.13 (source: server release metadata; artifact frontmatter lists 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
