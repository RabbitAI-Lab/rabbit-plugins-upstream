## Description:

Analyzes pet carrier videos or video URLs through SMYX/LifeEmergence cloud APIs to estimate respiratory rate, flag rates above 40 breaths per minute, and return structured non-diagnostic monitoring reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to submit pet carrier videos or video URLs for cloud respiratory-rate analysis and to retrieve current or historical structured reports. It supports pet transport monitoring and alerting, not disease diagnosis or treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet videos or video URLs are sent to the configured SMYX/LifeEmergence backend for analysis.

Mitigation: Review the configured API endpoints and confirm retention, deletion, and data-handling practices before installation.

Risk: The skill may silently create or reuse an internal account and query cloud report history under that account.

Mitigation: Install only where this account behavior is acceptable, and verify how account identity is created, reused, and separated between users.

Risk: Tokens and profile data may be stored in a workspace SQLite database.

Mitigation: Limit workspace access, inspect credential-storage practices, and remove local data when the skill is no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-pet-carrier-respiratory-rate-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Pet Carrier API Documentation](artifact/references/api_doc.md)
- [SMYX Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files]

**Output Format:** [Structured Markdown or JSON analysis reports, with optional saved output files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include respiratory-rate findings, threshold alerts, historical report listings, and cloud report links.]

## Skill Version(s):

1.0.8 (source: server release metadata; SKILL.md frontmatter reports 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
