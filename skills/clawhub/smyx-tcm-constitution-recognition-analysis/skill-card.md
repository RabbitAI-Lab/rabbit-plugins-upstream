## Description:

Determines nine TCM constitution types including Yin deficiency, Yang deficiency, Qi deficiency, phlegm-dampness, and blood stasis through facial features and physical signs, and provides personalized health preservation and conditioning suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit face images or videos to a cloud service for TCM constitution analysis, receive constitution scores and health-preservation suggestions, and retrieve account-linked historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Face images or videos are sent to the configured cloud service for analysis.

Mitigation: Use the skill only with appropriate consent and data-handling review for biometric or health-adjacent media.

Risk: The skill can create or reuse a persistent user identity, store access tokens locally, and fetch account-linked analysis history.

Mitigation: Review local token storage, account-linking behavior, and history access before deployment.

Risk: The analysis provides health-preservation and conditioning suggestions that may be mistaken for medical diagnosis.

Mitigation: Present outputs as wellness reference material and direct users with symptoms or medical concerns to a qualified clinician.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-tcm-constitution-recognition-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Interface Documentation](references/api_doc.md)
- [Analysis API Error Reference](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown reports or JSON output from cloud API analysis, with optional saved output files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local image/video paths or public media URLs; supports jpg, jpeg, png, mp4, avi, and mov up to 10MB.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact SKILL.md frontmatter says 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
