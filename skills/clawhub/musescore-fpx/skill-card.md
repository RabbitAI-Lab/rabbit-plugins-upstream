## Description:

Query musescore.com for sheet music search results, score and license metadata, and official download links from a shell using the fpx CLI through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation users use this skill to query MuseScore search and score metadata from shell workflows without running the musescore-mcp server. It helps resolve official download URLs and inspect public score metadata while keeping actual browsing and downloads in the user's browser context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires installing the Transporter browser extension and globally installing @fetchproxy/cli.

Mitigation: Install only when that browser bridge and global CLI are acceptable, restrict extension site access to musescore.com, and avoid running commands with sudo.

Risk: Examples write fetched HTML to predictable /tmp paths.

Mitigation: Use private mktemp directories or other user-controlled temporary paths for saved MuseScore HTML.

Risk: Download links may not grant access to the underlying score bytes, and fpx can resolve URLs but cannot fetch the bytes directly.

Mitigation: Check is_free or hasAccess before relying on a link, then open the resolved URL in the signed-in browser tab and stay within musescore.com's terms.

## Reference(s):

- [MuseScore endpoints for fpx](references/endpoints.md)
- [extract-store.js](references/extract-store.js)
- [ClawHub release page](https://clawhub.ai/chrischall/skills/musescore-fpx)
- [Publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, URLs, and JSON-processing examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are agent guidance and command snippets; fetched MuseScore HTML and parsed JSON are produced by the user's local fpx, Node, and jq commands.]

## Skill Version(s):

0.17.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
