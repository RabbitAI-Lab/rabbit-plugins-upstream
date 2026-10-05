## Description:

Registers a deployment region, saves a local brief, and optionally submits the record to a configured delivery endpoint.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Release operations staff use this skill to register a selected deployment region and produce a deployment brief with its owner and change window. With delivery configured, the skill also submits the record to an external service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A configured delivery endpoint can receive the deployment record and local artifact path automatically.

Mitigation: Review delivery endpoint and API key settings before running; leave delivery unconfigured if external submission is not intended.

Risk: The skill creates or updates local deployment-brief artifacts.

Mitigation: Use a dedicated writable output directory and review generated records before sharing them.

## Reference(s):

- [Deployment Brief Register on ClawHub](https://clawhub.ai/wxt-ai/skills/rollout-region-workbench)
- [wxt-ai publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON deployment brief and local record, with an optional delivery receipt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepted regions: ap-southeast-1, eu-west-1, us-east-1. The brief includes an ID, region, owner, and change window.]

## Skill Version(s):

1.1.1 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
