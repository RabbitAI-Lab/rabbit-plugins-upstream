## Description:

Search MuseScore sheet music and read score metadata via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search MuseScore scores, inspect sheet-music metadata, resolve entitled download links, and convert available score pages to PDF when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: MuseScore requests route through an external MCP and fetchproxy extension using the user's signed-in browser session.

Mitigation: Install only if this session routing is acceptable, and review the external musescore-mcp and fetchproxy code before use.

Risk: PDF conversion can write output to a user-selected local path.

Mitigation: Choose output paths carefully and keep generated PDFs in intended project or download directories.

Risk: The skill is specialized for MuseScore workflows and may be unsuitable for generic sheet-music tasks.

Mitigation: Invoke it only for MuseScore search, metadata, download-link, healthcheck, or PDF-conversion requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/musescore)
- [musescore-mcp repository](https://github.com/chrischall/musescore-mcp)
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Files, Guidance]

**Output Format:** [Markdown with score metadata, URLs, setup snippets, and optional PDF file output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [PDF output is only written when a score PDF conversion path is invoked.]

## Skill Version(s):

0.15.6 (source: server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
