## Description:

Access Artsonia student-art portfolios, comments, fans, notifications, and artwork downloads through an MCP server registered with the agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent work with Artsonia parent or fan account data, including student portfolios, artwork details, comments, fans, and notification preferences. It also supports local artwork downloads when the user intentionally requests retained files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run an external MCP package with Artsonia account credentials.

Mitigation: Pin and audit the artsonia-mcp package before use, keep credentials out of project files and source control, and restrict permissions on any MCP configuration or environment files.

Risk: The skill can persist sensitive student artwork data, comments, teacher feedback, metadata, and session state on disk.

Mitigation: Download or write metadata only when retention is intended, protect output directories, keep session cache files private, and disable or tightly control session caching when possible.

Risk: Artwork downloads may include private pieces unless the user opts out.

Mitigation: Use the skill's privacy-related download options intentionally, review outputs before sharing, and avoid retaining private artwork outside approved storage.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/artsonia-mcp)
- [npm package](https://www.npmjs.com/package/artsonia-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples and MCP tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local artwork image files, index manifests, metadata sidecars, or inline base64 image blocks depending on tool options and deployment mode.]

## Skill Version(s):

0.12.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
