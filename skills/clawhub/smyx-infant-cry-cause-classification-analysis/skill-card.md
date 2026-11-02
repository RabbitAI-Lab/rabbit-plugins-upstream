## Description:

Analyzes infant cry audio or audio from video to estimate likely causes and provide confidence scores and directional soothing suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and caregivers can submit an infant cry audio clip or video with audio to receive an estimate of possible causes, confidence, and soothing suggestions. The result is a parenting aid and is not a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private infant recordings may still be uploaded when the no-analysis option is used.

Mitigation: Before submitting private recordings, verify a working no-analysis mode and explicit cloud-upload controls; obtain guardian consent and avoid uploading sensitive audio if those controls are unclear.

Risk: Account creation and stored credential handling do not have clear user controls.

Mitigation: Use protected token storage, restrict where credentials can be sent, and avoid sharing the default account across users.

Risk: The provider's recording retention and deletion practices, server behavior, and classification quality are unverified.

Mitigation: Confirm retention and deletion practices before use, and treat classifications as non-diagnostic suggestions; seek pediatric care for persistent or unusual crying.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-infant-cry-cause-classification-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured analysis reports; Markdown tables for history listings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include likely cause, confidence, secondary causes, audio feature summary, soothing suggestions, and report links; results are not medical diagnoses.]

## Skill Version(s):

1.0.16 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
