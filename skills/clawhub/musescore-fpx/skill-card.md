## Description:

Query musescore.com for sheet music search results, score and license metadata, and official download links from a shell using the fpx CLI through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve MuseScore search results, score metadata, license information, and resolvable official download links from shell workflows without running the MuseScore MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fpx CLI and Transporter extension use the user's browser session for musescore.com, and pairing persists after setup.

Mitigation: Install only if this browser-bridge posture is acceptable, keep site access limited to musescore.com, and remove the pairing when it is no longer needed.

Risk: Queries and download-link resolution may touch MuseScore content that is not free or otherwise authorized for the user.

Mitigation: Use the skill only for pages and files the user is entitled to access, check is_free or hasAccess before relying on download links, and review MuseScore's terms before automation.

Risk: The skill can resolve official download URLs but cannot fetch score bytes from the shell via fpx.

Mitigation: Treat resolved links as handoff URLs and open them in the signed-in browser tab when an authorized download is needed.

## Reference(s):

- [MuseScore endpoints for fpx](artifact/references/endpoints.md)
- [MuseScore JSON store extractor](artifact/references/extract-store.js)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/musescore-fpx)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with shell commands, jq projections, and JavaScript helper usage]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a local dependency-free Node helper to extract JSON from fetched MuseScore HTML.]

## Skill Version(s):

0.16.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
