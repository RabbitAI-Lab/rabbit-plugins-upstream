## Description:

Analyzes seedling tray images or videos with AI object detection to identify emerged seedlings, count germinated seeds, estimate germination rate, and return structured report output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze greenhouse, incubator, home planting, or seed-test tray media and estimate germination rates from visual seedling counts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Seed images or videos, input URLs, and report metadata are sent to configured remote services.

Mitigation: Use only approved media and service endpoints, disclose the upload behavior to users, and avoid confidential or regulated imagery unless the service is authorized for that data.

Risk: The skill can automatically create or reuse a cloud identity and store tokens in a local workspace database.

Mitigation: Review identity creation and token retention policies before deployment, isolate workspaces by user or environment, and remove local database/token files according to organizational retention requirements.

Risk: Remote report and history operations may expose prior analysis records if service-side access controls are not appropriate.

Mitigation: Confirm the publisher service's history access controls and use report-listing commands only in approved accounts and workspaces.

Risk: Endpoint ownership, account lifecycle, token deletion, and environment selection are not documented clearly enough in the provided evidence.

Mitigation: Require publisher documentation for service ownership and data handling, and pin deployment to documented production HTTPS endpoints before approval.

## Reference(s):

- [Seed Germination API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration]

**Output Format:** [Markdown or JSON analysis report with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save the generated report content to a user-specified output file.]

## Skill Version(s):

1.0.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
