## Description:

Analyzes newborn face images or video to provide a preliminary visual jaundice-risk indication and suggested follow-up, without replacing clinical testing or diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and care teams use the skill to screen newborn face images or short videos for possible jaundice and view preliminary risk guidance or past reports. Results are not a diagnosis and should not replace bilirubin testing or clinical assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive newborn face images or video URLs and report queries are sent to LifeEmergence cloud services.

Mitigation: Obtain guardian consent before use and confirm the publisher's data retention, deletion, and access practices.

Risk: The skill silently creates or reuses persistent identities and tokens with limited user-facing control.

Mitigation: Ask the publisher how identities are bound to accounts, how tokens are stored, and whether local identity data is encrypted before installation.

Risk: Visual screening can be inconclusive or misleading, especially with poor lighting or obscured facial features.

Mitigation: Treat output as preliminary guidance only; seek clinical assessment and appropriate bilirubin testing rather than relying on the result for diagnosis.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-neonatal-jaundice-screening-analysis)
- [API interface reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis text or JSON; historical reports may be presented in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preliminary risk indication, suggested follow-up, and report links when available]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
