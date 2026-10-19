## Description:

Guides agents in searching MuseScore, reading score and license metadata, and resolving official download links through a browser-connected command-line tool.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to find sheet music, inspect score and license details, and obtain official download links without running a MuseScore MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The browser extension and command-line package are required to access MuseScore through an open tab.

Mitigation: Review their provenance before installation and scope the browser profile to musescore.com.

Risk: Download links may refer to content outside the user's entitlement.

Mitigation: Check access before opening links; do not automate purchases or access content beyond entitlement.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/musescore-fpx)
- [MuseScore endpoint reference](references/endpoints.md)
- [Score data extraction script](references/extract-store.mjs)
- [ContextMint Bridge extension releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON, Guidance]

**Output Format:** [Markdown instructions and JSON score metadata or download URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Resolves official download links but does not download score files.]

## Skill Version(s):

1.1.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
