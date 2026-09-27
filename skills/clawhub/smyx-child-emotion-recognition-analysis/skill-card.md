## Description:

Analyzes children's video and optional audio to report likely emotions, intensity, alerts, and suggested soothing responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, caregivers, and educators use the skill to review child video and optional audio for possible emotional distress, view historical reports, and consider non-clinical soothing suggestions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Children's video, audio, and reports may expose sensitive private information through cloud processing or report access.

Mitigation: Require verified guardian or institutional authorization; use a trusted operator and documented consent, access, retention, and deletion controls before processing real child media.

Risk: Silent account creation and locally stored tokens may enable unintended account or report access.

Mitigation: Review authentication and token storage; bind accounts to verified identities and prevent caller-supplied identifiers from creating or impersonating accounts.

Risk: Emotion classifications and soothing suggestions can be mistaken for clinical assessments.

Mitigation: Treat results as non-diagnostic guidance and have caregivers review concerning or persistent symptoms with a qualified professional.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-child-emotion-recognition-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance]

**Output Format:** [Structured text or JSON; historical reports can be shown as Markdown tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include emotion category, intensity, confidence, duration, alerts, soothing hints, and report links.]

## Skill Version(s):

1.0.28 (source: ClawHub release metadata; bundled SKILL.md frontmatter says 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
