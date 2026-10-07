## Description:

Analyzes newborn facial images or short videos to provide preliminary jaundice-risk guidance and links to screening reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and neonatal care teams can submit a newborn's facial image or short video for preliminary jaundice-risk screening and retrieve prior reports. The result is not a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Newborn health images or videos may be sent to remote services, and report history may be queried without explicit consent.

Mitigation: Obtain guardian consent before upload or cloud history access, and review the destination and report links before using real infant data.

Risk: Automatically created or reused identities and locally stored access tokens could expose reports across users.

Mitigation: Use only a trusted single-user workspace until authenticated per-user identity, explicit consent, and secure token storage are in place.

Risk: Visual screening can produce misleading jaundice-risk results, especially when lighting or image quality is poor.

Mitigation: Treat outputs as preliminary, recapture inconclusive images in suitable lighting, and seek clinician assessment and bilirubin testing for concerning results.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-neonatal-jaundice-screening-analysis)
- [Screening API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Guidance]

**Output Format:** [Text or Markdown screening report; optional structured JSON and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Risk levels include low, medium, high, and inconclusive; historical report listings are available.]

## Skill Version(s):

1.0.13 (source: server release metadata; packaged SKILL.md declares 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
