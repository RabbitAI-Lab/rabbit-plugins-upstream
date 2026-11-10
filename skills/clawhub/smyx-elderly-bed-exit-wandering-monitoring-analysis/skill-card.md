## Description:

Identifies abnormal behaviors such as getting out of bed at night, prolonged wandering, and remaining motionless for extended periods, for night-time safety monitoring in nursing homes and for elderly people living alone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers in nursing homes and families of older adults can use the skill to review nighttime camera footage for bed exits, prolonged wandering, and extended immobility, and to obtain structured reports and historical report links. Treat findings as care guidance and have a person check any alert or suspected incident.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The supplied security assessment rates the release suspicious with high confidence because reported behavior and sensitive-data access exceed its stated monitoring purpose.

Mitigation: Consider not installing until the publisher substantiates account registration, credential handling, destination controls, and video-upload behavior, and explains why export-only does not prevent analysis.

Risk: Security assessment coverage is incomplete because a referenced local path was missing.

Mitigation: Review the missing path and complete the assessment before relying on this release.

## Reference(s):

- [API interface documentation](artifact/references/api_doc.md)
- [Analysis API reference](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-elderly-bed-exit-wandering-monitoring-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured analysis results and Markdown report lists with recommendations and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings are for care reference and require human confirmation.]

## Skill Version(s):

1.0.22 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
