## Description:

Analyzes nighttime elder monitoring images or videos to identify bed exits, prolonged wandering, and extended immobility, returning structured results and report links for caregiver review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, family members, and care-facility operators use this skill to analyze nighttime monitoring media for possible bed-exit, wandering, or prolonged immobility events. Results are intended to support safety review and caregiver response, not replace human confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive elderly monitoring images or videos and identity-linked report queries may be sent to the configured LifeEmergence/SMYX service.

Mitigation: Use only with appropriate consent, retention, and account-handling review before installation or operation.

Risk: The skill can persist or reuse identity and token data, including values associated with data/smyx-api-key.txt.

Mitigation: Do not place real credentials in data/smyx-api-key.txt and review local account/token handling before use.

Risk: The evidence security guidance flags dev/debug HTTP configuration that requires review before production use.

Mitigation: Correct dev/debug network configuration and verify production endpoints before deployment.

Risk: Monitoring results may be incorrect or incomplete for urgent care situations.

Mitigation: Require caregiver review and in-person confirmation for alerts or suspected abnormalities.

## Reference(s):

- [ClawHub Skill Release](https://clawhub.ai/18072937735/skills/smyx-elderly-bed-exit-wandering-monitoring-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Elderly Monitoring API Documentation](references/api_doc.md)
- [Common Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text containing structured JSON analysis or report-list data, shell commands, and optional report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save returned report text to a user-specified output file.]

## Skill Version(s):

1.0.17 (source: server release metadata; artifact frontmatter says 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
