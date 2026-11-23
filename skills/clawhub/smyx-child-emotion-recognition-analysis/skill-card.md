## Description:

Using fixed cameras and optional microphones at home or in kindergartens, this skill analyzes a child's facial expressions, cry-sound features, and body movement to identify a typical emotional state.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, caregivers, and teachers can use the skill to review child video or optional audio and receive a structured emotion summary with directional soothing prompts. Results are a communication aid, not a psychological diagnosis or clinical advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment marks the skill suspicious because scanners report account and credential handling and broad credentialed network requests that are not clearly supported by its stated child emotion analysis purpose.

Mitigation: Review the service destinations and credential use before installation; limit credentials to the minimum required and avoid sharing account access.

Risk: Child recordings may contain sensitive personal data and are sent to a remote service; the service's retention and access practices may not fit your needs.

Mitigation: Obtain guardian consent, minimize recordings sent, and confirm the service's data retention and access controls before use.

Risk: The security scan was partial because a local reference was missing, so the assessment is incomplete.

Mitigation: Complete a review of the full release and its network and credential behavior before installing.

## Reference(s):

- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-child-emotion-recognition-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Text, Guidance]

**Output Format:** [Structured emotion analysis results in JSON or text, with optional Markdown report listings and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include emotion category, confidence, intensity, duration, alerts, and soothing prompts; results are reference information and not a diagnosis.]

## Skill Version(s):

1.0.40 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
