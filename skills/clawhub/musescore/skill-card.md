## Description:

Search MuseScore sheet music and read score metadata via MCP. Triggers on phrases like "find sheet music for", "search MuseScore for", "is there a free arrangement of", "what's the license on this MuseScore score", "how many pages is", or any request involving MuseScore scores, arrangements, or sheet-music metadata. Requires musescore-mcp installed and the fetchproxy extension active with a signed-in musescore.com tab (see Setup).

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to search MuseScore sheet music, inspect score metadata, resolve download links for free or entitled scores, and convert score-related SVG or PDF assets when the required local MCP and browser bridge are configured.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The required MCP server and browser extension are private or unpinned components that operate through a signed-in MuseScore browser session.

Mitigation: Install only trusted, pinned, or otherwise verified copies, and confirm that using the signed-in session is acceptable for the intended environment.

Risk: Downloads and score-to-PDF conversion may resolve external download URLs or write local PDF files despite read-only claims elsewhere in the artifact.

Mitigation: Require user confirmation before opening download links or running local file conversion, and prefer project-scoped MCP configuration over global registration.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/musescore)
- [musescore-mcp source reference](https://github.com/chrischall/musescore-mcp)
- [fetchproxy extension reference](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return MuseScore metadata, official download URLs, MCP configuration snippets, healthcheck guidance, and local PDF output paths when conversion is used.]

## Skill Version(s):

0.17.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
