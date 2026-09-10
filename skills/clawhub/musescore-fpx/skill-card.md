## Description:

Query musescore.com for sheet music search results, score and license metadata, and official download links from a shell through the fpx CLI and a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect MuseScore search results, score metadata, license details, and download-link availability from shell workflows when they do not want to run the MuseScore MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to install an external npm CLI globally.

Mitigation: Install only after reviewing the @fetchproxy/cli package and accepting the security posture described by the release evidence.

Risk: The skill relies on a persistent browser bridge pairing for musescore.com.

Mitigation: Keep browser site access restricted to musescore.com and revoke the pairing or extension site access when the skill is no longer needed.

Risk: The skill can resolve official MuseScore download URLs but cannot fetch score bytes itself.

Mitigation: Use it for search, metadata, license checks, and URL resolution; open eligible download links manually in the signed-in browser tab.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/musescore-fpx)
- [MuseScore endpoints for fpx](artifact/references/endpoints.md)
- [MuseScore JSON store extractor](artifact/references/extract-store.js)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, endpoint patterns, jq projections, and JavaScript helper code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the fpx CLI, a Transporter browser extension pairing scoped to musescore.com, and an open browser tab that has cleared MuseScore access checks.]

## Skill Version(s):

0.17.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
