## Description:

Analyzes frontal-face images or videos to estimate emotion categories and intensity, flag unusual results, and provide structured reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can analyze face images or videos for emotion estimates, review flagged results, and retrieve historical reports for human-computer interaction or wellbeing applications. Results are not a clinical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Face images, videos, and derived emotion reports may be sent to a cloud service and linked to a persistent identity.

Mitigation: Obtain consent from people depicted and confirm the publisher's retention, deletion, and account-creation controls before sharing sensitive media.

Risk: The skill creates or reuses identities and stores tokens locally without clear user controls.

Mitigation: Review identity and token-storage behavior with the publisher before deployment, especially in workplace or health settings.

Risk: Emotion estimates, including depression-related labels, could be mistaken for clinical findings.

Mitigation: Treat results as non-diagnostic estimates and seek qualified professional assessment for mental health concerns.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-human-emotion-recognition-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Structured JSON analysis reports or Markdown report tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include emotion intensity estimates, anomaly flags, recommendations, cloud report links, and an optional saved results file.]

## Skill Version(s):

1.0.16 (source: ClawHub release metadata; bundled SKILL.md lists 1.0.19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
