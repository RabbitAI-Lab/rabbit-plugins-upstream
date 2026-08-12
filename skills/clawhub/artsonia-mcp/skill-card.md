## Description:

Access Artsonia student-art portfolios, comments, fans, downloads, and notification settings through an MCP-backed agent workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to Artsonia so it can help inspect student artwork, retrieve portfolios and comments, manage fans and notifications, and prepare local artwork downloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles Artsonia account credentials and student artwork.

Mitigation: Install and run the MCP server only on trusted machines, and use an Artsonia account appropriate for the intended access.

Risk: Comments, fan invitations, and notification changes can modify Artsonia social or account state.

Mitigation: Review write actions before sending them.

Risk: Downloaded artwork and metadata may persist on disk.

Mitigation: Choose download destinations carefully and handle generated image files, sidecars, and manifests as sensitive data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/artsonia-mcp)
- [artsonia-mcp npm package](https://www.npmjs.com/package/artsonia-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON configuration snippets, shell commands, and MCP tool guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference Artsonia account credentials, student artwork metadata, local file paths, and user-reviewed social actions.]

## Skill Version(s):

0.9.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
