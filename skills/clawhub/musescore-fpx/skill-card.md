## Description:

Query musescore.com sheet music search results, score and license metadata, and official download links from a shell using the fpx CLI through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query MuseScore search and score metadata from scripts or shell workflows when the musescore-mcp server is not installed. It helps resolve score IDs, metadata, entitlement flags, render asset URLs, and official download links while relying on the user's own browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests run through the user's browser context via the fpx/Transporter bridge.

Mitigation: Install only if comfortable with that trust boundary, review the Transporter extension and @fetchproxy/cli setup, and scope use to the documented musescore.com profile.

Risk: Download URLs may require entitlement, and fpx can resolve links but cannot fetch protected score bytes.

Mitigation: Check is_free or hasAccess before relying on a download link, open resolved links manually in the signed-in browser tab, and stay within MuseScore terms.

## Reference(s):

- [MuseScore endpoints for fpx](artifact/references/endpoints.md)
- [MuseScore JSON store extractor](artifact/references/extract-store.js)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/musescore-fpx)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown with inline shell commands, JavaScript snippets, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill provides instructions and helper parsing code; it does not download score bytes through fpx.]

## Skill Version(s):

1.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
