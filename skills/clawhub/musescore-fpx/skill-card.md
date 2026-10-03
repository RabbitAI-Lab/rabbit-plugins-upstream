## Description:

Helps agents search MuseScore sheet music, inspect score and license metadata, and find official download links using a browser-connected shell workflow without an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agents use this skill to search MuseScore, inspect score availability and license details, and present official download links for manual use without running a MuseScore MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An untrusted CLI or browser extension could access activity in a paired browser tab.

Mitigation: Install only trusted @fetchproxy/cli and ContextMint Bridge releases, verify the extension hash or build from source, and restrict Chrome site access to musescore.com.

Risk: A resolved download link may not grant access to a score, and automated downloading could breach site terms.

Mitigation: Check the score's free or access status, open official links manually in the browser, and respect MuseScore's terms; do not automate purchases.

## Reference(s):

- [MuseScore endpoint and extraction reference](references/endpoints.md)
- [HTML store extraction helper](references/extract-store.js)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/musescore-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, JSON score metadata, Download links, Guidance]

**Output Format:** [Markdown with shell commands, JSON results, and URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Resolves official download links but does not download score files.]

## Skill Version(s):

1.1.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
