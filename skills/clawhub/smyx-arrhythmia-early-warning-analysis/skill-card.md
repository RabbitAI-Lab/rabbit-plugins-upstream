## Description:

Analyzes facial videos for early-warning signs of abnormal heart rhythms, including premature beats, atrial fibrillation, tachycardia, and bradycardia.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

People seeking non-contact heart-health screening can use the skill to analyze a facial video and review early-warning results, recommendations, and past reports. It is not a substitute for an ECG or a clinician's diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive facial video or video URLs are sent to external analysis services.

Mitigation: Obtain informed consent and clarify where the media goes, how long it is retained, and how it can be deleted before use.

Risk: The skill silently creates or reuses an account identity, stores report/session tokens locally, and can access sensitive report history without an explicit confirmation step.

Mitigation: Require confirmation for history access, restrict account scope, protect local tokens, and establish deletion controls before processing sensitive data.

Risk: A screening result may be mistaken for a medical diagnosis.

Mitigation: Present results as early-warning information only; seek an ECG and clinician evaluation for concerning or high-risk findings.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-arrhythmia-early-warning-analysis)
- [Arrhythmia analysis API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured text reports and Markdown tables with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Analyzes local video or video URLs; supports MP4, AVI, and MOV files up to 10 MB and can retrieve past reports.]

## Skill Version(s):

1.0.20 (source: ClawHub release metadata; bundled skill frontmatter lists 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
