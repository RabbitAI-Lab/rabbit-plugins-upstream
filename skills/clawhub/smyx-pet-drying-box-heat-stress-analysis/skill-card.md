## Description:

Analyzes pet drying-box videos for panting, tongue color, and movement to report possible heat-stress signals, risk levels, and intervention guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, groomers, and veterinary staff can submit drying-box videos or URLs to identify possible heat-stress signs and receive a risk assessment and suggested cooling or stopping actions. The skill also supports retrieving prior analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet videos or video URLs are sent to a configured cloud service.

Mitigation: Use the skill only when you are comfortable sharing the video with that service; review its data handling before uploading sensitive footage.

Risk: Stored identities and reusable tokens can expose cloud report history in shared workspaces.

Mitigation: Avoid shared or multi-user workspaces unless identity and report-history access are isolated per user or session.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-pet-drying-box-heat-stress-analysis)
- [Skill API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance]

**Output Format:** [Structured analysis report and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports observed signs and heat-stress risk levels; supports report-history queries.]

## Skill Version(s):

1.0.12 (source: server-resolved ClawHub release; artifact frontmatter lists 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
