## Description:

Query musescore.com for sheet music search results, score and license metadata, and official download links from a shell using the fpx CLI through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query MuseScore search and score-detail pages from shell workflows without running the musescore-mcp server. It helps retrieve public metadata and resolve official download URLs while leaving access checks and file downloads to the user's browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on fpx, the Transporter browser extension, and an active musescore.com tab, which expands the trusted local tooling involved in each request.

Mitigation: Review @fetchproxy/cli and the Transporter extension before installation, pair only the intended profile, and keep browser site access limited to musescore.com.

Risk: Resolved download links may be used outside the intended access checks for MuseScore content.

Mitigation: Use the skill only for public metadata and legitimate URL resolution, check is_free or hasAccess before relying on a link, and do not use resolved links to bypass MuseScore access rules or purchases.

Risk: Plain server-side requests cannot reproduce the browser session behavior required by MuseScore pages and static assets.

Mitigation: Run requests through the paired fpx browser bridge and treat direct curl or Node fetch failures as expected rather than bypassing site protections.

## Reference(s):

- [MuseScore endpoints for fpx](references/endpoints.md)
- [JSON store extractor](references/extract-store.js)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/musescore-fpx)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline shell and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces command guidance and JSON extraction patterns; the included extractor reads HTML from stdin and writes JSON to stdout.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
