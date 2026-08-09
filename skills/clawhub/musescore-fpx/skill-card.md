## Description:

Query musescore.com for sheet music search results, score and license metadata, and official download links from a shell using the fpx CLI through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, automation users, and music researchers use this skill to retrieve MuseScore search results, score metadata, license details, and official download-link URLs from scripts or shell sessions without running the musescore-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a browser bridge with site access to musescore.com.

Mitigation: Keep the fpx profile and Transporter extension pairing scoped to MuseScore and review the extension site access before use.

Risk: MuseScore search, metadata, and download-link resolution may be subject to MuseScore terms and entitlement checks.

Mitigation: Review MuseScore's terms and verify that a score is free or otherwise accessible before using a resolved download URL.

Risk: Resolved download URLs are not fetched by fpx and may point to gated browser download flows.

Mitigation: Treat resolved URLs as links to open manually in the signed-in browser tab rather than as automated downloads.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/musescore-fpx)
- [MuseScore endpoints for fpx](references/endpoints.md)
- [MuseScore JSON store extractor](references/extract-store.js)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, jq projections, and JavaScript helper code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces human-reviewed commands and extracted JSON; fpx can resolve MuseScore download URLs but does not fetch score files.]

## Skill Version(s):

0.15.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
