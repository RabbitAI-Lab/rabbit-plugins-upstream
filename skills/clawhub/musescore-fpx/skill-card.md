## Description:

Query musescore.com for sheet music search, score and license metadata, and official download links from a shell using the fpx CLI through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve MuseScore search results, score metadata, license details, and official download URLs through a browser-backed fpx workflow when the MuseScore MCP server is not installed or not desired.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow depends on a globally installed @fetchproxy/cli package and the Transporter browser extension.

Mitigation: Install only reviewed versions, prefer pinning the CLI version, avoid sudo, and keep the browser extension scoped to musescore.com.

Risk: The browser pairing can persist beyond a single use.

Mitigation: Revoke the fpx pairing when the workflow is no longer needed and periodically review active browser extension permissions.

Risk: The skill resolves official MuseScore download URLs but cannot fetch score bytes through fpx.

Mitigation: Use the resolved URL manually in the signed-in browser tab, check is_free or hasAccess before relying on a download, and stay within MuseScore terms.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/musescore-fpx)
- [MuseScore endpoints for fpx](references/endpoints.md)
- [JSON store extractor](references/extract-store.js)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands, Node.js snippets, URL patterns, and JSON extraction guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a paired Transporter browser extension, an open musescore.com tab, and fpx access through the musescore profile.]

## Skill Version(s):

0.17.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
