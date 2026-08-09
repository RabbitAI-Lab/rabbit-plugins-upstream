## Description:

Access Artsonia student-art portfolios, comments, and fans via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an MCP-capable agent to Artsonia so it can list linked students, view portfolios and artwork details, download artwork, manage comments, check fans, invite fans, and update notification preferences.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Artsonia credentials are required for the MCP server and could be exposed if stored or run in an untrusted environment.

Mitigation: Run the server only on trusted machines and store the Artsonia password with secure secret storage rather than sharing it in project files.

Risk: Downloaded student artwork, comments, teacher feedback, and metadata may include private child-related data that can persist in local folders, backups, or shared directories.

Mitigation: Review download destinations before confirming exports and avoid shared or automatically backed-up folders unless that handling is intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/artsonia-mcp)
- [npm package: artsonia-mcp](https://www.npmjs.com/package/artsonia-mcp)
- [Source repository: chrischall/artsonia-mcp](https://github.com/chrischall/artsonia-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown with JSON configuration snippets, shell commands, and MCP tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return portfolio data, comments, fan information, downloaded artwork files, sidecar metadata, and index manifests depending on the invoked MCP tool.]

## Skill Version(s):

0.8.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
