## Description:

Accesses Artsonia student-art portfolios, comments, fans, artwork downloads, and notification settings through the artsonia MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, guardians, and authorized Artsonia account users use this skill to view student artwork, read activity and comments, manage fans, post comments, download artwork, and adjust notifications from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Artsonia account credentials and can access student-related artwork data, comments, feedback, and cached sessions.

Mitigation: Install only when that access is intended; keep credentials private, use a protected environment, and disable or relocate the session cache on shared machines or shared backups.

Risk: Downloaded student artwork, private pieces, embedded metadata, manifests, and sidecar files may contain sensitive information.

Mitigation: Store downloads in private folders, review private-piece settings before export, and limit sharing of generated files and metadata.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/artsonia-mcp)
- [npm package](https://www.npmjs.com/package/artsonia-mcp)
- [Source repository](https://github.com/chrischall/artsonia-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON configuration snippets, shell commands, and MCP tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local artwork files, image metadata, index manifests, and per-artwork JSON sidecars when download options are used.]

## Skill Version(s):

0.10.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
