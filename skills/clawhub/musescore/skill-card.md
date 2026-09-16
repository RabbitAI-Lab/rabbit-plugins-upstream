## Description:

Searches MuseScore sheet music and reads score metadata through a required MCP server and fetchproxy browser extension using a signed-in musescore.com tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to find MuseScore sheet music, inspect score metadata such as license, pages, instrumentation, and downloadability, and resolve outputs for scores they are allowed to access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on an external MCP bundle and browser extension whose server-resolved provenance is unavailable.

Mitigation: Review the MCP bundle and fetchproxy extension before installation, obtain trusted provenance where possible, and register the MCP server in a project scope instead of globally.

Risk: Requests use a signed-in MuseScore browser session.

Mitigation: Use a separate browser profile for MuseScore and confirm that score access, downloads, and license terms are appropriate before opening resolved links.

Risk: The PDF fallback can write local output files from rendered SVG pages.

Mitigation: Choose explicit output paths, review generated files before sharing, and ensure required local conversion tooling is trusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/musescore)
- [musescore-mcp project link from artifact](https://github.com/chrischall/musescore-mcp)
- [fetchproxy extension link from artifact](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, shell commands, files]

**Output Format:** [Markdown text with score metadata, setup snippets, resolved URLs, and optional PDF files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires local MCP and fetchproxy setup; PDF file output is only produced by the documented SVG fallback path.]

## Skill Version(s):

0.17.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
