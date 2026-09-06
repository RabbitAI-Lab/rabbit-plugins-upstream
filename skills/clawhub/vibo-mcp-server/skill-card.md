## Description:

ViBo MCP provides local-first memory for AI agents over MCP, including persistent memory, semantic recall, thread memory, and local storage with explicit user consent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vnbochkarev-netizen](https://clawhub.ai/user/vnbochkarev-netizen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to configure an MCP memory server that lets supported clients store, search, and manage local memory with a ViBo license key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill configures a third-party npm package as a persistent MCP server with access to a ViBo license key and local memory files.

Mitigation: Pin and audit the exact package version before installation, avoid recurring unpinned npx resolution in client configuration, and run it with least-privileged local file access.

Risk: The skill stores user-provided facts and thread history in local memory files.

Mitigation: Ask for explicit consent before storing facts or thread history, tell users what will be stored, and provide deletion or wipe instructions.

Risk: The security verdict is suspicious because installation guidance relies on unpinned npm execution in persistent client configuration.

Mitigation: Review the package supply chain and client configuration before use, and install only when the user accepts the third-party server risk.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vnbochkarev-netizen/skills/vibo-mcp-server)
- [ViBo site](https://wwwvibo.com)
- [ViBo memory docs](https://github.com/vnbochkarev-netizen/ViBo-memory)
- [Installation guide](artifact/INSTALL.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash and JSON configuration blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces installation and MCP client configuration guidance; the configured server exposes memory search, memory add, usage, and thread memory tools.]

## Skill Version(s):

0.2.5 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
