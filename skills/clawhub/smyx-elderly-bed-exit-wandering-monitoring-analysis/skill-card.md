## Description:

Analyzes nighttime monitoring media for bed exits, prolonged wandering, and extended immobility in elder-care settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers, nursing-home staff, and developers use this skill to analyze nighttime monitoring videos for possible bed exits, wandering, or immobility and to review past monitoring reports. Results support care decisions but do not replace an in-person check.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive elder-care videos, video URLs, analysis results, and report history are sent to cloud services.

Mitigation: Confirm resident consent, service account ownership, and the provider's retention practices before using real monitoring media.

Risk: The skill silently creates or reuses an identity and stores access tokens locally.

Mitigation: Review identity and token-storage expectations, restrict access to local credentials, and use only approved accounts.

Risk: Automated behavioral findings may be mistaken for a definitive safety or medical assessment.

Mitigation: Have caregivers verify concerning results in person and follow established care procedures.

## Reference(s):

- [Monitoring analysis API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-elderly-bed-exit-wandering-monitoring-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis report or JSON; Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include risk findings, recommendations, and report links.]

## Skill Version(s):

1.0.19 (source: release metadata; SKILL.md states 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
