## Description:

Helps agents query MuseScore search results, score metadata, and official download-link records from a shell through the fpx CLI and a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to prepare shell commands and parsing steps for MuseScore search, score-detail inspection, and official download-link resolution without running the MuseScore MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser-mediated access requires the Transporter/fpx tooling to use a musescore.com browser tab.

Mitigation: Keep browser site access limited to musescore.com, verify the Transporter pairing state, and review the external npm package and browser extension before use.

Risk: Resolved download links can point to content that is free, entitled, or server-gated.

Mitigation: Use resolved links only for scores the user is entitled to access, check is_free or hasAccess before relying on a link, and do not automate purchases.

Risk: MuseScore page data is hydrated from encoded HTML stores, so naive scraping can return missing or misleading results.

Mitigation: Use the bundled extractor and documented endpoint patterns, and treat missing keyed arrays as no result rather than falling back to unrelated feeds.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/musescore-fpx)
- [MuseScore endpoints for fpx](artifact/references/endpoints.md)
- [MuseScore JSON-store extractor](artifact/references/extract-store.js)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JavaScript helper usage, and JSON/jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill resolves download URLs and parses fetched HTML; it does not download score bytes for the agent.]

## Skill Version(s):

0.17.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
