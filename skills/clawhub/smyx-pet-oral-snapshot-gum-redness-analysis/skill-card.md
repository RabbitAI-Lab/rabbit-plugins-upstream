## Description:

Analyzes pet mouth photos or videos for visible gum color and tartar coverage, returning structured observations to support early awareness without diagnosing disease.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and teams building pet cameras, smart pet products, or pet health platforms use the skill to review oral snapshots and receive observations about visible gum color and tartar coverage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media may still be uploaded even when export-only behavior is requested, and the selected API address may be ignored.

Mitigation: Avoid private footage until these options are fixed; confirm the receiving service and its retention practices before sending media.

Risk: The workspace database may contain login tokens.

Mitigation: Restrict access to the workspace database and protect any stored tokens.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Text, Markdown, Guidance]

**Output Format:** [Structured oral-health observations as JSON or text; historical reports may be presented as Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include visible gum color, redness level, estimated tartar coverage, care guidance, and report links; results are not a diagnosis.]

## Skill Version(s):

1.0.17 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
