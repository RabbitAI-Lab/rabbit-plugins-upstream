## Description:

Query musescore.com for sheet music search results, score and license metadata, and official download links from a shell using the fpx CLI through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve MuseScore search results, score details, entitlement metadata, and download URL candidates from shell workflows when the MuseScore MCP server is not installed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Global installation of a third-party CLI and browser-extension pairing can increase local browser-bridge exposure.

Mitigation: Verify the @fetchproxy/cli package source and version, avoid elevated npm installs, and limit Transporter site access to musescore.com.

Risk: MuseScore queries depend on a browser tab that has cleared Cloudflare and may fail or return gated content outside the intended anonymous read surface.

Mitigation: Use the skill only for MuseScore pages you intend to query, respect musescore.com terms, and avoid automating purchases or account-only workflows.

Risk: Resolved download URLs may not actually provide file bytes unless the score is free or the user has access.

Mitigation: Check is_free or hasAccess before relying on a download URL and open resolved links manually in the signed-in browser.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/musescore-fpx)
- [MuseScore endpoints for fpx](artifact/references/endpoints.md)
- [extract-store.js](artifact/references/extract-store.js)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, endpoint patterns, and JSON/jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include fpx setup commands, jq projections, endpoint patterns, and Node extraction guidance; it resolves download URLs but does not download score bytes.]

## Skill Version(s):

0.17.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
