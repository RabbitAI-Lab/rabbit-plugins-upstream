## Description:

Search MuseScore sheet music and read score metadata via MCP. Triggers on phrases like "find sheet music for", "search MuseScore for", "is there a free arrangement of", "what's the license on this MuseScore score", "how many pages is", or any request involving MuseScore scores, arrangements, or sheet-music metadata. Requires musescore-mcp installed and the fetchproxy extension active with a signed-in musescore.com tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and music-focused agents use this skill to search MuseScore scores, inspect score metadata, resolve download links for free or entitled scores, and create PDFs through a signed-in browser-session MCP setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill under-discloses its browser-session dependency.

Mitigation: Review before installing and use only when a signed-in MuseScore tab and fetchproxy extension are acceptable for the deployment.

Risk: The skill can resolve download actions and write local PDF files in the SVG fallback path.

Mitigation: Require explicit user intent for download or PDF actions, confirm entitlement or free-score status, and review any requested output path before execution.

Risk: The security verdict is suspicious because the stated read-only posture does not fully cover download and local file creation behavior.

Mitigation: Prefer a release that separates search-only functions from download and PDF-writing functions or updates the documentation to disclose those behaviors clearly.

## Reference(s):

- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with JSON configuration snippets, tool-call summaries, download URLs, and optional local PDF file paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Depends on musescore-mcp, the fetchproxy extension, a signed-in MuseScore browser tab, and rsvg-convert for SVG-to-PDF fallback.]

## Skill Version(s):

0.16.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
