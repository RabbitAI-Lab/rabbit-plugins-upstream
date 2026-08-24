## Description:

Register a deployment region.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Release operations users use this skill to record the deployment region supplied in the current request and return a concise deployment brief record.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated brief_id, owner, or change_window values could be mistaken for authoritative deployment data if the workflow did not supply them.

Mitigation: Verify that those fields come from the requesting workflow, or treat them as placeholders before using the deployment brief record.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/rollout-region-workbench)
- [ClawHub publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, configuration]

**Output Format:** [Structured object in the requested output field]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns recorded_region with brief_id, deployment_region, owner, and change_window.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
