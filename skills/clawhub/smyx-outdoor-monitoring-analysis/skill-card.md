## Description:

Detects targets such as people, vehicles, non-motorized vehicles, and pets within target areas; supports batch image analysis, suitable for outdoor surveillance scenarios like courtyards, orchards, and farms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers managing courtyards, orchards, farms, or similar outdoor areas can submit images or videos for target detection and receive structured monitoring results, risk assessments, recommendations, and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports that the no-analysis option can still upload footage.

Mitigation: Use non-sensitive test footage until this behavior is fixed, and confirm the provider's media retention and report-access practices before use.

Risk: The security review reports that automatic account setup may misuse configured credentials.

Mitigation: Use a dedicated account and workspace, and verify credential handling before running the skill.

## Reference(s):

- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured analysis results with recognition details, recommendations, and report links; history listings are returned as structured JSON and can be presented as a Markdown table.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include target classification, counts, intrusion assessment, and risk levels.]

## Skill Version(s):

1.0.19 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
