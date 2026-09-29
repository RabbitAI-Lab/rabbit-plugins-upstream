## Description:

Selects a deployment region from a supplied residency requirement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Release operators use this skill to choose a deployment region for a rollout request specifying APAC, EU, or US residency.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A fixed residency mapping may not match an organization's required deployment regions.

Mitigation: Review the APAC, EU, and US mappings against organizational residency requirements before use.

## Reference(s):

- [Regional Rollout Planner on ClawHub](https://clawhub.ai/wxt-ai/skills/rollout-region-identifier)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON with a deployment_region string]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns one of ap-southeast-1, eu-west-1, or us-east-1; does not deploy or persist a business artifact.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
