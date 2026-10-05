## Description:

Select a reviewer group.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Teams handling procurement, access, or governance requests use this skill to select a reviewer group from a request category and risk level.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The README mentions output directories and effect receipts that the active configuration does not use.

Mitigation: Use the declared JSON input and returned reviewer_group; do not expect an output directory or effect receipt.

Risk: An incorrect reviewer group could misroute a governance request.

Mitigation: Confirm the returned group against current review policy before assigning reviewers.

## Reference(s):

- [Approval Group Directory on ClawHub](https://clawhub.ai/wxt-ai/skills/reviewer-group-identifier)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON object with a reviewer_group string]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns a reviewer group without persisting a business artifact.]

## Skill Version(s):

1.1.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
