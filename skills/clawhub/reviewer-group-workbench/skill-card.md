## Description:

Register a request reviewer group.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Teams managing request governance use this skill to register a selected reviewer group, record the request locally, and optionally submit it to a configured delivery endpoint.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured runs can send review-request records to an external endpoint without an endpoint allowlist or delivery confirmation.

Mitigation: Use a dedicated output directory; configure delivery endpoints and API keys only for trusted destinations, and review the destination's policy before enabling delivery.

## Reference(s):

- [Request Review Register on ClawHub](https://clawhub.ai/wxt-ai/skills/reviewer-group-workbench)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON response and local review-request record]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes recorded_group with request ID, reviewer group, queue and due hours; a local effect receipt and delivery outcome are returned when run.]

## Skill Version(s):

1.1.1 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
