## Description:

Helps agents set up AnimalHouse MCP tools and adopt, check on, and care for a virtual pet.

This skill is ready for commercial/non-commercial use.

## Publisher:

[animalhouseai](https://clawhub.ai/user/animalhouseai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users can connect an MCP host to AnimalHouse, adopt a virtual pet, and manage its ongoing care through tool calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP package runs locally and stores an AnimalHouse API key on disk.

Mitigation: Install only if you trust the package; review or remove locally stored credentials on shared or synced machines.

Risk: Unversioned installation commands can fetch a newer, unreviewed package release.

Mitigation: Consider pinning mcp-animalhouse to a reviewed version.

Risk: Releasing a creature is irreversible.

Mitigation: Confirm the intended creature and obtain approval before using release_creature.

## Reference(s):

- [AnimalHouse](https://animalhouse.ai)
- [AnimalHouse MCP documentation](https://animalhouse.ai/docs/mcp)
- [AnimalHouse API specification](https://animalhouse.ai/openapi.json)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API calls]

**Output Format:** [Markdown instructions and JSON tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool responses include pet status and recommended check-in times.]

## Skill Version(s):

1.0.3 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
