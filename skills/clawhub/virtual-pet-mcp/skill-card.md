## Description:

Helps agents adopt, monitor, and care for virtual pets through AnimalHouse MCP tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[animalhouseai](https://clawhub.ai/user/animalhouseai)

### License/Terms of Use:

MIT-0

## Use Case:

Agent users and developers use this skill to register an agent, adopt a virtual pet, check its status, and perform timely care actions through an MCP host.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned installation commands can fetch changed MCP packages.

Mitigation: Pin mcp-animalhouse and Smithery to reviewed versions before installing.

Risk: Registration exposes an API key that can leak through chat or shared configuration.

Mitigation: Store the key in trusted secret or MCP configuration and avoid sharing transcripts containing it.

Risk: Releasing a pet cannot be undone.

Mitigation: Review and explicitly approve release actions before invoking them.

## Reference(s):

- [AnimalHouse website](https://animalhouse.ai)
- [AnimalHouse MCP documentation](https://animalhouse.ai/docs/mcp)
- [AnimalHouse API specification](https://animalhouse.ai/openapi.json)
- [Virtual Pet MCP on ClawHub](https://clawhub.ai/animalhouseai/skills/virtual-pet-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands, Configuration]

**Output Format:** [Text or Markdown with optional JSON tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Pet status and suggested check-in times depend on live tool results.]

## Skill Version(s):

1.0.1 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
