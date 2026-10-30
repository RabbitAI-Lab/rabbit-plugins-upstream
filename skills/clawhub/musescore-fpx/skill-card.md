## Description:

Guides agents in searching MuseScore and retrieving score metadata and official download links using a browser-connected shell CLI instead of an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agents use this skill to search MuseScore, inspect score and license details, and locate official download links from a shell without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The browser bridge reuses the user's browser session for MuseScore requests.

Mitigation: Limit extension site access to musescore.com and verify the extension release or build it from source.

Risk: Download links may point to content the user is not entitled to access.

Mitigation: Check score access flags and do not automate purchases or bypass MuseScore entitlements.

## Reference(s):

- [MuseScore FPX ClawHub release](https://clawhub.ai/chrischall/skills/musescore-fpx)
- [MuseScore endpoints for fpx](references/endpoints.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON]

**Output Format:** [Markdown with shell commands and JSON extraction examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Resolves download URLs but does not download score files.]

## Skill Version(s):

1.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
