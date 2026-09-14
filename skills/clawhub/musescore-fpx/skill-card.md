## Description:

Query musescore.com for sheet music search results, score and license metadata, and official download links from a shell using the fpx CLI through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query MuseScore search and score metadata through fpx, extract embedded JSON from returned HTML, and resolve official download links without running the MuseScore MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on @fetchproxy/cli and the Transporter browser extension for browser-mediated access to musescore.com.

Mitigation: Install trusted or pinned versions where possible, keep the fpx profile restricted to musescore.com, and remove the pairing when the skill is no longer needed.

Risk: Persistent fpx pairing reuses browser-mediated access after the initial approval.

Mitigation: Treat the paired browser profile as trusted access, review pairing state with fpx health, and revoke or remove the musescore profile when finished.

Risk: Download URLs may point to gated or rights-restricted score assets even when URL metadata is visible.

Mitigation: Check is_free or hasAccess before relying on a link, stay within MuseScore terms, and do not automate purchases.

## Reference(s):

- [MuseScore endpoints for fpx](references/endpoints.md)
- [MuseScore JSON store extractor](references/extract-store.js)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/musescore-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Code, Guidance]

**Output Format:** [Markdown with shell commands and JSON extraction examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses browser-mediated fpx calls and a dependency-free Node helper to extract JSON from MuseScore HTML.]

## Skill Version(s):

0.17.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
