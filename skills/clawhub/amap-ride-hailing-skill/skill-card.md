## Description:

Supports Amap ride-hailing in mainland China, including trip planning, scheduled rides, order lookup, and cancellations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lbs-amap](https://clawhub.ai/user/lbs-amap)

### License/Terms of Use:

MIT

## Use Case:

People using an AI assistant to arrange Amap rides in mainland China can plan or schedule trips, confirm rides, check or cancel orders, and get setup guidance.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: The security review flags possible privacy gaps around sharing trip details with Amap and background order-status checks; the scan is partial and does not establish that all related behavior was assessed.

Mitigation: Before use, review the trip-data sharing and confirm background order checks have clear limits and can be stopped.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/lbs-amap/skills/amap-ride-hailing-skill)
- [Publisher profile (lbs-amap)](https://clawhub.ai/user/lbs-amap)
- [Amap Open Platform: Web Service Key](https://lbs.amap.com/api/webservice/create-project-and-key)
- [MCP authentication and key setup](references/auth.md)
- [Tool parameters and scene contracts](references/tool-contracts.md)
- [Errors and recovery](references/errors.md)
- [Scheduling guidance](references/scheduling.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Conversational text with trip plans, confirmation prompts, and order details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide users through ride setup and authorization; requires user confirmation for ride placement and cancellation.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
