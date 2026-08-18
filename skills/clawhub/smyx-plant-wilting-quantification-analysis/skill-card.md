## Description:

Quantifies plant wilting severity from plant images or videos and can use soil-moisture context to help distinguish underwatering from overwatering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and plant-care operators can use this skill to analyze full-plant media from smart pots, fixed cameras, home gardens, greenhouses, or plant factories. It produces a wilting score, likely cause, intervention direction, and optional history reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded plant images, videos, and media URLs may be sent to a remote analysis service.

Mitigation: Review media sensitivity before use and avoid submitting private or regulated content unless the remote service and data handling are approved.

Risk: The skill silently creates or reuses internal identities and stores service token or user data locally.

Mitigation: Review local workspace storage before deployment, scope credentials appropriately, and clear stored identity data when sharing or rotating workspaces.

Risk: Default development HTTP endpoints and hidden account/token handling may be unexpected in production use.

Mitigation: Confirm the configured endpoints, transport security, and account behavior before installing or using the skill with private media.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-plant-wilting-quantification-analysis)
- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON text containing structured analysis results, report links, and history-list output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a report export URL and optional file output when the skill is run with an output path.]

## Skill Version(s):

1.0.12 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
