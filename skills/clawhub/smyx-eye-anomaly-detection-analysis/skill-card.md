## Description:

Analyzes pet facial images or videos for eye redness, abnormal tearing, and corneal or pupil cloudiness, then provides anomaly alerts and care guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, boarding staff, and veterinary teams use close-up pet images or video to screen for visible eye changes, review alert severity, and decide when to seek a veterinarian's assessment. Results are visual screening guidance, not a diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet images or video URLs are sent to an external analysis service.

Mitigation: Obtain consent before submitting media and disclose the external service and its data handling.

Risk: The skill automatically creates or reuses a cloud-linked identity and stores tokens.

Mitigation: Document identity and token storage, access, and deletion; limit permissions to the minimum necessary.

Risk: Report history can be retrieved from the cloud without an explicit confirmation step.

Mitigation: Ask for confirmation before retrieving or displaying historical reports.

Risk: Image-based eye assessments may miss or misclassify veterinary conditions.

Mitigation: Treat alerts as screening guidance and seek veterinary assessment for suspected abnormalities.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-eye-anomaly-detection-analysis)
- [Skill API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis report text or Markdown history table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include severity and care suggestions; results can be saved to a local file.]

## Skill Version(s):

1.0.9 (source: ClawHub release; bundled frontmatter lists 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
