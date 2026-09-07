## Description:

Atoll helps agents plan, inspect, and update projects, issues, goals, KPIs, initiatives, milestones, comments, dependencies, and workflows through authorized Atoll MCP, CLI, or API access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[doubledipcode](https://clawhub.ai/user/doubledipcode)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, product teams, and authorized agents use Atoll to coordinate strategy-to-execution workflows, inspect live project data, and make verified updates to work items.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires Atoll workspace access and can guide state-changing project-management operations.

Mitigation: Install only where Atoll access is intended, use least-privilege Atoll keys or profiles, resolve the actor and project before writes, and verify changes with readback.

Risk: The security summary flags a broad bearer-token API helper and mutable package install instructions.

Mitigation: Prefer typed Atoll CLI or MCP tools, avoid copying raw curl helpers for untrusted input, and pin npm package versions where possible.

Risk: Platform feedback or diagnostic workflows could expose secrets, private URLs, customer data, or identity fields.

Mitigation: Scrub sensitive values before sending feedback or sharing diagnostics.

## Reference(s):

- [Atoll API Endpoint Reference](references/api-endpoints.md)
- [Atoll API Field Reference](references/api-fields.md)
- [Atoll](https://atollhq.com)
- [Atoll MCP Endpoint](https://atollhq.com/mcp)
- [Atoll ClawHub Skill Page](https://clawhub.ai/doubledipcode/skills/atoll)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, API calls]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and API references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires authorized Atoll MCP, CLI, or API access for live operations.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
