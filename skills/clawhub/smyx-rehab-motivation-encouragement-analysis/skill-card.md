## Description:

Analyzes fixed-camera rehabilitation-session video, with optional audio, to identify signs of patient frustration or giving-up tendency and produce structured motivation guidance, alerts, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External rehabilitation teams and developers use this skill to process rehabilitation training media or URLs and return structured observations about frustration signals, motivation actions, therapist or family escalation, and report links. It is intended to support patient motivation and adherence, not to make medical diagnoses or adjust rehabilitation plans without clinician review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive rehabilitation video and patient-linked history could be exposed if development HTTP endpoints are used.

Mitigation: Install only after the publisher removes development HTTP configuration and enforces HTTPS production endpoints.

Risk: Silent identity and token handling can make patient identity creation and report-history linkage unclear.

Mitigation: Require explicit documentation and controls for identity lifecycle, credential separation, and report access before deployment.

Risk: Camera/audio monitoring and therapist or family notifications affect patient privacy and consent.

Mitigation: Document consent controls for monitoring and notifications, and verify them with the deploying rehabilitation organization.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-rehab-motivation-encouragement-analysis)
- [API Documentation](references/api_doc.md)
- [Nested API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-oriented structured analysis reports with command examples and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save analysis output to a caller-provided file and may list historical reports as a Markdown table.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
