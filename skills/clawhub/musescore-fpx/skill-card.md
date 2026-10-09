## Description:

Helps agents search MuseScore sheet music, inspect score and license metadata, and resolve official download links using fpx through a browser tab without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agents use this skill to find sheet music, inspect score details and licensing, and obtain official download URLs from MuseScore through their browser context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The browser extension makes MuseScore requests through the user's browser context.

Mitigation: Verify the extension source and use a dedicated browser profile or minimally privileged MuseScore tab if session exposure matters.

Risk: A resolved download link may not grant access to the score.

Mitigation: Check the score's free or access status, follow MuseScore's terms, and avoid automating purchases or sensitive authenticated activity.

## Reference(s):

- [MuseScore fpx ClawHub release](https://clawhub.ai/chrischall/skills/musescore-fpx)
- [MuseScore endpoint reference](references/endpoints.md)
- [HTML store extraction helper](references/extract-store.js)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Download URLs]

**Output Format:** [Markdown with shell examples and structured score data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Resolves official download links but does not download score files through fpx.]

## Skill Version(s):

1.1.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
