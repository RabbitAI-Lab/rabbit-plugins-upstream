## Description:

Analyzes medication-area images or video to detect pick-up, to-mouth, and swallow steps, then reports whether an elderly person's medication action appears completed or missing steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Care teams, family caregivers, and elder-care system developers use this skill to review medication-area media and receive structured compliance findings for pick-up, to-mouth, and swallow actions. The output supports follow-up checks and reporting, not medical prescribing or dosage decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive medication-area video or identifiers may be sent to remote cloud services.

Mitigation: Use only with informed consent, verify the configured endpoints and data-handling terms, and avoid deployment where remote processing of health-related media is not acceptable.

Risk: Persistent identities, local tokens, and automatic history access may expose sensitive care records.

Mitigation: Review token storage and history-access behavior before deployment, restrict local file access, and clear credentials where retention is not approved.

Risk: Packaged dev or private HTTP endpoints may route data to unintended services.

Mitigation: Replace or disable dev/private endpoints before use and confirm production endpoint ownership and transport security.

## Reference(s):

- [API Documentation](references/api_doc.md)
- [Supplemental API Documentation](skills/smyx_analysis/references/api_doc.md)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-elderly-medication-compliance-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, configuration]

**Output Format:** [Markdown and JSON-like structured analysis text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include detected medication steps, compliance status, missing steps, confidence, event time, snapshot/report links, and alert text.]

## Skill Version(s):

1.0.9 (source: ClawHub release metadata; artifact frontmatter states 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
