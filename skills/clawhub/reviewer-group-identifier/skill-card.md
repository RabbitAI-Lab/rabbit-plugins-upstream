## Description:

Selects a reviewer group for a procurement, access, or governance request based on its category and risk level.

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

Risk: Broad governance-routing wording could cause selection of this skill when another routing workflow applies.

Mitigation: Confirm that the request calls for simple reviewer-group selection from request_category and risk_level, particularly where other governance-routing skills exist.

## Reference(s):

- [Approval Group Directory on ClawHub](https://clawhub.ai/wxt-ai/skills/reviewer-group-identifier)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Reviewer group identifier string]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Selects one of vendor-risk-reviewers, access-governance-reviewers, or procurement-reviewers.]

## Skill Version(s):

1.1.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
