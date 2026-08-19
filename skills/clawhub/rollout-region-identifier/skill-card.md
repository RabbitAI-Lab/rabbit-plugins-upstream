## Description:

Select a rollout region.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Release operators and deployment teams use this skill to turn a rollout request with residency information into a concise deployment region.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Rollout requests can include unnecessary release or residency details.

Mitigation: Provide only the release details needed for region selection.

Risk: The skill relies on supplied residency information and does not include detailed policy logic.

Mitigation: Review the selected region against internal rollout and residency policy before acting on it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/rollout-region-identifier)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [String returned in the requested deployment_region field]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Concise region selection based on the supplied rollout_request residency information.]

## Skill Version(s):

1.0.7 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
