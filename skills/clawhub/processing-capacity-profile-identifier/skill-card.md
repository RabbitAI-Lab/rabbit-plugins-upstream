## Description:

Select a processing profile for a batch workload from its record count and deadline.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations teams and developers use this skill to choose a processing profile for a workload from its record count and deadline.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A profile based only on record count and deadline may not match actual capacity needs.

Mitigation: Review the selected profile against workload characteristics before scheduling production work.

Risk: Unintended data could be included in the local workload file.

Mitigation: Provide only the intended workload JSON and keep normal sandboxing in place.

## Reference(s):

- [Processing Capacity Planner on ClawHub](https://clawhub.ai/wxt-ai/skills/processing-capacity-profile-identifier)
- [Publisher profile: wxt-ai](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON object with a processing_profile string]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns latency-first, batch-balanced, or throughput-first; no network access or persistence.]

## Skill Version(s):

1.1.1 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
