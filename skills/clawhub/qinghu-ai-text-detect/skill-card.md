## Description:

Checks submitted text for indicators of AI generation and summarizes overall confidence, estimated AI proportion, and segment-level results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Users submit text to assess whether it may be AI-generated and receive a concise breakdown of the detection results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted text is sent to Qinghu's external service and may include confidential or personal information.

Mitigation: Review the text and service terms before submission; avoid sending sensitive content without authorization.

Risk: Detection calls consume Qinghu credits.

Mitigation: Check the estimated cost and obtain user consent before making paid calls.

Risk: Automatic setup may download Node or unpinned packages and change shell startup files.

Mitigation: Preinstall qhkit using an approved package-management process; review and approve any environment changes separately.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-ai-text-detect)
- [qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise text or Markdown summary; a table file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes confidence, estimated AI proportion, segment details when available, and credits spent.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
