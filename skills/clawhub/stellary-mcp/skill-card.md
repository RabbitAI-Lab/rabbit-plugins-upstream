## Description:

Use Stellary, the AI-native project piloting SaaS, through its hosted remote MCP to discover projects, boards, cards, documents, cockpit state, and governed agent missions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[anymfah](https://clawhub.ai/user/anymfah)

### License/Terms of Use:

MIT

## Use Case:

Developers, operators, and AI-agent users use this skill to connect assistants to Stellary's hosted MCP service, inspect project-management context, and perform governed project actions within the user's token scopes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Stellary token could expose project data or allow changes beyond the user's intent.

Mitigation: Use a dedicated expiring token, start with read-only scopes such as projects:read and pilotage:read, add write scopes only when required, and revoke the token if exposed.

Risk: The remote MCP can access live Stellary workspace data and may perform write actions when token scopes allow it.

Mitigation: List projects and inspect exact project, card, and document IDs before writes, and confirm user intent before creating, moving, assigning, or completing work.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/Anymfah/stellary-mcp)
- [Stellary MCP documentation](https://stellary.co/docs/mcp/)
- [Official MCP Registry listing](https://registry.modelcontextprotocol.io/v0.1/servers/io.github.Anymfah%2Fstellary-project-management/versions/latest)
- [ClawHub skill page](https://clawhub.ai/anymfah/skills/stellary-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce MCP client configuration snippets that reference STELLARY_TOKEN rather than embedding secrets.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
