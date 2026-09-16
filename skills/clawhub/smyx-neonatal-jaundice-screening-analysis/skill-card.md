## Description:

Provides visual, non-diagnostic neonatal jaundice pre-screening from newborn facial images or short videos, returning a risk level, confidence-related metrics, suggested next action, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers and healthcare users can use this skill to submit newborn face images or short videos for visual jaundice-risk pre-screening, historical report lookup, and suggested follow-up actions. It should be treated as screening support only, with medium or high risk confirmed by clinical bilirubin testing or a clinician.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive newborn images or videos may be uploaded to a remote service.

Mitigation: Use only with explicit guardian consent, documented backend ownership, retention controls, and appropriate privacy safeguards.

Risk: The security evidence flags broad or under-secured backend, identity, token storage, and network configuration.

Mitigation: Do not use for real infant health screening until production HTTPS endpoints, secure credential storage, and backend handling are reviewed and fixed by the publisher.

Risk: History retrieval and internal identity reuse can expose sensitive health report data if identity linkage is incorrect.

Mitigation: Verify user identity isolation and report-access controls before enabling report history queries.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-neonatal-jaundice-screening-analysis)
- [API Documentation](references/api_doc.md)
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown text or JSON report with jaundice risk level, visual feature metrics, suggested action, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes screening status, confidence-oriented fields, clinical follow-up guidance, and historical report listings when requested.]

## Skill Version(s):

1.0.11 (source: server release metadata; SKILL.md frontmatter: 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
