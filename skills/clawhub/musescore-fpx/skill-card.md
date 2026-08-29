## Description:

Query musescore.com for sheet music search results, score and license metadata, and official download links from a shell through the fpx CLI and a paired browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve MuseScore search results, score metadata, entitlement signals, and official download URLs from shell workflows without running the musescore-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a paired FetchProxy/Transporter browser bridge and a persistent fpx profile for musescore.com.

Mitigation: Keep browser extension site access limited to MuseScore and confirm the paired profile before use.

Risk: Resolved download URLs may point to browser-mediated or cross-origin locations that should not be trusted blindly.

Mitigation: Review download URLs manually in the browser and rely on the skill for read-only lookup and URL resolution.

Risk: MuseScore access and entitlement signals affect whether a resolved link is expected to work.

Mitigation: Check free-access or user-access metadata before using any resolved download link.

## Reference(s):

- [MuseScore endpoints for fpx](references/endpoints.md)
- [JSON store extractor](references/extract-store.js)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/musescore-fpx)
- [Publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JavaScript helper usage, URL patterns, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses user-directed, read-only browser-bridged requests; download files are not fetched by the skill.]

## Skill Version(s):

0.15.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
