## Description:

Query musescore.com for sheet music search results, score and license metadata, and official download links from a shell with the fpx CLI through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to search MuseScore and inspect score and license metadata from shell scripts or machines without the musescore-mcp server. It can resolve official download links, which users open in their browser.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The browser extension and CLI pairing grant access through an open MuseScore tab, and pairing remains active after use.

Mitigation: Review the CLI and extension before installation, verify the extension download, approve only the MuseScore domain and needed capabilities, and revoke pairing from the extension popup when access is no longer needed.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/chrischall/skills/musescore-fpx)
- [MuseScore endpoint guide](artifact/references/endpoints.md)
- [JSON store extraction script](artifact/references/extract-store.mjs)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ContextMint Bridge documentation](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration instructions]

**Output Format:** [Shell commands and extracted MuseScore data in JSON or readable text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [fpx resolves official download links but does not download score files; users open links in the browser.]

## Skill Version(s):

1.3.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
