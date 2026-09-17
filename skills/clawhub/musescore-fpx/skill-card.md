## Description:

Query musescore.com for sheet music search, score and license metadata, and official download links from a shell via @fetchproxy/cli using a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search MuseScore, inspect score metadata, resolve official download URLs, and extract embedded JSON-store data from fetched HTML without running the musescore-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to install an unpinned global proxy CLI and persistently pair it with a browser extension that can use a MuseScore browser session.

Mitigation: Install only if comfortable with that access, prefer a dedicated browser profile, verify the @fetchproxy/cli package and Transporter extension source before pairing, and remove the fpx profile or extension permission when finished.

Risk: The browser bridge depends on a MuseScore tab with Cloudflare already cleared, so requests can fail or act through a live browser session rather than an isolated API key.

Mitigation: Use the musescore.com-scoped profile only, check bridge health before use, and keep browser site access limited to musescore.com.

Risk: The artifact resolves official download URLs but cannot fetch protected score bytes through fpx.

Mitigation: Verify is_free or hasAccess before using a resolved link, open eligible links manually in the signed-in browser tab, and do not automate purchases or bypass MuseScore access controls.

## Reference(s):

- [MuseScore endpoints for fpx](references/endpoints.md)
- [extract-store.js](references/extract-store.js)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/musescore-fpx)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON extraction examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides fpx CLI setup, MuseScore URL patterns, JSON-store extraction, and download URL resolution; it does not fetch protected score bytes.]

## Skill Version(s):

0.17.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
