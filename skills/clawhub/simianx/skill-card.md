## Description:

Provides stock and crypto research, market news and catalyst monitoring, and scheduled paper-position tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simianxai](https://clawhub.ai/user/simianxai)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and market researchers use this skill to examine US stock and crypto analysis, news, and sector catalysts, and to monitor scheduled analyses with simulated positions. Its outputs are informational, not investment advice; real trades require a separately authorized execution system.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic instruction updates could change how the skill behaves, and default account permissions may be broader than needed.

Mitigation: Review remote instruction updates before adopting them; restrict API keys to data:read and analysis:run unless additional permissions are needed, and set spending limits and an expiry.

Risk: Positions recorded in SimianX are simulated and do not establish that a separate real-world order was submitted or filled.

Mitigation: Treat SimianX positions as paper-only; route any real trades through a separately authorized execution system and verify execution there.

## Reference(s):

- [SimianX agent documentation](https://www.simianx.ai/agents)
- [SimianX API reference (OpenAPI)](https://service.simianx.ai/v1/openapi.json)
- [ClawHub skill release](https://clawhub.ai/simianxai/skills/simianx)
- [Autopilot guidance](references/autopilots.md)
- [Authentication guidance](references/auth.md)
- [Sector Watch guidance](references/sectors.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, JSON, PDF report]

**Output Format:** [Natural-language analysis and guidance, with JSON data and optional PDF research reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include entry, stop, and target levels; signals and simulated positions do not confirm execution of real trades.]

## Skill Version(s):

1.0.5 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
