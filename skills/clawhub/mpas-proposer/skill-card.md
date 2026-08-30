## Description:

Allow any combination of agents, humans, or software to approve MCP tool calls that you flag. Prevent your agent from deleting your production database or violating compliance. Use this skill for agents that propose calls, not agents that approve calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oma3](https://clawhub.ai/user/oma3)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to make an agent propose protected MCP write operations through an MPAS approval bridge, wait for authorization, and report the final result without holding protected application credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Misconfigured bridge, maintainer identities, or notification channels could cause governed write operations to be routed or reviewed incorrectly.

Mitigation: Confirm the MPAS bridge, maintainer identities, and approved notification channel before installation and before using the skill for governed operations.

Risk: A proposing agent could accidentally create duplicate actions or misstate completion if it repeats tool calls or treats nonterminal approvals as execution success.

Mitigation: Track the original Action ID, use the appropriate Tasks or compatibility wait flow, and report success only after receiving a terminal application result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oma3/skills/mpas-proposer)
- [Publisher profile](https://clawhub.ai/user/oma3)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline command and configuration references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides an agent to submit governed MCP actions once, track their authorization state, notify maintainers, and avoid self-approval or direct credentialed bypass paths.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
