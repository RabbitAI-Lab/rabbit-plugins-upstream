## Description:

Analyzes pet cage floor images or videos to estimate feces and urine coverage, score cage cleanliness, trigger cleaning alerts, and return structured reports with report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External operators and developers use this skill to analyze cage floor media from boarding kennels, pet shops, animal hospitals, or breeding facilities and identify when waste coverage exceeds cleaning thresholds. It is intended for environmental hygiene management and does not provide medical diagnosis or treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media submitted for analysis is sent to the Life Emergence cloud service.

Mitigation: Enable the skill only where uploaded images or videos may be processed by that service, and review data-retention expectations before use in sensitive environments.

Risk: The skill can automatically create or reuse an account-linked identity, read a workspace identity file, and store tokens locally for future report access.

Mitigation: Administrators should review account provisioning and local token storage before enabling the skill in shared workspaces, and remove or revoke stored credentials when access should end.

Risk: Historical report queries return account-linked cloud report data.

Mitigation: Restrict use to users authorized to access those reports and review report-access controls before deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-cage-cleanliness-detection-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Cage Cleanliness API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Markdown or JSON-like structured text, with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cleanliness scores, waste coverage estimates, alerts, recommendations, history tables, and cloud report links.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter says 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
