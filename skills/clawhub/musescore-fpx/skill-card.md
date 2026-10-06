## Description:

Helps agents search MuseScore, inspect score and license metadata, and resolve official download links using a browser-backed command-line workflow without the MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agents use this skill to look up sheet music, review score and licensing details, and obtain official download links for material they are entitled to access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent browser pairing permits requests through the user's browser context.

Mitigation: Limit the extension's site access to musescore.com and verify the extension package before pairing.

Risk: A resolved download link does not establish permission to use the score.

Mitigation: Check access rights and license details before opening or using the link.

## Reference(s):

- [MuseScore fpx skill release](https://clawhub.ai/chrischall/skills/musescore-fpx)
- [MuseScore endpoint reference](artifact/references/endpoints.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON]

**Output Format:** [Markdown guidance and structured score metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Resolves official download URLs but does not save score files.]

## Skill Version(s):

1.1.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
