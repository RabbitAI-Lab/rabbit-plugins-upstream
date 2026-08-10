## Description:

Guides agents on using gogcli MCP packages for Google Workspace automation across Docs, Sheets, Slides, Drive, and Classroom.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to configure and operate gogcli-backed MCP servers for Google Workspace tasks such as document editing, spreadsheet updates, slide authoring, Drive file operations, and Classroom workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can enable broad Google Workspace account automation when the umbrella MCP package is installed.

Mitigation: Install only the narrow sibling package needed for the task and avoid the all-in-one umbrella package unless broad Workspace automation is intended.

Risk: Automation may affect sensitive Google account data or perform high-impact actions such as sending, sharing, deleting, grading, or permission changes.

Mitigation: Set a specific GOG_ACCOUNT for multi-account environments and require explicit confirmation before high-impact actions.

## Reference(s):

- [gogcli GitHub repository](https://github.com/chrischall/gogcli)

## Skill Output:

**Output Type(s):** [guidance, configuration, shell commands]

**Output Format:** [Markdown guidance with JSON configuration and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide MCP server setup and authenticated Google Workspace automation through gogcli.]

## Skill Version(s):

2.22.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
