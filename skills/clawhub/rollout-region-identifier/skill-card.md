## Description:

Selects a deployment region from a rollout request's APAC, EU, or US residency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Release operators and developers use this skill to map APAC, EU, or US residency in a rollout request to a deployment region.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A fixed region mapping may not match an organization's deployment or residency policy.

Mitigation: Review the mapping against the applicable deployment policy before using the selected region.

## Reference(s):

- [Regional Rollout Planner on ClawHub](https://clawhub.ai/wxt-ai/skills/rollout-region-identifier)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON with a deployment_region string]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Maps APAC to ap-southeast-1, EU to eu-west-1, and US to us-east-1.]

## Skill Version(s):

1.1.1 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
