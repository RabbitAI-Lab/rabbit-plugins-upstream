## Description:

Access your Vibo (vibodj.com) event music planning via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and event hosts use this skill to let an agent inspect and update Vibo event music plans, including timelines, song requests, playlists, guest participation, and exports to connected music services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup can require Vibo account credentials or captured browser tokens, including tokens saved in ~/.vibo-mcp/session.json.

Mitigation: Use a pinned, reviewed package version; avoid storing real passwords in project .mcp.json files; keep MCP configs containing secrets out of source control; and rotate or delete exposed Vibo tokens.

Risk: The recommended npx setup installs an unpinned MCP package at runtime.

Mitigation: Pin and review the package version before installing or deploying the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/vibo-mcp)
- [Vibo](https://vibodj.com)
- [npm package](https://www.npmjs.com/package/vibo-mcp)
- [Source link from artifact](https://github.com/chrischall/vibo-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples and MCP tool usage notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Mutating Vibo tools are described as confirm-gated dry runs unless confirm is explicitly true.]

## Skill Version(s):

1.8.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
