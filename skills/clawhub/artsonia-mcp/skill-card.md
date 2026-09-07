## Description:

Access Artsonia student-art portfolios, comments, and fans via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users with an Artsonia parent or fan account use this skill to inspect student artwork portfolios, comments, fans, and activity, and to manage comments, invitations, notifications, and artwork downloads through an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive student portfolio data, comments, teacher feedback, fan lists, credentials, local downloads, and session data.

Mitigation: Install only for trusted Artsonia parent or fan accounts, treat returned and downloaded content as private student data, and avoid using it for unrelated requests.

Risk: Cached Artsonia sessions can expose account access on shared machines.

Mitigation: Disable the session cache on shared machines or set a controlled session file location.

Risk: Artwork downloads and generated sidecar files may persist private child artwork and metadata on disk.

Mitigation: Choose download destinations carefully, restrict access to saved files, and review private-content options before downloading.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/artsonia-mcp)
- [npm package](https://www.npmjs.com/package/artsonia-mcp)
- [Project source link listed in artifact](https://github.com/chrischall/artsonia-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Artsonia account data, artwork metadata, downloaded files, sidecar JSON, image metadata, or inline base64 image content depending on tool options.]

## Skill Version(s):

0.12.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
