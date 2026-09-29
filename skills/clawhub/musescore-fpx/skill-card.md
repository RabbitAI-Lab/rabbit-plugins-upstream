## Description:

Helps agents search MuseScore sheet music, inspect score and license metadata, and resolve official download links through a paired browser tab without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other MuseScore users can query sheet music listings and score details from a shell, then open eligible official download links in their browser. The skill resolves download URLs but does not download score files through the CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent browser-extension pairing can expose the MuseScore browsing session to the workflow.

Mitigation: Verify the extension release or build it from source, and use a dedicated browser profile or tab to limit session exposure.

Risk: Download links may require access rights, and use outside MuseScore's terms or for account-only purchases may be inappropriate.

Mitigation: Check score access before using a link, stay within MuseScore's terms, and avoid automating account-only purchases.

## Reference(s):

- [MuseScore endpoint and extraction reference](references/endpoints.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [MuseScore FPX release on ClawHub](https://clawhub.ai/chrischall/skills/musescore-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Text, Guidance]

**Output Format:** [Markdown with inline shell commands and extracted score metadata or download links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Download URLs must be opened in a browser; the CLI cannot fetch score files.]

## Skill Version(s):

1.1.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
