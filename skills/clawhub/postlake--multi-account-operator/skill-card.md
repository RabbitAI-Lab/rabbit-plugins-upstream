## Description:

Multi-account social media operator for AI agents that helps operators publish and monitor high-volume social posts through PostLake while protecting account health.

This skill is ready for commercial/non-commercial use.

## Publisher:

[postlake](https://clawhub.ai/user/postlake)

### License/Terms of Use:

MIT-0

## Use Case:

External operators, agencies, portfolio managers, and agent builders use this skill to run many connected social accounts, schedule batches, read per-network PostLake results, distinguish platform restrictions from actionable failures, and apply guardrails before volume workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent may publish or schedule posts through PostLake for accounts the operator does not intend to expose.

Mitigation: Before running volume workflows, configure allowed profiles, allowed networks, daily caps, OAuth or scoped keys, and revocation controls.

Risk: High-volume retries or repeated posts can worsen platform restrictions or post to the wrong brand.

Mitigation: Cap retries, read per-target errors, pause restricted queues, lower cadence, vary captions, and review the scheduled queue before adding more posts.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/postlake/skills/multi-account-operator)
- [PostLake Documentation](https://docs.postlake.dev)
- [PostLake MCP Endpoint](https://api.postlake.dev/mcp)
- [PostLake Agent Keys](https://app.postlake.dev/app/keys)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands, API examples, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Focuses on operator decisions, account pacing, target-level error handling, and PostLake guardrails.]

## Skill Version(s):

1.0.1 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
