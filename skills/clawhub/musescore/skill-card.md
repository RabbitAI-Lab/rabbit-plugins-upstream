## Description:

Helps agents search MuseScore sheet music, inspect score metadata, and obtain available score links or PDFs through a connected browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

MuseScore users and developers can ask an agent to find arrangements, check score details and licensing, and obtain available download links or PDFs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external MuseScore MCP server is private, and requests use a signed-in browser session.

Mitigation: Verify the MCP server and fetchproxy extension before installation; only enable them for intended MuseScore tasks.

Risk: A globally enabled MCP connection may be available beyond the intended project.

Mitigation: Prefer project-local MCP configuration where practical.

## Reference(s):

- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Text with score metadata and links; PDF files when supported]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Official download links require a free or entitled score; PDF creation may require local SVG conversion.]

## Skill Version(s):

1.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
