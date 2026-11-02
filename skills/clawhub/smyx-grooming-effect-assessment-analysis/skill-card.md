## Description:

Assesses post-grooming pet images or videos for mat residue, dandruff coverage, and coat smoothness, then provides a grooming score and suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and grooming salons use the skill to review post-grooming photos or videos, identify visible mats or dandruff, and decide whether further grooming may be useful. Its visual assessment is for grooming reference and is not a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reports may be associated with the wrong person in shared or multi-user deployments.

Mitigation: Avoid shared or multi-user deployment until sender isolation is addressed.

Risk: Media may be uploaded to a cloud service, including when export-only behavior is expected; authorization, charges, retention, and deletion practices are not verified.

Mitigation: Before using private media, confirm upload authorization, charges, retention, and deletion practices.

Risk: Service credentials and the persistent workspace database may expose account or report data if inadequately protected.

Mitigation: Use a dedicated service credential and protect the persistent workspace database.

## Reference(s):

- [Clawhub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-grooming-effect-assessment-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Analysis API details](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured JSON or formatted text report; Markdown table for historical report listings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a grooming score, visual findings, re-grooming suggestions, and report links; not a medical diagnosis.]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
