## Description:

Helps agents research onchain tooling, assess project records, plan agent stacks, and cite agent-economy measurements using Sato Hub.

This skill is ready for commercial/non-commercial use.

## Publisher:

[satohubai](https://clawhub.ai/user/satohubai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can find and compare onchain-agent components, check project and agent records, plan integrations, and explain cited adoption figures. Some available tools also prepare crypto transactions or submit information, so confirm those actions before use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill's read-only description conflicts with write-capable crypto routing, watch subscription, project submission, and agent registration tools.

Mitigation: Require explicit confirmation before preparing swap transactions or launch routes, subscribing to watches, submitting projects, or registering agents; review transactions before signing.

Risk: Outbound Sato Hub access can disclose personal email, wallet details, or transaction details and may result in their storage.

Mitigation: Grant network access only if acceptable and avoid sharing sensitive details unless you accept Sato Hub receiving and possibly storing them.

## Reference(s):

- [Sato Hub skill release](https://clawhub.ai/satohubai/skills/sato-hub)
- [Sato Hub MCP documentation](https://satohub.ai/mcp)
- [Sato Hub MCP endpoint](https://satohub.ai/api/mcp)
- [Tool reference](references/tools.md)
- [REST reference](references/rest.md)
- [Worked examples](references/examples.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands, Configuration]

**Output Format:** [Markdown or text with citations, structured query results, and optional commands or configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cite the canonical Sato Hub record; distinguish project scores and preflight verdicts from security guarantees.]

## Skill Version(s):

1.1.2 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
