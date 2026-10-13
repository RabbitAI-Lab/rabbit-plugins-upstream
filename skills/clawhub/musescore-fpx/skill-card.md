## Description:

Queries MuseScore search results, score metadata, and official download links through a paired browser tab using the fpx CLI instead of an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search MuseScore, inspect score and license metadata, and resolve official download links in shell workflows without running the MuseScore MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Approved bridge pairing persists, so later fpx calls can reuse access to the MuseScore browser tab.

Mitigation: Verify the extension source, use a dedicated browser profile or minimally privileged tab, and revoke or reset pairing when no longer needed.

Risk: A resolved score download URL does not guarantee access to the file.

Mitigation: Check is_free or hasAccess before opening the official link in the browser; do not automate purchases.

## Reference(s):

- [MuseScore FPX on ClawHub](https://clawhub.ai/chrischall/skills/musescore-fpx)
- [MuseScore endpoint guide](references/endpoints.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Resolves official download URLs but does not download score files through fpx.]

## Skill Version(s):

1.1.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
