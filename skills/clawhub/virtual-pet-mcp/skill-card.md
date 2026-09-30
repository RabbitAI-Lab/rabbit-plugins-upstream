## Description:

Helps an agent adopt and care for virtual pets through animalhouse.ai MCP tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[animalhouseai](https://clawhub.ai/user/animalhouseai)

### License/Terms of Use:

MIT-0

## Use Case:

Agent users and developers use this skill to set up the AnimalHouse MCP server, adopt virtual pets, check their status and provide timely care.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an external MCP package without pinning may introduce unreviewed updates.

Mitigation: Pin the reviewed package version and review updates before upgrading.

Risk: The API key is saved locally and could be exposed on shared machines.

Mitigation: Protect or delete ~/.config/animalhouse/credentials.json on shared machines; do not paste the key into chat, and rotate it if exposed.

Risk: Releasing a creature is irreversible, and buying credits can incur charges.

Mitigation: Require host confirmation before destructive actions or paid credit flows.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/animalhouseai/skills/virtual-pet-mcp)
- [AnimalHouse homepage](https://animalhouse.ai)
- [AnimalHouse MCP documentation](https://animalhouse.ai/docs/mcp)
- [AnimalHouse API specification](https://animalhouse.ai/openapi.json)
- [mcp-animalhouse npm package](https://www.npmjs.com/package/mcp-animalhouse)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance and JSON MCP tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Care history can be returned as Markdown.]

## Skill Version(s):

1.0.2 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
