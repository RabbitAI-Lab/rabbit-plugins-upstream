## Description:

Query musescore.com for sheet music search results, score and license metadata, and official download links from a shell using the fpx CLI through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve MuseScore search metadata, score details, license fields, and official download URLs from shell workflows when the musescore-mcp server is not installed or not desired.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser-bridge requests depend on the fpx CLI, the Transporter extension, and an active musescore.com tab, creating a third-party CLI and extension trust boundary.

Mitigation: Install only when comfortable with that trust boundary, keep the fpx profile scoped to musescore.com, and verify the active tab before making requests.

Risk: Resolved MuseScore download links may be subject to copyright, access, or terms restrictions.

Mitigation: Check the exposed entitlement fields before opening links and follow MuseScore copyright and terms guidance.

## Reference(s):

- [MuseScore endpoints for fpx](artifact/references/endpoints.md)
- [MuseScore JSON store extraction script](artifact/references/extract-store.js)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell, JavaScript, and jq command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the fpx CLI, the Transporter browser extension, and a musescore.com browser tab with the challenge cleared; resolves official download URLs but does not fetch score bytes.]

## Skill Version(s):

0.15.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
