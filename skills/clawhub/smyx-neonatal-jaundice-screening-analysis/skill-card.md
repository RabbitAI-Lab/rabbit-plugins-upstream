## Description:

Analyzes newborn face images or short videos for visual jaundice indicators and returns a non-diagnostic low, medium, high, or inconclusive risk hint with suggested next steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, caregivers, and clinical support teams use this skill to submit newborn face images or short videos for non-diagnostic visual jaundice risk screening, history lookup, and follow-up guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends sensitive newborn face images or videos, related metadata, and account identifiers to a LifeEmergence cloud service.

Mitigation: Use only with explicit guardian consent, appropriate privacy controls, and approval for cloud processing of infant media and identifiers.

Risk: The skill silently creates and persists local identity or token records for future report history lookup.

Mitigation: Review local credential storage behavior before deployment and restrict access to generated identity or token records.

Risk: Visual jaundice screening can be affected by lighting, filters, image quality, and other capture conditions.

Mitigation: Treat outputs as screening hints only and require clinical bilirubin confirmation, especially for medium or high risk results.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-neonatal-jaundice-screening-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown report or JSON result with risk level, confidence, recommendations, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save an output file when requested; results are non-diagnostic visual screening hints.]

## Skill Version(s):

1.0.8 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
