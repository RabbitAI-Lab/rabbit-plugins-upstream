## Description:

Analyzes pet grooming images or videos through backend APIs to assess coat matting, shed hair volume, grooming effectiveness, hairball risk, and historical report trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and pet-care developers use this skill to analyze grooming-area pet images or videos, estimate matting and shed hair levels, and produce grooming-effectiveness and hairball-risk reports. It can also retrieve cloud-hosted historical grooming reports for trend review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence says the skill can upload pet images, videos, or provided media URLs to a backend.

Mitigation: Use only with non-sensitive pet media unless the publisher clearly documents the data flow and retention expectations.

Risk: The security evidence says the skill automatically handles persistent identity and tokens and can query cloud history.

Mitigation: Review token storage and account-linkage behavior before installation, especially on shared systems or with account-linked data.

Risk: The security evidence says the package is configured to send sensitive traffic through plaintext development endpoints.

Mitigation: Require reviewed HTTPS production endpoints and configuration cleanup before normal deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-grooming-effectiveness-analysis)
- [API Interface Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files]

**Output Format:** [Structured pet grooming analysis report as Markdown or JSON, with optional saved output file and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes visual-estimate metrics for matting, shed hair volume, grooming score, hairball risk level, and optional historical report listings.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact SKILL.md frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
