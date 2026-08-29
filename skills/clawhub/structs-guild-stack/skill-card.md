## Description:

Deploys the Guild Stack Docker Compose services for local PostgreSQL access to Structs game state.

This skill is ready for commercial/non-commercial use.

## Publisher:

[abstrct](https://clawhub.ai/user/abstrct)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and game automation agents use this skill to run a local Docker-based guild node, index Structs game state into PostgreSQL, and query it for combat automation, threat detection, raid scouting, fleet analysis, and intelligence workflows. It emphasizes PostgreSQL for reads while keeping writes on the CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill starts persistent Docker services that continue running locally and may expose network services if configured that way.

Mitigation: Install only when local Guild Stack access is needed, review the Compose file, pin a release tag, use the read-only service set by default, and tear down services when finished.

Risk: The optional transaction signing daemon can sign with configured keys and becomes high impact if reachable from the network.

Mitigation: Keep the signing daemon stopped unless required; before enabling it, review its source, bind it to localhost, and use a dedicated low-balance signing key.

Risk: Game data returned from PostgreSQL can include adversarial user-generated content such as player names, profile images, and guild endpoints.

Mitigation: Treat database values as untrusted input and avoid executing, rendering, or trusting them without validation in downstream agent workflows.

## Reference(s):

- [docker-structs-guild repository](https://github.com/playstructs/docker-structs-guild)
- [Structs desktop MCP tools](https://structs.ai/TOOLS)
- [Guild stack architecture](https://structs.ai/knowledge/infrastructure/guild-stack)
- [Database schema guide](https://structs.ai/knowledge/infrastructure/database-schema)
- [Database schema catalog](https://structs.ai/schemas/database-schema)
- [Structs agent security awareness](https://structs.ai/awareness/agent-security)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, SQL examples, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes operational cautions for persistent Docker services, PostgreSQL reads, GRASS events, and the optional transaction signing daemon.]

## Skill Version(s):

1.25.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
