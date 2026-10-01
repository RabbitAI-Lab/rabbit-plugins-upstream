## Description:

Search MuseScore sheet music, inspect score metadata, and obtain available download links or PDF output through a signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Musicians, educators, and other users can find arrangements, check score details and licensing, and request available downloads or PDFs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a signed-in MuseScore browser session to query scores.

Mitigation: Review the session access before installation and use only an account you are comfortable letting the agent query.

Risk: The browser bridge and external MCP server are required, but the server was not bundled for inspection.

Mitigation: Review and trust these separate components before installing or enabling them.

Risk: Download actions may expose file links, and PDF conversion may write a local file.

Mitigation: Require explicit confirmation before downloads or PDF output and review the destination path.

## Reference(s):

- [ClawHub musescore release](https://clawhub.ai/chrischall/skills/musescore)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Links, Files]

**Output Format:** [Markdown text with score metadata, download links, and optional PDF file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [PDF conversion may write a local file when an official PDF is unavailable.]

## Skill Version(s):

1.1.4 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
