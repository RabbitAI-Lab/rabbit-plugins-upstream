## Description:

Analyzes children's video, with optional audio, to classify apparent emotions and provide non-clinical soothing prompts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Families and childcare staff can review child video or audio for apparent emotion, intensity, and possible soothing steps. Treat results as a communication aid, not a psychological diagnosis or clinical advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The export-only option can still upload children's recordings.

Mitigation: Wait for this behavior to be fixed before using sensitive recordings; confirm guardian authorization covers external processing and check the provider's retention and deletion terms.

Risk: The skill silently registers accounts and stores reusable credentials locally.

Mitigation: Protect the workspace credential database and restrict access to it.

Risk: The --api-url option may not change the upload destination.

Mitigation: Do not rely on --api-url to control where recordings are sent.

## Reference(s):

- [API interface reference](references/api_doc.md)
- [ClawHub release](https://clawhub.ai/18072937735/skills/smyx-child-emotion-recognition-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured JSON analysis with optional Markdown report listings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include emotion category, confidence, intensity, duration, alerts, soothing prompts, and report links; results are not a diagnosis.]

## Skill Version(s):

1.0.34 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
