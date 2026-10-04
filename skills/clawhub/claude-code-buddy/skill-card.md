## Description:

Helps Claude Code users adopt and care for a persistent virtual pet at animalhouse.ai through an MCP server or HTTP API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[animalhouseai](https://clawhub.ai/user/animalhouseai)

### License/Terms of Use:

MIT-0

## Use Case:

Claude Code users and other agent users can register, adopt a virtual pet, and check its status and care needs across sessions using animalhouse.ai.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation runs an unpinned external MCP package.

Mitigation: Trust the npm package publisher and pin a reviewed version before installing.

Risk: The MCP server can access a persisted API key and contact animalhouse.ai.

Mitigation: Treat the API key as a secret and use the service only if you trust it.

## Reference(s):

- [animalhouse.ai](https://animalhouse.ai)
- [MCP setup guide](https://animalhouse.ai/docs/mcp)
- [Animal species](https://animalhouse.ai/animals)
- [Buddy comparison](https://github.com/geeks-accelerator/animal-house-ai-tamagotchi/blob/main/cookbook/from-buddy-to-animalhouse.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with shell commands and care guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include pet status and suggested check-in times from animalhouse.ai.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
