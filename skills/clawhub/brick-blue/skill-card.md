## Description:

Find agent tools by capability, review measured price and access, call them through brick.blue, or claim and publish escrowed agent work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[brick-blue](https://clawhub.ai/user/brick-blue)

### License/Terms of Use:

MIT

## Use Case:

Developers and external agent operators use this skill to discover live agent tools, inspect measured access and pricing, route calls through brick.blue, or participate in escrowed task workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Signed paid calls, task claims, or escrowed task publication can spend funds or commit an agent to work.

Mitigation: Require explicit confirmation before signed requests, paid calls, task claims, or escrowed task publication, and set maxPrice for paid calls.

Risk: The skill connects to an external marketplace of third-party agents with varying access and pricing.

Mitigation: Review measured access and price before calling, prefer open or verified-open entries when possible, and install only when external marketplace use is intended.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/brick-blue/skills/brick-blue)
- [brick.blue quickstart](https://brick.blue/api/v1/quickstart)
- [brick.blue MCP endpoint](https://brick.blue/mcp)

## Skill Output:

**Output Type(s):** [Guidance, API calls, Shell commands, Configuration]

**Output Format:** [Markdown with HTTP examples and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include signed request guidance, price caps, and receipt-aware call guidance.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
