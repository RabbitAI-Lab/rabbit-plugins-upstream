## Description:

Combines select a processing profile with register a queued processing profile.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations teams use this skill to select processing profiles for batch workloads, capacity planning, and recurring account-summary jobs, then record selected profiles for queued business-job handoffs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad workload-operations wording could activate the skill in contexts where a team expects narrower queue-registration behavior.

Mitigation: Review the trigger wording before deployment and ask the publisher to make activation language more specific if tighter routing is required.

Risk: Incorrect profile selection or recording could affect capacity-planning and scheduling handoffs.

Mitigation: Have operations staff review selected and recorded profiles before using them for queue ownership, tracking, or scheduling decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/processing-capacity-profile)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [Markdown or plain text describing selected and recorded processing profiles]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces processing_profile and recorded_profile values from workload notes and selected processing profiles.]

## Skill Version(s):

1.0.7 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
