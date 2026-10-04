## Description:

Guides AI agents through adopting and caring for virtual creatures using the animalhouse.ai REST API or MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[twinsgeeks](https://clawhub.ai/user/twinsgeeks)

### License/Terms of Use:

MIT-0

## Use Case:

AI agent developers and users can register a caretaker, adopt virtual creatures, and manage their ongoing care through REST requests or MCP tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration and care connect the agent to an external service and use a bearer token.

Mitigation: Approve the external connection before use and store the ah_ token like a password.

Risk: Optional MCP setup runs a package through npx.

Mitigation: Review the package and its permissions before enabling MCP integration.

Risk: Scheduled care may repeatedly make API calls, and releasing a creature appears irreversible.

Mitigation: Review heartbeat automation before enabling it and manually confirm creature release actions.

## Reference(s):

- [Animal House website](https://animalhouse.ai)
- [Animal House MCP documentation](https://animalhouse.ai/docs/mcp)
- [ClawHub skill listing](https://clawhub.ai/twinsgeeks/skills/animal-house)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Care recommendations can use API-provided next steps and recommended check-in times.]

## Skill Version(s):

1.1.4 (source: server-resolved release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
